"""Thread-safe spawn queue for communication between API and game loop."""

import queue
from dataclasses import dataclass
from typing import Optional, Tuple


@dataclass
class SpawnRequest:
    """Represents a spawn request from the API."""
    agent_type: str  # 'rock', 'paper', or 'scissors'
    x: float
    y: float
    original_x: Optional[float] = None
    original_y: Optional[float] = None
    adjusted: bool = False


class SpawnQueue:
    """Thread-safe queue for spawn requests."""
    
    def __init__(self, maxsize: int = 1000):
        """Initialize the spawn queue.
        
        Args:
            maxsize: Maximum number of pending spawn requests
        """
        self._queue = queue.Queue(maxsize=maxsize)
    
    def add(self, spawn_request: SpawnRequest) -> bool:
        """Add a spawn request to the queue.
        
        Args:
            spawn_request: The spawn request to add
            
        Returns:
            True if added successfully, False if queue is full
        """
        try:
            self._queue.put_nowait(spawn_request)
            return True
        except queue.Full:
            return False
    
    def get_all(self) -> list:
        """Get all pending spawn requests (non-blocking).
        
        Returns:
            List of spawn requests
        """
        requests = []
        while not self._queue.empty():
            try:
                requests.append(self._queue.get_nowait())
            except queue.Empty:
                break
        return requests
    
    def size(self) -> int:
        """Get current queue size.
        
        Returns:
            Number of pending requests
        """
        return self._queue.qsize()
    
    def is_full(self) -> bool:
        """Check if queue is full.
        
        Returns:
            True if queue is full
        """
        return self._queue.full()
    
    def clear(self):
        """Clear all pending requests."""
        while not self._queue.empty():
            try:
                self._queue.get_nowait()
            except queue.Empty:
                break

