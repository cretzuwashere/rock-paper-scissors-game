"""Sprite generation for agents."""

import pygame
import math


def create_rock_sprite(radius: int, color: tuple) -> pygame.Surface:
    """Create a rock sprite with a rough, angular appearance.
    
    Args:
        radius: Sprite radius
        color: Base color (RGB)
        
    Returns:
        Surface with rock sprite
    """
    size = radius * 2
    surface = pygame.Surface((size, size), pygame.SRCALPHA)
    
    # Draw irregular polygon for rock
    points = []
    num_points = 8
    for i in range(num_points):
        angle = (2 * math.pi * i / num_points) + 0.2
        r = radius * (0.8 + 0.2 * ((i % 3) / 3))  # Vary radius
        x = radius + r * math.cos(angle)
        y = radius + r * math.sin(angle)
        points.append((x, y))
    
    # Fill
    pygame.draw.polygon(surface, color, points)
    
    # Add some texture/shading
    for i in range(3):
        shade_color = tuple(max(0, c - 30 - i * 10) for c in color)
        x = radius + (i - 1) * radius * 0.3
        y = radius + (i - 1) * radius * 0.2
        pygame.draw.circle(surface, shade_color, (int(x), int(y)), radius // 4)
    
    # Border
    border_color = tuple(max(0, c - 40) for c in color)
    pygame.draw.polygon(surface, border_color, points, 2)
    
    return surface


def create_paper_sprite(radius: int, color: tuple) -> pygame.Surface:
    """Create a paper sprite with a rectangular, folded appearance.
    
    Args:
        radius: Sprite radius
        color: Base color (RGB)
        
    Returns:
        Surface with paper sprite
    """
    size = radius * 2
    surface = pygame.Surface((size, size), pygame.SRCALPHA)
    
    # Draw slightly rotated rectangle
    rect_width = radius * 1.5
    rect_height = radius * 1.8
    
    # Create rectangle surface
    rect_surface = pygame.Surface((int(rect_width), int(rect_height)), pygame.SRCALPHA)
    pygame.draw.rect(rect_surface, color, (0, 0, rect_width, rect_height))
    
    # Add fold line
    fold_color = tuple(max(0, c - 30) for c in color)
    pygame.draw.line(rect_surface, fold_color, 
                    (rect_width * 0.3, 0), (rect_width * 0.3, rect_height), 2)
    pygame.draw.line(rect_surface, fold_color, 
                    (rect_width * 0.6, 0), (rect_width * 0.6, rect_height), 2)
    
    # Add corner fold
    corner_points = [(rect_width - 5, 0), (rect_width, 0), (rect_width, 5)]
    corner_color = tuple(max(0, c - 50) for c in color)
    pygame.draw.polygon(rect_surface, corner_color, corner_points)
    
    # Border
    border_color = tuple(max(0, c - 40) for c in color)
    pygame.draw.rect(rect_surface, border_color, (0, 0, rect_width, rect_height), 2)
    
    # Rotate slightly
    rotated = pygame.transform.rotate(rect_surface, 15)
    
    # Blit centered
    rect = rotated.get_rect(center=(radius, radius))
    surface.blit(rotated, rect)
    
    return surface


def create_scissors_sprite(radius: int, color: tuple) -> pygame.Surface:
    """Create a scissors sprite with two blades in an X pattern.
    
    Args:
        radius: Sprite radius
        color: Base color (RGB)
        
    Returns:
        Surface with scissors sprite
    """
    size = radius * 2
    surface = pygame.Surface((size, size), pygame.SRCALPHA)
    
    # Draw two crossing blades
    blade_length = radius * 1.4
    blade_width = radius * 0.3
    
    # Blade color (slightly darker)
    blade_color = tuple(max(0, c - 20) for c in color)
    
    # Left blade (top-left to bottom-right)
    points1 = [
        (radius - blade_width, radius - blade_length),
        (radius + blade_width, radius - blade_length),
        (radius + blade_width + 2, radius + blade_length),
        (radius - blade_width + 2, radius + blade_length)
    ]
    pygame.draw.polygon(surface, blade_color, points1)
    
    # Right blade (top-right to bottom-left)
    points2 = [
        (radius + blade_length, radius - blade_width),
        (radius + blade_length, radius + blade_width),
        (radius - blade_length - 2, radius + blade_width + 2),
        (radius - blade_length - 2, radius - blade_width + 2)
    ]
    pygame.draw.polygon(surface, blade_color, points2)
    
    # Center pivot point
    pygame.draw.circle(surface, color, (radius, radius), int(radius * 0.4))
    
    # Border on blades
    border_color = tuple(max(0, c - 60) for c in color)
    pygame.draw.polygon(surface, border_color, points1, 2)
    pygame.draw.polygon(surface, border_color, points2, 2)
    
    # Border on pivot
    pygame.draw.circle(surface, border_color, (radius, radius), int(radius * 0.4), 2)
    
    return surface


def create_agent_sprites(config) -> dict:
    """Create all agent sprites based on config.
    
    Args:
        config: Game configuration
        
    Returns:
        Dictionary mapping agent kind to sprite surface
    """
    return {
        'rock': create_rock_sprite(config.agent_radius_rock, config.color_rock),
        'paper': create_paper_sprite(config.agent_radius_paper, config.color_paper),
        'scissors': create_scissors_sprite(config.agent_radius_scissors, config.color_scissors)
    }

