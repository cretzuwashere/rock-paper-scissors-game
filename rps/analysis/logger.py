"""Event logging for analysis."""

from dataclasses import dataclass
from typing import List
import csv
import os
from datetime import datetime


@dataclass
class SpawnEvent:
    """Record of an agent spawn event."""
    id: int
    kind: str
    x: float
    y: float
    tick: int


@dataclass
class CollisionEvent:
    """Record of a collision event."""
    winner_id: int
    winner_kind: str
    loser_id: int
    loser_kind: str
    x: float
    y: float
    tick: int


class AnalysisLogger:
    """Logs and exports simulation events for analysis."""
    
    def __init__(self):
        """Initialize the logger."""
        self.spawn_events: List[SpawnEvent] = []
        self.collision_events: List[CollisionEvent] = []
        self.enabled = True
    
    def log_spawn(self, id: int, kind: str, x: float, y: float, tick: int):
        """Log an agent spawn event.
        
        Args:
            id: Agent ID
            kind: Agent type
            x: Spawn X position
            y: Spawn Y position
            tick: Game tick
        """
        if self.enabled:
            self.spawn_events.append(SpawnEvent(id, kind, x, y, tick))
    
    def log_collision(
        self, 
        winner_id: int, 
        winner_kind: str, 
        loser_id: int, 
        loser_kind: str, 
        x: float, 
        y: float, 
        tick: int
    ):
        """Log a collision event.
        
        Args:
            winner_id: Winner agent ID
            winner_kind: Winner type
            loser_id: Loser agent ID
            loser_kind: Loser type
            x: Collision X position
            y: Collision Y position
            tick: Game tick
        """
        if self.enabled:
            self.collision_events.append(
                CollisionEvent(winner_id, winner_kind, loser_id, loser_kind, x, y, tick)
            )
    
    def export_csv(self, directory: str = "analysis_output"):
        """Export logged events to CSV files.
        
        Args:
            directory: Output directory for CSV files
            
        Returns:
            Tuple of (spawn_file_path, collision_file_path)
        """
        # Create output directory
        os.makedirs(directory, exist_ok=True)
        
        # Generate timestamp for filenames
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Export spawn events
        spawn_file = os.path.join(directory, f"spawns_{timestamp}.csv")
        with open(spawn_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['id', 'kind', 'x', 'y', 'tick'])
            for event in self.spawn_events:
                writer.writerow([event.id, event.kind, event.x, event.y, event.tick])
        
        # Export collision events
        collision_file = os.path.join(directory, f"collisions_{timestamp}.csv")
        with open(collision_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['winner_id', 'winner_kind', 'loser_id', 'loser_kind', 'x', 'y', 'tick'])
            for event in self.collision_events:
                writer.writerow([
                    event.winner_id, event.winner_kind, 
                    event.loser_id, event.loser_kind, 
                    event.x, event.y, event.tick
                ])
        
        return spawn_file, collision_file
    
    def clear(self):
        """Clear all logged events."""
        self.spawn_events.clear()
        self.collision_events.clear()
    
    def get_stats(self) -> dict:
        """Get statistics about logged events.
        
        Returns:
            Dictionary with event counts and statistics
        """
        stats = {
            'total_spawns': len(self.spawn_events),
            'total_collisions': len(self.collision_events),
            'spawns_by_kind': {},
            'kills_by_kind': {},
            'deaths_by_kind': {}
        }
        
        # Count spawns by kind
        for event in self.spawn_events:
            stats['spawns_by_kind'][event.kind] = stats['spawns_by_kind'].get(event.kind, 0) + 1
        
        # Count kills and deaths by kind
        for event in self.collision_events:
            stats['kills_by_kind'][event.winner_kind] = stats['kills_by_kind'].get(event.winner_kind, 0) + 1
            stats['deaths_by_kind'][event.loser_kind] = stats['deaths_by_kind'].get(event.loser_kind, 0) + 1
        
        return stats

