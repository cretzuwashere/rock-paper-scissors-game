"""Victory screen with scoreboard."""

import pygame
from typing import List, Tuple


class VictoryScreen:
    """Displays victory message and scoreboard."""
    
    def __init__(self, language):
        """Initialize the victory screen.
        
        Args:
            language: Language manager
        """
        self.language = language
        self.font_title = None
        self.font_subtitle = None
        self.font_scoreboard = None
    
    def initialize_fonts(self):
        """Initialize pygame fonts (must be called after pygame.init())."""
        self.font_title = pygame.font.Font(None, 72)
        self.font_subtitle = pygame.font.Font(None, 36)
        self.font_scoreboard = pygame.font.Font(None, 28)
    
    def draw(
        self, 
        surface: pygame.Surface, 
        winner_kind: str,
        scoreboard: List[Tuple[str, int]]
    ):
        """Draw the victory screen.
        
        Args:
            surface: Surface to draw on
            winner_kind: Winning faction ('rock', 'paper', or 'scissors')
            scoreboard: List of (name, kills) tuples
        """
        if self.font_title is None:
            self.initialize_fonts()
        
        # Semi-transparent overlay
        overlay = pygame.Surface((surface.get_width(), surface.get_height()), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 200))
        surface.blit(overlay, (0, 0))
        
        # Winner announcement
        winner_text = f"{self.language.get(winner_kind + 's').upper()} {self.language.get('win').upper()}"
        title = self.font_title.render(winner_text, True, (255, 215, 0))  # Gold
        title_rect = title.get_rect(center=(surface.get_width() // 2, 100))
        surface.blit(title, title_rect)
        
        # Subtitle
        subtitle = self.font_subtitle.render(self.language.get('scoreboard'), True, (255, 255, 255))
        subtitle_rect = subtitle.get_rect(center=(surface.get_width() // 2, 180))
        surface.blit(subtitle, subtitle_rect)
        
        # Scoreboard
        y = 240
        max_display = 20  # Show top 20
        
        for i, (name, kills) in enumerate(scoreboard[:max_display]):
            # Rank
            rank_text = f"#{i+1}"
            rank_color = self._get_rank_color(i)
            rank_surface = self.font_scoreboard.render(rank_text, True, rank_color)
            
            # Name
            name_surface = self.font_scoreboard.render(name, True, (255, 255, 255))
            
            # Kills
            kill_word = self.language.get('kills') if kills != 1 else self.language.get('kill')
            kills_text = f"{kills} {kill_word}"
            kills_color = (200, 200, 200) if kills > 0 else (100, 100, 100)
            kills_surface = self.font_scoreboard.render(kills_text, True, kills_color)
            
            # Draw
            x_start = surface.get_width() // 2 - 250
            surface.blit(rank_surface, (x_start, y))
            surface.blit(name_surface, (x_start + 60, y))
            surface.blit(kills_surface, (x_start + 350, y))
            
            y += 30
        
        # Show total if more than max_display
        if len(scoreboard) > max_display:
            more_text = f"{self.language.get('and_more')} {len(scoreboard) - max_display} {self.language.get('more')}"
            more_surface = self.font_scoreboard.render(more_text, True, (150, 150, 150))
            more_rect = more_surface.get_rect(center=(surface.get_width() // 2, y + 10))
            surface.blit(more_surface, more_rect)
        
        # Show total count
        total_text = f"{self.language.get('total_count')}: {len(scoreboard)} {self.language.get(winner_kind + 's')}"
        total_surface = self.font_scoreboard.render(total_text, True, (180, 180, 180))
        total_rect = total_surface.get_rect(center=(surface.get_width() // 2, y + 40))
        surface.blit(total_surface, total_rect)
        
        # Instructions
        instructions = self.font_scoreboard.render(self.language.get('press_c'), True, (255, 255, 100))
        inst_rect = instructions.get_rect(center=(surface.get_width() // 2, surface.get_height() - 50))
        surface.blit(instructions, inst_rect)
    
    def _get_rank_color(self, rank: int) -> Tuple[int, int, int]:
        """Get color for rank.
        
        Args:
            rank: 0-based rank
            
        Returns:
            RGB color tuple
        """
        if rank == 0:
            return (255, 215, 0)  # Gold
        elif rank == 1:
            return (192, 192, 192)  # Silver
        elif rank == 2:
            return (205, 127, 50)  # Bronze
        else:
            return (255, 255, 255)  # White

