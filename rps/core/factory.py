"""Factory for creating agents with proper encapsulation."""

import random
from typing import Tuple, Optional, Dict, Type
from .agent import Agent, Rock, Paper, Scissors
from .config import Config, KINDS
from .names import NameGenerator


class AgentFactory:
    """Factory class for creating and managing agent instances.
    
    This factory encapsulates all agent creation logic and provides
    a single point of control for spawning agents.
    """
    
    def __init__(self, config: Config, rng: random.Random):
        """Initialize the factory.
        
        Args:
            config: Game configuration
            rng: Random number generator for deterministic behavior
        """
        self.config = config
        self.rng = rng
        self.name_generator = NameGenerator(config.seed)
        
        # Registry mapping kind strings to agent classes
        self._registry: Dict[str, Type[Agent]] = {
            'rock': Rock,
            'paper': Paper,
            'scissors': Scissors
        }
    
    def create_agent(
        self, 
        kind: str, 
        pos: Tuple[float, float], 
        vel: Optional[Tuple[float, float]] = None
    ) -> Agent:
        """Create a single agent of the specified type.
        
        Args:
            kind: Type of agent ('rock', 'paper', or 'scissors')
            pos: Initial position (x, y)
            vel: Optional initial velocity (vx, vy)
            
        Returns:
            New agent instance
            
        Raises:
            ValueError: If kind is not recognized
        """
        if kind not in self._registry:
            raise ValueError(f"Unknown agent kind: {kind}. Valid kinds: {list(self._registry.keys())}")
        
        agent_class = self._registry[kind]
        name = self.name_generator.generate_name(kind)
        return agent_class(pos, vel, self.config, self.rng, name)
    
    def create_random_agent(
        self, 
        kind: str, 
        bounds: Optional[Tuple[int, int]] = None
    ) -> Agent:
        """Create an agent at a random position within bounds.
        
        Args:
            kind: Type of agent to create
            bounds: Optional (width, height) bounds. Uses config if not provided.
            
        Returns:
            New agent at random position
        """
        if bounds is None:
            bounds = (self.config.screen_width, self.config.screen_height)
        
        x = self.rng.uniform(0, bounds[0])
        y = self.rng.uniform(0, bounds[1])
        
        return self.create_agent(kind, (x, y))
    
    def create_batch(
        self, 
        kind: str, 
        count: int,
        bounds: Optional[Tuple[int, int]] = None
    ) -> list:
        """Create multiple agents of the same type.
        
        Args:
            kind: Type of agent to create
            count: Number of agents to create
            bounds: Optional bounds for random positioning
            
        Returns:
            List of newly created agents
        """
        return [self.create_random_agent(kind, bounds) for _ in range(count)]
    
    def create_balanced_population(
        self, 
        count_per_kind: int,
        bounds: Optional[Tuple[int, int]] = None
    ) -> Dict[str, list]:
        """Create a balanced population of all agent types.
        
        Args:
            count_per_kind: Number of each agent type to create
            bounds: Optional bounds for random positioning
            
        Returns:
            Dictionary mapping kind to list of agents
        """
        population = {}
        for kind in KINDS:
            population[kind] = self.create_batch(kind, count_per_kind, bounds)
        return population
    
    def register_agent_type(self, kind: str, agent_class: Type[Agent]):
        """Register a new agent type with the factory.
        
        This allows for runtime extension of available agent types.
        
        Args:
            kind: String identifier for the agent type
            agent_class: Agent class to register
        """
        self._registry[kind] = agent_class
    
    def get_available_kinds(self) -> list:
        """Get list of all registered agent kinds.
        
        Returns:
            List of agent kind strings
        """
        return list(self._registry.keys())
    
    def get_agent_class(self, kind: str) -> Type[Agent]:
        """Get the agent class for a given kind.
        
        Args:
            kind: Agent kind string
            
        Returns:
            Agent class
            
        Raises:
            ValueError: If kind is not registered
        """
        if kind not in self._registry:
            raise ValueError(f"Unknown agent kind: {kind}")
        return self._registry[kind]

