"""Agent base class and Rock/Paper/Scissors implementations."""

import pygame
import random
import math
from typing import Tuple, Optional, List
from .config import Config, BEATS


class Agent:
    """Base class for all agents in the RPS world."""
    
    _id_counter = 0
    
    def __init__(
        self,
        kind: str,
        pos: Tuple[float, float],
        vel: Optional[Tuple[float, float]],
        radius: int,
        color: Tuple[int, int, int],
        config: Config,
        rng: random.Random,
        name: str = None
    ):
        """Initialize an agent.
        
        Args:
            kind: Type of agent ('rock', 'paper', or 'scissors')
            pos: Initial position (x, y)
            vel: Initial velocity (vx, vy), or None for random
            radius: Collision radius
            color: RGB color tuple
            config: Game configuration
            rng: Random number generator
            name: Agent name (optional)
        """
        self.id = Agent._id_counter
        Agent._id_counter += 1
        
        self.kind = kind
        self.name = name or f"{kind.capitalize()}-{self.id}"
        self.pos = pygame.Vector2(pos)
        self.radius = radius
        self.color = color
        self.config = config
        self.rng = rng
        
        # Kill tracking
        self.kills = 0
        
        # Set velocity
        if vel is None:
            # Random direction and speed based on kind
            angle = rng.uniform(0, 2 * math.pi)
            speed = self._get_random_speed()
            self.vel = pygame.Vector2(math.cos(angle) * speed, math.sin(angle) * speed)
            self.max_speed = speed
        else:
            self.vel = pygame.Vector2(vel)
            # Calculate max speed from provided velocity
            self.max_speed = self.vel.length() if self.vel.length() > 0 else self._get_random_speed()
        
        self.alive = True
        self.last_collision_tick = -10**9
        
        # Steering behavior properties
        self.max_force = self.max_speed * 0.1  # Steering force
        self.detection_range = float('inf')  # Global search - no range limit
        self.target = None  # Current target agent
        
        # Create sprite surface
        self.sprite = self._create_sprite()
        self.rect = self.sprite.get_rect(center=self.pos)
    
    def _get_random_speed(self) -> float:
        """Get random speed based on agent kind."""
        if self.kind == 'rock':
            return self.rng.uniform(*self.config.agent_speed_rock)
        elif self.kind == 'paper':
            return self.rng.uniform(*self.config.agent_speed_paper)
        else:  # scissors
            return self.rng.uniform(*self.config.agent_speed_scissors)
    
    def _create_sprite(self) -> pygame.Surface:
        """Create a sprite for the agent."""
        # Import here to avoid circular dependency
        from ..assets.sprites import create_rock_sprite, create_paper_sprite, create_scissors_sprite
        
        if self.kind == 'rock':
            return create_rock_sprite(self.radius, self.color)
        elif self.kind == 'paper':
            return create_paper_sprite(self.radius, self.color)
        elif self.kind == 'scissors':
            return create_scissors_sprite(self.radius, self.color)
        else:
            # Fallback to simple circle
            size = self.radius * 2
            surface = pygame.Surface((size, size), pygame.SRCALPHA)
            pygame.draw.circle(surface, self.color, (self.radius, self.radius), self.radius)
            border_color = tuple(max(0, c - 40) for c in self.color)
            pygame.draw.circle(surface, border_color, (self.radius, self.radius), self.radius, 2)
            return surface
    
    def update(self, dt: float, nearby_agents: Optional[List['Agent']] = None):
        """Update agent position and handle boundaries.
        
        Args:
            dt: Time delta in seconds
            nearby_agents: Optional list of nearby agents for steering behavior
        """
        if not self.alive:
            return
        
        # Apply steering behavior if enabled and agents provided
        if self.config.enable_steering and nearby_agents:
            self._apply_steering(nearby_agents, dt)
        
        # Limit velocity to max speed
        if self.vel.length() > self.max_speed:
            self.vel.scale_to_length(self.max_speed)
        
        # Update position
        self.pos += self.vel * dt
        
        # Handle boundaries
        if self.config.boundary_mode == "wrap":
            self._wrap_boundaries()
        else:  # bounce
            self._bounce_boundaries()
        
        # Update rect for drawing
        self.rect.center = (int(self.pos.x), int(self.pos.y))
    
    def _wrap_boundaries(self):
        """Wrap position around screen boundaries."""
        if self.pos.x < 0:
            self.pos.x += self.config.screen_width
        elif self.pos.x >= self.config.screen_width:
            self.pos.x -= self.config.screen_width
        
        if self.pos.y < 0:
            self.pos.y += self.config.screen_height
        elif self.pos.y >= self.config.screen_height:
            self.pos.y -= self.config.screen_height
    
    def _bounce_boundaries(self):
        """Bounce off screen boundaries."""
        if self.pos.x - self.radius < 0:
            self.pos.x = self.radius
            self.vel.x = abs(self.vel.x)
        elif self.pos.x + self.radius >= self.config.screen_width:
            self.pos.x = self.config.screen_width - self.radius
            self.vel.x = -abs(self.vel.x)
        
        if self.pos.y - self.radius < 0:
            self.pos.y = self.radius
            self.vel.y = abs(self.vel.y)
        elif self.pos.y + self.radius >= self.config.screen_height:
            self.pos.y = self.config.screen_height - self.radius
            self.vel.y = -abs(self.vel.y)
    
    def draw(self, surface: pygame.Surface):
        """Draw the agent on the surface.
        
        Args:
            surface: Pygame surface to draw on
        """
        if self.alive:
            surface.blit(self.sprite, self.rect)
    
    def collides_with(self, other: 'Agent') -> bool:
        """Check if this agent collides with another.
        
        Args:
            other: Another agent
            
        Returns:
            True if agents are colliding
        """
        if not (self.alive and other.alive):
            return False
        
        r = self.radius + other.radius
        return self.pos.distance_squared_to(other.pos) <= r * r
    
    def compare(self, other: 'Agent') -> int:
        """Compare this agent with another using R-P-S rules.
        
        Args:
            other: Another agent
            
        Returns:
            1 if this agent wins, -1 if loses, 0 if tie
        """
        if self.kind == other.kind:
            return 0
        return 1 if BEATS[self.kind] == other.kind else -1
    
    def kill(self):
        """Mark this agent as dead."""
        self.alive = False
    
    def soft_bounce(self, other: 'Agent'):
        """Apply a soft bounce when colliding with same type.
        
        Args:
            other: Another agent of the same type
        """
        # Calculate normal vector from other to self
        if self.pos.distance_squared_to(other.pos) < 0.01:
            # Too close, random bounce
            angle = self.rng.uniform(0, 2 * math.pi)
            normal = pygame.Vector2(math.cos(angle), math.sin(angle))
        else:
            normal = (self.pos - other.pos).normalize()
        
        # Reflect velocity along normal
        dot = self.vel.dot(normal)
        if dot < 0:  # Moving towards each other
            self.vel -= 2 * dot * normal
    
    def _apply_steering(self, nearby_agents: List['Agent'], dt: float):
        """Apply steering behavior to hunt prey (global search, no flee behavior).
        
        Args:
            nearby_agents: All agents in the world
            dt: Time delta in seconds
        """
        # Find prey (agents this one beats) - GLOBAL SEARCH
        prey = []
        
        for other in nearby_agents:
            if not other.alive or other.id == self.id:
                continue
            
            comparison = self.compare(other)
            if comparison > 0:  # This agent beats other
                distance = self.pos.distance_to(other.pos)
                prey.append((other, distance))
        
        # If no prey exists anywhere in the world, STOP and accept defeat
        if not prey:
            # Gradually slow down to a stop
            self.vel *= 0.95  # Damping factor
            if self.vel.length() < 1.0:  # Stop completely when very slow
                self.vel = pygame.Vector2(0, 0)
            return
        
        # Seek nearest prey (NO FLEE BEHAVIOR - prey is clueless)
        prey.sort(key=lambda x: x[1])
        nearest_prey = prey[0][0]
        self.target = nearest_prey
        seek_force = self._seek(nearest_prey.pos)
        
        # Apply steering force (only seeking, no fleeing)
        if seek_force.length() > 0:
            if seek_force.length() > self.max_force:
                seek_force.scale_to_length(self.max_force)
            self.vel += seek_force
    
    def _has_prey_in_world(self, all_agents: List['Agent']) -> bool:
        """Check if any prey exists in the entire world.
        
        Args:
            all_agents: All agents in the world
            
        Returns:
            True if at least one prey exists, False otherwise
        """
        for other in all_agents:
            if not other.alive or other.id == self.id:
                continue
            if self.compare(other) > 0:  # Found prey
                return True
        return False
    
    def _seek(self, target_pos: pygame.Vector2) -> pygame.Vector2:
        """Calculate steering force to seek a target position.
        
        Args:
            target_pos: Target position to seek
            
        Returns:
            Steering force vector
        """
        desired = target_pos - self.pos
        if desired.length() > 0:
            desired.scale_to_length(self.max_speed)
            steering = desired - self.vel
            return steering
        return pygame.Vector2(0, 0)
    
    def _flee(self, threat_pos: pygame.Vector2) -> pygame.Vector2:
        """Calculate steering force to flee from a threat.
        
        Args:
            threat_pos: Position to flee from
            
        Returns:
            Steering force vector
        """
        desired = self.pos - threat_pos
        if desired.length() > 0:
            desired.scale_to_length(self.max_speed)
            steering = desired - self.vel
            return steering
        return pygame.Vector2(0, 0)


