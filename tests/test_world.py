"""Tests for World class."""

import unittest
import random
import pygame
from rps.core.world import World
from rps.core.config import Config


class TestWorld(unittest.TestCase):
    """Test World orchestration."""
    
    @classmethod
    def setUpClass(cls):
        """Initialize pygame for tests."""
        pygame.init()
        pygame.display.set_mode((1, 1), pygame.HIDDEN)
    
    def setUp(self):
        """Set up test fixtures."""
        self.config = Config(seed=42, max_population=100)
        self.world = World(self.config)
    
    def test_spawn_single_agent(self):
        """Test spawning a single agent."""
        agent = self.world.spawn('rock', (100, 100))
        
        self.assertIsNotNone(agent)
        self.assertEqual(agent.kind, 'rock')
        self.assertEqual(len(self.world.agents), 1)
        self.assertEqual(len(self.world.by_kind['rock']), 1)
    
    def test_spawn_multiple_kinds(self):
        """Test spawning multiple agent types."""
        self.world.spawn('rock', (100, 100))
        self.world.spawn('paper', (200, 200))
        self.world.spawn('scissors', (300, 300))
        
        self.assertEqual(len(self.world.agents), 3)
        self.assertEqual(len(self.world.by_kind['rock']), 1)
        self.assertEqual(len(self.world.by_kind['paper']), 1)
        self.assertEqual(len(self.world.by_kind['scissors']), 1)
    
    def test_spawn_random(self):
        """Test random spawning."""
        agents = self.world.spawn_random('rock', 5)
        
        self.assertEqual(len(agents), 5)
        self.assertEqual(len(self.world.agents), 5)
        
        # Check all are rocks
        for agent in agents:
            self.assertEqual(agent.kind, 'rock')
    
    def test_spawn_batch(self):
        """Test batch spawning."""
        self.config.spawn_batch_size = 3
        self.world.spawn_batch()
        
        # Should have 3 of each kind
        self.assertEqual(len(self.world.by_kind['rock']), 3)
        self.assertEqual(len(self.world.by_kind['paper']), 3)
        self.assertEqual(len(self.world.by_kind['scissors']), 3)
        self.assertEqual(len(self.world.agents), 9)
    
    def test_population_cap(self):
        """Test population cap is enforced."""
        self.config.max_population = 5
        
        # Spawn 10, but only 5 should succeed
        agents = self.world.spawn_random('rock', 10)
        
        self.assertEqual(len(agents), 5)
        self.assertEqual(len(self.world.agents), 5)
    
    def test_clear_world(self):
        """Test clearing all agents."""
        self.world.spawn_random('rock', 5)
        self.world.spawn_random('paper', 5)
        
        self.assertEqual(len(self.world.agents), 10)
        
        self.world.clear()
        
        self.assertEqual(len(self.world.agents), 0)
        self.assertEqual(len(self.world.by_kind['rock']), 0)
        self.assertEqual(len(self.world.by_kind['paper']), 0)
    
    def test_update_removes_dead_agents(self):
        """Test that dead agents are removed during update."""
        rock = self.world.spawn('rock', (100, 100))
        scissors = self.world.spawn('scissors', (110, 100))
        
        self.assertEqual(len(self.world.agents), 2)
        
        # Update should detect collision and remove scissors
        self.world.update(0.016)
        
        # Scissors should be dead and removed
        self.assertEqual(len(self.world.agents), 1)
        self.assertEqual(self.world.agents[0], rock)
    
    def test_get_counts(self):
        """Test getting agent counts."""
        self.world.spawn_random('rock', 3)
        self.world.spawn_random('paper', 5)
        self.world.spawn_random('scissors', 2)
        
        counts = self.world.get_counts()
        
        self.assertEqual(counts['rock'], 3)
        self.assertEqual(counts['paper'], 5)
        self.assertEqual(counts['scissors'], 2)
    
    def test_reset_world(self):
        """Test resetting the world."""
        self.world.spawn_random('rock', 5)
        old_seed = self.world.config.seed
        
        self.world.reset(new_seed=123)
        
        self.assertEqual(len(self.world.agents), 0)
        self.assertEqual(self.world.config.seed, 123)
        self.assertEqual(self.world.tick, 0)
    
    def test_deterministic_with_seed(self):
        """Test that same seed produces same results."""
        # First run
        world1 = World(Config(seed=42))
        world1.spawn_random('rock', 3)
        positions1 = [(a.pos.x, a.pos.y) for a in world1.agents]
        
        # Second run with same seed
        world2 = World(Config(seed=42))
        world2.spawn_random('rock', 3)
        positions2 = [(a.pos.x, a.pos.y) for a in world2.agents]
        
        # Should be identical
        self.assertEqual(positions1, positions2)


if __name__ == '__main__':
    unittest.main()

