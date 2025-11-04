"""Tests for AgentFactory."""

import unittest
import random
import pygame
from rps.core.factory import AgentFactory
from rps.core.agent import Rock, Paper, Scissors
from rps.core.config import Config


class TestAgentFactory(unittest.TestCase):
    """Test AgentFactory class."""
    
    @classmethod
    def setUpClass(cls):
        """Initialize pygame for tests."""
        pygame.init()
        pygame.display.set_mode((1, 1), pygame.HIDDEN)
    
    def setUp(self):
        """Set up test fixtures."""
        self.config = Config(seed=42)
        self.rng = random.Random(42)
        self.factory = AgentFactory(self.config, self.rng)
    
    def test_create_rock(self):
        """Test creating a Rock agent."""
        agent = self.factory.create_agent('rock', (100, 100))
        
        self.assertIsInstance(agent, Rock)
        self.assertEqual(agent.kind, 'rock')
        self.assertEqual(agent.pos.x, 100)
        self.assertEqual(agent.pos.y, 100)
    
    def test_create_paper(self):
        """Test creating a Paper agent."""
        agent = self.factory.create_agent('paper', (200, 200))
        
        self.assertIsInstance(agent, Paper)
        self.assertEqual(agent.kind, 'paper')
    
    def test_create_scissors(self):
        """Test creating a Scissors agent."""
        agent = self.factory.create_agent('scissors', (300, 300))
        
        self.assertIsInstance(agent, Scissors)
        self.assertEqual(agent.kind, 'scissors')
    
    def test_create_invalid_kind(self):
        """Test that invalid kind raises ValueError."""
        with self.assertRaises(ValueError):
            self.factory.create_agent('invalid', (100, 100))
    
    def test_create_random_agent(self):
        """Test creating agent at random position."""
        agent = self.factory.create_random_agent('rock')
        
        self.assertIsInstance(agent, Rock)
        self.assertTrue(0 <= agent.pos.x < self.config.screen_width)
        self.assertTrue(0 <= agent.pos.y < self.config.screen_height)
    
    def test_create_batch(self):
        """Test creating multiple agents."""
        agents = self.factory.create_batch('paper', 5)
        
        self.assertEqual(len(agents), 5)
        for agent in agents:
            self.assertIsInstance(agent, Paper)
            self.assertEqual(agent.kind, 'paper')
    
    def test_create_balanced_population(self):
        """Test creating balanced population."""
        population = self.factory.create_balanced_population(3)
        
        self.assertEqual(len(population), 3)  # rock, paper, scissors
        self.assertEqual(len(population['rock']), 3)
        self.assertEqual(len(population['paper']), 3)
        self.assertEqual(len(population['scissors']), 3)
    
    def test_get_available_kinds(self):
        """Test getting available agent kinds."""
        kinds = self.factory.get_available_kinds()
        
        self.assertIn('rock', kinds)
        self.assertIn('paper', kinds)
        self.assertIn('scissors', kinds)
    
    def test_get_agent_class(self):
        """Test getting agent class by kind."""
        rock_class = self.factory.get_agent_class('rock')
        paper_class = self.factory.get_agent_class('paper')
        scissors_class = self.factory.get_agent_class('scissors')
        
        self.assertEqual(rock_class, Rock)
        self.assertEqual(paper_class, Paper)
        self.assertEqual(scissors_class, Scissors)
    
    def test_deterministic_with_seed(self):
        """Test that same seed produces same positions."""
        factory1 = AgentFactory(Config(seed=123), random.Random(123))
        factory2 = AgentFactory(Config(seed=123), random.Random(123))
        
        agent1 = factory1.create_random_agent('rock')
        agent2 = factory2.create_random_agent('rock')
        
        self.assertEqual(agent1.pos.x, agent2.pos.x)
        self.assertEqual(agent1.pos.y, agent2.pos.y)


if __name__ == '__main__':
    unittest.main()