class Rock(Agent):
    """Rock agent - beats Scissors."""
    
    def __init__(self, pos: Tuple[float, float], vel: Optional[Tuple[float, float]], 
                 config: Config, rng: random.Random, name: str = None):
        super().__init__(
            kind='rock',
            pos=pos,
            vel=vel,
            radius=config.agent_radius_rock,
            color=config.color_rock,
            config=config,
            rng=rng,
            name=name
        )


class Paper(Agent):
    """Paper agent - beats Rock."""
    
    def __init__(self, pos: Tuple[float, float], vel: Optional[Tuple[float, float]], 
                 config: Config, rng: random.Random, name: str = None):
        super().__init__(
            kind='paper',
            pos=pos,
            vel=vel,
            radius=config.agent_radius_paper,
            color=config.color_paper,
            config=config,
            rng=rng,
            name=name
        )


class Scissors(Agent):
    """Scissors agent - beats Paper."""
    
    def __init__(self, pos: Tuple[float, float], vel: Optional[Tuple[float, float]], 
                 config: Config, rng: random.Random, name: str = None):
        super().__init__(
            kind='scissors',
            pos=pos,
            vel=vel,
            radius=config.agent_radius_scissors,
            color=config.color_scissors,
            config=config,
            rng=rng,
            name=name
        )

