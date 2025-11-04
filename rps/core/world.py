"""World orchestration and simulation management."""

import pygame
import random
from typing import List, Tuple, Optional, Dict
from .agent import Agent
from .factory import AgentFactory
from .collision import CollisionResolver
from .config import Config, KINDS


class World:
    """Manages all agents and simulation state."""
    
    def __init__(self, config: Config, logger=None):
        """Initialize the world.
        
        Args:
            config: Game configuration
            logger: Optional analysis logger
        """
        self.config = config
        self.logger = logger
        self.rng = random.Random(config.seed)
        
        # Agent factory for creating all agents
        self.factory = AgentFactory(config, self.rng)
        
        # Agent management
        self.agents: List[Agent] = []
        self.by_kind: Dict[str, List[Agent]] = {kind: [] for kind in KINDS}
        
        # Collision handling
        self.collision_resolver = CollisionResolver(config)
        
        # Simulation state
        self.tick = 0
        self.paused = False
        self.debug_mode = False
        
        # Victory state
        self.game_over = False
        self.winner_kind = None
        self.winner_agents = []
        
        # Track all agents ever spawned (for victory scoreboard)
        self.all_agents_history = []
    
    def spawn(
        self, 
        kind: str, 
        pos: Tuple[float, float], 
        vel: Optional[Tuple[float, float]] = None
    ) -> Optional[Agent]:
        """Spawn a single agent at a specific position using the factory.
        
        Args:
            kind: Agent type ('rock', 'paper', or 'scissors')
            pos: Position (x, y)
            vel: Optional velocity (vx, vy)
            
        Returns:
            The spawned agent, or None if population cap reached
        """
        if len(self.agents) >= self.config.max_population:
            return None
        
        # Use factory to create agent
        agent = self.factory.create_agent(kind, pos, vel)
        
        self.agents.append(agent)
        self.by_kind[kind].append(agent)
        self.all_agents_history.append(agent)  # Track for victory scoreboard
        
        # Log spawn event
        if self.logger:
            self.logger.log_spawn(agent.id, agent.kind, agent.pos.x, agent.pos.y, self.tick)
        
        return agent
    
    def spawn_random(self, kind: str, count: int = 1) -> List[Agent]:
        """Spawn multiple agents at random positions using the factory.
        
        Args:
            kind: Agent type
            count: Number of agents to spawn
            
        Returns:
            List of spawned agents
        """
        spawned = []
        for _ in range(count):
            if len(self.agents) >= self.config.max_population:
                break
            
            # Use factory to create agent at random position
            agent = self.factory.create_random_agent(
                kind, 
                (self.config.screen_width, self.config.screen_height)
            )
            
            self.agents.append(agent)
            self.by_kind[kind].append(agent)
            self.all_agents_history.append(agent)  # Track for victory scoreboard
            
            # Log spawn event
            if self.logger:
                self.logger.log_spawn(agent.id, agent.kind, agent.pos.x, agent.pos.y, self.tick)
            
            spawned.append(agent)
        
        return spawned
    
    def spawn_batch(self, batch_size: int = None):
        """Spawn a batch of each kind randomly.
        
        Args:
            batch_size: Number of each kind to spawn (uses config default if None)
        """
        size = batch_size or self.config.spawn_batch_size
        for kind in KINDS:
            self.spawn_random(kind, size)
    
    def update(self, dt: float):
        """Update all agents and handle collisions.
        
        Args:
            dt: Time delta in seconds
        """
        if self.paused or self.game_over:
            return
        
        # Update all living agents with steering behavior
        for agent in self.agents:
            if agent.alive:
                # Pass all agents for steering behavior
                # (agents will filter based on detection range)
                agent.update(dt, self.agents if self.config.enable_steering else None)
        
        # Detect and resolve collisions
        self.resolve_collisions()
        
        # Remove dead agents
        self.remove_dead()
        
        # Check for victory
        self._check_victory()
        
        # Increment tick
        self.tick += 1
    
    def resolve_collisions(self):
        """Detect and resolve all collisions."""
        # Get all living agents
        living = [a for a in self.agents if a.alive]
        
        # Detect collisions
        pairs = self.collision_resolver.detect_collisions(living, self.tick)
        
        # Resolve collisions
        self.collision_resolver.resolve_collisions(pairs, self.tick, self.logger)
    
    def remove_dead(self):
        """Remove dead agents from tracking lists."""
        # Filter out dead agents
        self.agents = [a for a in self.agents if a.alive]
        
        # Update by_kind tracking
        for kind in KINDS:
            self.by_kind[kind] = [a for a in self.by_kind[kind] if a.alive]
    
    def draw(self, surface: pygame.Surface):
        """Draw all agents.
        
        Args:
            surface: Pygame surface to draw on
        """
        for agent in self.agents:
            if agent.alive:
                agent.draw(surface)
                
                # Draw name if enabled
                if self.config.show_names:
                    self._draw_agent_name(surface, agent)
        
        # Draw debug info if enabled
        if self.debug_mode:
            self._draw_debug(surface)
    
    def _draw_agent_name(self, surface: pygame.Surface, agent):
        """Draw agent name above sprite.
        
        Args:
            surface: Surface to draw on
            agent: Agent to draw name for
        """
        if not hasattr(self, '_name_font'):
            self._name_font = pygame.font.Font(None, 16)
        
        # Render name
        name_surface = self._name_font.render(agent.name, True, (255, 255, 255))
        name_rect = name_surface.get_rect(center=(agent.pos.x, agent.pos.y - agent.radius - 10))
        
        # Draw semi-transparent background
        bg_rect = name_rect.inflate(4, 2)
        bg_surface = pygame.Surface((bg_rect.width, bg_rect.height), pygame.SRCALPHA)
        bg_surface.fill((0, 0, 0, 180))
        surface.blit(bg_surface, bg_rect.topleft)
        
        # Draw name
        surface.blit(name_surface, name_rect)
    
    def _draw_debug(self, surface: pygame.Surface):
        """Draw debug information (collision radii, velocities, etc.).
        
        Args:
            surface: Pygame surface to draw on
        """
        for agent in self.agents:
            if agent.alive:
                # Draw collision circle
                pygame.draw.circle(
                    surface, 
                    (255, 255, 255), 
                    (int(agent.pos.x), int(agent.pos.y)), 
                    agent.radius, 
                    1
                )
                
                # Draw velocity vector (only if moving)
                if agent.vel.length() > 0:
                    end_pos = agent.pos + agent.vel.normalize() * agent.radius * 2
                    pygame.draw.line(
                        surface,
                        (0, 255, 0),
                        (int(agent.pos.x), int(agent.pos.y)),
                        (int(end_pos.x), int(end_pos.y)),
                        2
                    )
    
    def clear(self):
        """Remove all agents and reset game state."""
        self.agents.clear()
        for kind in KINDS:
            self.by_kind[kind].clear()
        self.all_agents_history.clear()
        
        # Reset victory state
        self.game_over = False
        self.winner_kind = None
        self.winner_agents = []
    
    def reset(self, new_seed: Optional[int] = None):
        """Reset the world with a new seed.
        
        Args:
            new_seed: Optional new random seed
        """
        self.clear()
        if new_seed is not None:
            self.config.seed = new_seed
        else:
            self.config.seed = random.randint(0, 999999)
        self.rng = random.Random(self.config.seed)
        
        # Recreate factory with new RNG
        self.factory = AgentFactory(self.config, self.rng)
        
        self.tick = 0
        if self.logger:
            self.logger.clear()
    
    def get_counts(self) -> Dict[str, int]:
        """Get count of living agents by kind.
        
        Returns:
            Dictionary mapping kind to count
        """
        return {kind: len(agents) for kind, agents in self.by_kind.items()}
    
    def get_total_count(self) -> int:
        """Get total number of living agents.
        
        Returns:
            Total agent count
        """
        return len(self.agents)
    
    def _check_victory(self):
        """Check if one faction has won."""
        if self.game_over:
            return
        
        counts = self.get_counts()
        kinds_alive = [kind for kind, count in counts.items() if count > 0]
        
        # Victory if only one kind remains
        if len(kinds_alive) == 1:
            self.game_over = True
            self.winner_kind = kinds_alive[0]
            # Get ALL agents from winning faction (including dead ones)
            self.winner_agents = [agent for agent in self.all_agents_history if agent.kind == self.winner_kind]
            # Sort by kills (descending), then by name
            self.winner_agents.sort(key=lambda a: (-a.kills, a.name))
    
    def get_scoreboard(self) -> List[Tuple[str, int]]:
        """Get scoreboard of winners sorted by kills.
        
        Returns:
            List of (name, kills) tuples
        """
        if not self.game_over:
            return []
        return [(agent.name, agent.kills) for agent in self.winner_agents]

