"""Tests for collision detection and resolution."""

import unittest
import random
import pygame
from rps.core.agent import Rock, Paper, Scissors
from rps.core.collision import CollisionResolver
from rps.core.config import Config


class TestCollision(unittest.TestCase):
    """Test collision detection and resolution."""
    
    @classmethod
    def setUpClass(cls):
        """Initialize pygame for tests."""
        pygame.init()
        pygame.display.set_mode((1, 1), pygame.HIDDEN)
    
    def setUp(self):
        """Set up test fixtures."""
        self.config = Config(seed=42)
        self.rng = random.Random(42)
        self.resolver = CollisionResolver(self.config)
    
    def test_detect_collision_between_agents(self):
        """Test detecting collision between two agents."""
        rock = Rock((100, 100), None, self.config, self.rng)
        scissors = Scissors((110, 100), None, self.config, self.rng)
        
        agents = [rock, scissors]
        pairs = self.resolver.detect_collisions(agents, tick=0)
        
        self.assertEqual(len(pairs), 1)
        self.assertIn((rock, scissors), pairs)
    
    def test_no_collision_when_separated(self):
        """Test no collision detected when agents are far apart."""
        rock = Rock((100, 100), None, self.config, self.rng)
        scissors = Scissors((300, 300), None, self.config, self.rng)
        
        agents = [rock, scissors]
        pairs = self.resolver.detect_collisions(agents, tick=0)
        
        self.assertEqual(len(pairs), 0)
    
    def test_resolve_rock_beats_scissors(self):
        """Test resolution: Rock beats Scissors."""
        rock = Rock((100, 100), None, self.config, self.rng)
        scissors = Scissors((110, 100), None, self.config, self.rng)
        
        pairs = [(rock, scissors)]
        outcomes = self.resolver.resolve_collisions(pairs, tick=0)
        
        self.assertEqual(len(outcomes), 1)
        winner, loser, outcome_type = outcomes[0]
        
        self.assertEqual(winner, rock)
        self.assertEqual(loser, scissors)
        self.assertEqual(outcome_type, 'kill')
        self.assertTrue(rock.alive)
        self.assertFalse(scissors.alive)
    
    def test_resolve_paper_beats_rock(self):
        """Test resolution: Paper beats Rock."""
        paper = Paper((100, 100), None, self.config, self.rng)
        rock = Rock((110, 100), None, self.config, self.rng)
        
        pairs = [(paper, rock)]
        outcomes = self.resolver.resolve_collisions(pairs, tick=0)
        
        self.assertEqual(len(outcomes), 1)
        winner, loser, outcome_type = outcomes[0]
        
        self.assertEqual(winner, paper)
        self.assertEqual(loser, rock)
        self.assertTrue(paper.alive)
        self.assertFalse(rock.alive)
    
    def test_resolve_scissors_beats_paper(self):
        """Test resolution: Scissors beats Paper."""
        scissors = Scissors((100, 100), None, self.config, self.rng)
        paper = Paper((110, 100), None, self.config, self.rng)
        
        pairs = [(scissors, paper)]
        outcomes = self.resolver.resolve_collisions(pairs, tick=0)
        
        self.assertEqual(len(outcomes), 1)
        winner, loser, outcome_type = outcomes[0]
        
        self.assertEqual(winner, scissors)
        self.assertEqual(loser, paper)
        self.assertTrue(scissors.alive)
        self.assertFalse(paper.alive)
    
    def test_collision_cooldown(self):
        """Test collision cooldown prevents immediate re-collision."""
        self.config.collision_cooldown_frames = 10
        rock = Rock((100, 100), None, self.config, self.rng)
        scissors = Scissors((110, 100), None, self.config, self.rng)
        
        # First collision at tick 0
        agents = [rock, scissors]
        pairs = self.resolver.detect_collisions(agents, tick=0)
        self.assertEqual(len(pairs), 1)
        
        self.resolver.resolve_collisions(pairs, tick=0)
        
        # Try again at tick 5 (within cooldown) - should not detect
        scissors.alive = True  # Resurrect for test
        pairs = self.resolver.detect_collisions(agents, tick=5)
        self.assertEqual(len(pairs), 0)  # Cooldown active
        
        # Try at tick 11 (after cooldown)
        pairs = self.resolver.detect_collisions(agents, tick=11)
        self.assertEqual(len(pairs), 1)  # Should detect again
    
    def test_deterministic_ordering(self):
        """Test that collision resolution is deterministic."""
        # Create multiple agents
        agents = [
            Rock((100, 100), None, self.config, self.rng),
            Scissors((110, 100), None, self.config, self.rng),
            Paper((105, 110), None, self.config, self.rng),
        ]
        
        # Run collision detection/resolution multiple times
        results1 = []
        for agent in agents:
            agent.alive = True
        pairs = self.resolver.detect_collisions(agents, tick=0)
        outcomes = self.resolver.resolve_collisions(pairs, tick=0)
        results1 = [(o[0].id, o[1].id) for o in outcomes]
        
        # Reset
        for agent in agents:
            agent.alive = True
            agent.last_collision_tick = -10**9
        
        pairs = self.resolver.detect_collisions(agents, tick=0)
        outcomes = self.resolver.resolve_collisions(pairs, tick=0)
        results2 = [(o[0].id, o[1].id) for o in outcomes]
        
        # Should be the same
        self.assertEqual(results1, results2)


if __name__ == '__main__':
    unittest.main()

