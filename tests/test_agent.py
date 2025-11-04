"""Tests for Agent class and subclasses."""

import unittest
import random
import pygame
from rps.core.agent import Agent, Rock, Paper, Scissors
from rps.core.config import Config


class TestAgent(unittest.TestCase):
    """Test Agent base class."""
    
    @classmethod
    def setUpClass(cls):
        """Initialize pygame for tests."""
        pygame.init()
        pygame.display.set_mode((1, 1), pygame.HIDDEN)
    
    def setUp(self):
        """Set up test fixtures."""
        self.config = Config(seed=42)
        self.rng = random.Random(42)
    
    def test_rock_paper_scissors_creation(self):
        """Test creating Rock, Paper, and Scissors agents."""
        rock = Rock((100, 100), None, self.config, self.rng)
        paper = Paper((200, 200), None, self.config, self.rng)
        scissors = Scissors((300, 300), None, self.config, self.rng)
        
        self.assertEqual(rock.kind, 'rock')
        self.assertEqual(paper.kind, 'paper')
        self.assertEqual(scissors.kind, 'scissors')
        
        self.assertTrue(rock.alive)
        self.assertTrue(paper.alive)
        self.assertTrue(scissors.alive)
    
    def test_compare_rock_beats_scissors(self):
        """Test Rock beats Scissors."""
        rock = Rock((100, 100), None, self.config, self.rng)
        scissors = Scissors((200, 200), None, self.config, self.rng)
        
        self.assertEqual(rock.compare(scissors), 1)  # Rock wins
        self.assertEqual(scissors.compare(rock), -1)  # Scissors loses
    
    def test_compare_paper_beats_rock(self):
        """Test Paper beats Rock."""
        paper = Paper((100, 100), None, self.config, self.rng)
        rock = Rock((200, 200), None, self.config, self.rng)
        
        self.assertEqual(paper.compare(rock), 1)  # Paper wins
        self.assertEqual(rock.compare(paper), -1)  # Rock loses
    
    def test_compare_scissors_beats_paper(self):
        """Test Scissors beats Paper."""
        scissors = Scissors((100, 100), None, self.config, self.rng)
        paper = Paper((200, 200), None, self.config, self.rng)
        
        self.assertEqual(scissors.compare(paper), 1)  # Scissors wins
        self.assertEqual(paper.compare(scissors), -1)  # Paper loses
    
    def test_compare_tie(self):
        """Test same types result in tie."""
        rock1 = Rock((100, 100), None, self.config, self.rng)
        rock2 = Rock((200, 200), None, self.config, self.rng)
        
        self.assertEqual(rock1.compare(rock2), 0)  # Tie
        self.assertEqual(rock2.compare(rock1), 0)  # Tie
    
    def test_collision_detection_touching(self):
        """Test collision detection for touching agents."""
        rock = Rock((100, 100), None, self.config, self.rng)
        scissors = Scissors((100, 100), None, self.config, self.rng)
        # Place scissors close to rock
        scissors.pos.x = rock.pos.x + rock.radius + scissors.radius - 1
        
        self.assertTrue(rock.collides_with(scissors))
    
    def test_collision_detection_not_touching(self):
        """Test collision detection for separated agents."""
        rock = Rock((100, 100), None, self.config, self.rng)
        scissors = Scissors((300, 300), None, self.config, self.rng)
        
        self.assertFalse(rock.collides_with(scissors))
    
    def test_agent_movement_wrap(self):
        """Test agent movement with wrap boundary mode."""
        self.config.boundary_mode = "wrap"
        self.config.enable_steering = False  # Disable steering for predictable movement
        rock = Rock((10, 10), (100, 0), self.config, self.rng)
        
        # Move for 10 seconds (should wrap)
        rock.update(10.0, None)
        
        # Should have wrapped around
        self.assertTrue(0 <= rock.pos.x < self.config.screen_width)
        self.assertTrue(0 <= rock.pos.y < self.config.screen_height)
    
    def test_agent_movement_bounce(self):
        """Test agent movement with bounce boundary mode."""
        self.config.boundary_mode = "bounce"
        self.config.enable_steering = False  # Disable steering for predictable movement
        rock = Rock((10, 10), (-100, 0), self.config, self.rng)
        
        # Move towards left boundary
        rock.update(0.5, None)
        
        # Should have bounced - velocity should be positive now
        self.assertGreater(rock.vel.x, 0)
    
    def test_kill_agent(self):
        """Test killing an agent."""
        rock = Rock((100, 100), None, self.config, self.rng)
        self.assertTrue(rock.alive)
        
        rock.kill()
        self.assertFalse(rock.alive)
    
    def test_agent_unique_ids(self):
        """Test that agents get unique IDs."""
        rock1 = Rock((100, 100), None, self.config, self.rng)
        rock2 = Rock((200, 200), None, self.config, self.rng)
        paper = Paper((300, 300), None, self.config, self.rng)
        
        ids = {rock1.id, rock2.id, paper.id}
        self.assertEqual(len(ids), 3)  # All unique


if __name__ == '__main__':
    unittest.main()

