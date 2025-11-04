"""Collision detection and resolution."""

from typing import List, Tuple, Optional
from .agent import Agent


class CollisionResolver:
    """Handles collision detection and resolution between agents."""
    
    def __init__(self, config):
        """Initialize collision resolver.
        
        Args:
            config: Game configuration
        """
        self.config = config
        self.collision_pairs = []
    
    def detect_collisions(self, agents: List[Agent], tick: int) -> List[Tuple[Agent, Agent]]:
        """Detect all colliding pairs of agents.
        
        Args:
            agents: List of active agents
            tick: Current game tick
            
        Returns:
            List of colliding agent pairs
        """
        pairs = []
        n = len(agents)
        
        for i in range(n):
            agent_i = agents[i]
            if not agent_i.alive:
                continue
            
            # Skip if recently collided
            if tick - agent_i.last_collision_tick < self.config.collision_cooldown_frames:
                continue
            
            for j in range(i + 1, n):
                agent_j = agents[j]
                if not agent_j.alive:
                    continue
                
                # Skip if recently collided
                if tick - agent_j.last_collision_tick < self.config.collision_cooldown_frames:
                    continue
                
                if agent_i.collides_with(agent_j):
                    pairs.append((agent_i, agent_j))
        
        return pairs
    
    def resolve_collisions(
        self, 
        pairs: List[Tuple[Agent, Agent]], 
        tick: int,
        logger=None
    ) -> List[Tuple[Agent, Agent, str]]:
        """Resolve collisions between agent pairs.
        
        Args:
            pairs: List of colliding agent pairs
            tick: Current game tick
            logger: Optional event logger
            
        Returns:
            List of (winner, loser, outcome_type) tuples
        """
        outcomes = []
        
        # Sort pairs for deterministic processing
        sorted_pairs = sorted(pairs, key=lambda p: (min(p[0].id, p[1].id), max(p[0].id, p[1].id)))
        
        for agent_a, agent_b in sorted_pairs:
            # Skip if either agent is already dead
            if not (agent_a.alive and agent_b.alive):
                continue
            
            # Update collision timestamps
            agent_a.last_collision_tick = tick
            agent_b.last_collision_tick = tick
            
            # Compare agents
            result = agent_a.compare(agent_b)
            
            if result > 0:
                # agent_a wins
                agent_a.kills += 1  # Track kill
                agent_b.kill()
                outcomes.append((agent_a, agent_b, 'kill'))
                
                if logger:
                    logger.log_collision(
                        winner_id=agent_a.id,
                        winner_kind=agent_a.kind,
                        loser_id=agent_b.id,
                        loser_kind=agent_b.kind,
                        x=agent_b.pos.x,
                        y=agent_b.pos.y,
                        tick=tick
                    )
                
            elif result < 0:
                # agent_b wins
                agent_b.kills += 1  # Track kill
                agent_a.kill()
                outcomes.append((agent_b, agent_a, 'kill'))
                
                if logger:
                    logger.log_collision(
                        winner_id=agent_b.id,
                        winner_kind=agent_b.kind,
                        loser_id=agent_a.id,
                        loser_kind=agent_a.kind,
                        x=agent_a.pos.x,
                        y=agent_a.pos.y,
                        tick=tick
                    )
                
            else:
                # Tie - optional soft bounce
                if self.config.bounce_on_tie:
                    agent_a.soft_bounce(agent_b)
                    agent_b.soft_bounce(agent_a)
                    outcomes.append((agent_a, agent_b, 'bounce'))
        
        return outcomes

