"""Configuration and constants for the RPS world."""

from dataclasses import dataclass
from typing import Tuple
import random


@dataclass
class Config:
    """Configuration for the RPS simulation."""
    
    # Display settings
    screen_width: int = 1200
    screen_height: int = 800
    fps: int = 60
    background_color: Tuple[int, int, int] = (20, 20, 30)
    
    # Agent settings
    agent_radius_rock: int = 15
    agent_radius_paper: int = 12
    agent_radius_scissors: int = 13
    
    agent_speed_rock: Tuple[float, float] = (50, 80)  # min, max pixels/sec
    agent_speed_paper: Tuple[float, float] = (80, 120)
    agent_speed_scissors: Tuple[float, float] = (60, 100)
    
    # Colors (RGB)
    color_rock: Tuple[int, int, int] = (120, 120, 120)  # Gray
    color_paper: Tuple[int, int, int] = (255, 255, 100)  # Yellow
    color_scissors: Tuple[int, int, int] = (255, 100, 100)  # Red
    
    # Collision settings
    collision_cooldown_frames: int = 8
    bounce_on_tie: bool = True
    boundary_mode: str = "bounce"  # "wrap" or "bounce" - changed to bounce
    
    # Steering behavior
    enable_steering: bool = True
    agent_detection_range: float = 200.0
    
    # Display options
    show_names: bool = False
    language: str = 'en'  # 'en' or 'ro'  # How far agents can detect others
    
    # Spawning
    spawn_batch_size: int = 10
    max_population: int = 500
    
    # Analysis
    log_events: bool = True
    
    # Random seed
    seed: int = None
    
    def __post_init__(self):
        """Initialize random seed if not provided."""
        if self.seed is None:
            self.seed = random.randint(0, 999999)


# Game rules
BEATS = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper'
}

KINDS = ['rock', 'paper', 'scissors']

