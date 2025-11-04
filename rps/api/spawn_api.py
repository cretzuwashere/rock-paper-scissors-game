"""Spawn API logic and validation."""

from typing import Tuple, Dict, Any, Optional
from .spawn_queue import SpawnRequest


class SpawnAPI:
    """Handles spawn API logic and validation."""
    
    # Valid agent types (case-sensitive)
    VALID_TYPES = {'Rock', 'Paper', 'Scissors'}
    
    # Type mapping to internal format
    TYPE_MAPPING = {
        'Rock': 'rock',
        'Paper': 'paper',
        'Scissors': 'scissors'
    }
    
    def __init__(self, screen_width: int, screen_height: int, margin: int = 50):
        """Initialize the spawn API.
        
        Args:
            screen_width: Game screen width
            screen_height: Game screen height
            margin: Minimum distance from screen edge (pixels)
        """
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.margin = margin
    
    def validate_and_create_request(
        self, 
        data: Dict[str, Any]
    ) -> Tuple[Optional[SpawnRequest], Optional[Dict[str, Any]]]:
        """Validate request data and create spawn request.
        
        Args:
            data: Request data dictionary
            
        Returns:
            Tuple of (SpawnRequest, error_dict)
            If valid: (SpawnRequest, None)
            If invalid: (None, error_dict)
        """
        # Check required fields
        if 'type' not in data:
            return None, {
                'success': False,
                'error': 'Missing required field: type',
                'code': 'MISSING_FIELD'
            }
        
        if 'x' not in data:
            return None, {
                'success': False,
                'error': 'Missing required field: x',
                'code': 'MISSING_FIELD'
            }
        
        if 'y' not in data:
            return None, {
                'success': False,
                'error': 'Missing required field: y',
                'code': 'MISSING_FIELD'
            }
        
        # Validate agent type
        agent_type = data['type']
        if agent_type not in self.VALID_TYPES:
            return None, {
                'success': False,
                'error': f"Invalid agent type. Must be 'Rock', 'Paper', or 'Scissors' (case-sensitive)",
                'code': 'INVALID_TYPE',
                'received': agent_type
            }
        
        # Validate coordinates are numbers
        try:
            x = float(data['x'])
            y = float(data['y'])
        except (ValueError, TypeError):
            return None, {
                'success': False,
                'error': 'Invalid coordinate format. x and y must be numbers',
                'code': 'INVALID_COORDINATES'
            }
        
        # Adjust coordinates if off-screen
        adjusted_x, adjusted_y, was_adjusted = self.adjust_coordinates(x, y)
        
        # Create spawn request
        request = SpawnRequest(
            agent_type=self.TYPE_MAPPING[agent_type],
            x=adjusted_x,
            y=adjusted_y,
            original_x=x if was_adjusted else None,
            original_y=y if was_adjusted else None,
            adjusted=was_adjusted
        )
        
        return request, None
    
    def adjust_coordinates(self, x: float, y: float) -> Tuple[float, float, bool]:
        """Adjust off-screen coordinates to be on-screen.
        
        Args:
            x: Original x coordinate
            y: Original y coordinate
            
        Returns:
            Tuple of (adjusted_x, adjusted_y, was_adjusted)
        """
        adjusted = False
        
        # Adjust X coordinate
        if x < 0:
            x = self.margin
            adjusted = True
        elif x >= self.screen_width:
            x = self.screen_width - self.margin
            adjusted = True
        
        # Adjust Y coordinate
        if y < 0:
            y = self.margin
            adjusted = True
        elif y >= self.screen_height:
            y = self.screen_height - self.margin
            adjusted = True
        
        return x, y, adjusted
    
    def create_success_response(
        self, 
        agent_id: int, 
        request: SpawnRequest
    ) -> Dict[str, Any]:
        """Create success response dictionary.
        
        Args:
            agent_id: ID of spawned agent
            request: Original spawn request
            
        Returns:
            Success response dictionary
        """
        response = {
            'success': True,
            'agent': {
                'id': agent_id,
                'type': request.agent_type.capitalize(),
                'x': request.x,
                'y': request.y,
                'adjusted': request.adjusted
            }
        }
        
        if request.adjusted:
            response['agent']['original_x'] = request.original_x
            response['agent']['original_y'] = request.original_y
            response['message'] = 'Agent spawned successfully (coordinates adjusted to be on-screen)'
        else:
            response['message'] = 'Agent spawned successfully'
        
        return response
    
    def create_population_cap_error(
        self, 
        current_pop: int, 
        max_pop: int
    ) -> Dict[str, Any]:
        """Create population cap error response.
        
        Args:
            current_pop: Current population
            max_pop: Maximum population
            
        Returns:
            Error response dictionary
        """
        return {
            'success': False,
            'error': 'Population cap reached. Cannot spawn more agents.',
            'code': 'POPULATION_CAP',
            'current_population': current_pop,
            'max_population': max_pop
        }

