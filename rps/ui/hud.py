"""HUD overlay for displaying game information."""

import pygame
from typing import Dict


class HUD:
    """Heads-up display for game information."""
    
    def __init__(self, config):
        """Initialize the HUD.
        
        Args:
            config: Game configuration
        """
        self.config = config
        self.font_large = None
        self.font_small = None
        self.font_tiny = None
        
    def initialize_fonts(self):
        """Initialize pygame fonts (must be called after pygame.init())."""
        self.font_large = pygame.font.Font(None, 36)
        self.font_small = pygame.font.Font(None, 24)
        self.font_tiny = pygame.font.Font(None, 18)
    
    def draw(
        self, 
        surface: pygame.Surface, 
        counts: Dict[str, int],
        total_interactions: int,
        fps: float,
        seed: int,
        paused: bool,
        debug_mode: bool,
        tick: int
    ):
        """Draw the HUD overlay.
        
        Args:
            surface: Surface to draw on
            counts: Agent counts by kind
            total_interactions: Total collision count
            fps: Current FPS
            seed: Random seed
            paused: Whether game is paused
            debug_mode: Whether debug mode is enabled
            tick: Current game tick
        """
        if self.font_large is None:
            self.initialize_fonts()
        
        x, y = 10, 10
        line_height = 30
        
        # Draw semi-transparent background
        info_height = 240
        bg_surface = pygame.Surface((320, info_height), pygame.SRCALPHA)
        bg_surface.fill((0, 0, 0, 180))
        surface.blit(bg_surface, (5, 5))
        
        # Title
        text = self.font_large.render("RPS World", True, (255, 255, 255))
        surface.blit(text, (x, y))
        y += 40
        
        # Agent counts with colors
        rock_color = self.config.color_rock
        paper_color = self.config.color_paper
        scissors_color = self.config.color_scissors
        
        text = self.font_small.render(f"Rock:", True, (200, 200, 200))
        surface.blit(text, (x, y))
        count_text = self.font_small.render(f"{counts.get('rock', 0)}", True, rock_color)
        surface.blit(count_text, (x + 80, y))
        y += line_height
        
        text = self.font_small.render(f"Paper:", True, (200, 200, 200))
        surface.blit(text, (x, y))
        count_text = self.font_small.render(f"{counts.get('paper', 0)}", True, paper_color)
        surface.blit(count_text, (x + 80, y))
        y += line_height
        
        text = self.font_small.render(f"Scissors:", True, (200, 200, 200))
        surface.blit(text, (x, y))
        count_text = self.font_small.render(f"{counts.get('scissors', 0)}", True, scissors_color)
        surface.blit(count_text, (x + 80, y))
        y += line_height
        
        # Total
        total = sum(counts.values())
        text = self.font_small.render(f"Total: {total}", True, (255, 255, 255))
        surface.blit(text, (x, y))
        y += line_height
        
        # Stats
        text = self.font_small.render(f"Collisions: {total_interactions}", True, (200, 200, 200))
        surface.blit(text, (x, y))
        y += line_height
        
        text = self.font_small.render(f"FPS: {fps:.1f}", True, (200, 200, 200))
        surface.blit(text, (x, y))
        y += line_height
        
        text = self.font_small.render(f"Seed: {seed}", True, (200, 200, 200))
        surface.blit(text, (x, y))
        y += line_height
        
        # Status indicators
        if paused:
            pause_text = self.font_large.render("PAUSED", True, (255, 255, 0))
            text_rect = pause_text.get_rect(center=(surface.get_width() // 2, 50))
            surface.blit(pause_text, text_rect)
        
        if debug_mode:
            debug_text = self.font_small.render("DEBUG", True, (0, 255, 0))
            surface.blit(debug_text, (surface.get_width() - 80, 10))
        
        # Show steering status
        steering_status = "HUNT ON" if self.config.enable_steering else "HUNT OFF"
        steering_color = (0, 255, 0) if self.config.enable_steering else (255, 100, 100)
        steering_text = self.font_small.render(steering_status, True, steering_color)
        surface.blit(steering_text, (surface.get_width() - 100, 40))
        
        # Show names status
        names_status = "NAMES ON" if self.config.show_names else "NAMES OFF"
        names_color = (0, 255, 0) if self.config.show_names else (255, 100, 100)
        names_text = self.font_small.render(names_status, True, names_color)
        surface.blit(names_text, (surface.get_width() - 110, 70))
        
        # Controls help (bottom)
        self._draw_controls(surface)
    
    def _draw_controls(self, surface: pygame.Surface):
        """Draw controls help at the bottom of the screen.
        
        Args:
            surface: Surface to draw on
        """
        help_lines = [
            "Controls: R/P/S=Spawn at mouse | 1/2/3=Batch spawn | B=Random Spawn | Space=Pause",
            "H=Toggle Hunt | N=Toggle Names | C=Clear | D=Debug | F9=Export CSV | F5=New seed+spawn | ESC=Quit"
        ]
        
        y = surface.get_height() - 60
        for line in help_lines:
            text = self.font_tiny.render(line, True, (180, 180, 180))
            surface.blit(text, (10, y))
            y += 20
    
    def draw_message(self, surface: pygame.Surface, message: str, duration: float = 2.0):
        """Draw a temporary message on screen.
        
        Args:
            surface: Surface to draw on
            message: Message text
            duration: How long to show (unused here, managed by caller)
        """
        if self.font_small is None:
            self.initialize_fonts()
        
        text = self.font_small.render(message, True, (0, 255, 0))
        bg_width = text.get_width() + 20
        bg_height = text.get_height() + 10
        
        bg_surface = pygame.Surface((bg_width, bg_height), pygame.SRCALPHA)
        bg_surface.fill((0, 0, 0, 200))
        
        x = (surface.get_width() - bg_width) // 2
        y = surface.get_height() - 120
        
        surface.blit(bg_surface, (x, y))
        surface.blit(text, (x + 10, y + 5))

