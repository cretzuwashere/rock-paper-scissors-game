"""Flask API server for external agent spawning."""

from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from rps.api.spawn_api import SpawnAPI
from rps.api.spawn_queue import SpawnQueue
from rps.core.config import Config

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for web clients

# Configuration
config = Config()
spawn_api = SpawnAPI(
    screen_width=config.screen_width,
    screen_height=config.screen_height,
    margin=50
)

# Global spawn queue (will be shared with game)
spawn_queue = None


def set_spawn_queue(queue: SpawnQueue):
    """Set the spawn queue (called by game on startup).
    
    Args:
        queue: SpawnQueue instance from the game
    """
    global spawn_queue
    spawn_queue = queue


@app.route('/api/spawn', methods=['POST'])
def spawn_agent():
    """Spawn an agent via API.
    
    Request JSON:
        {
            "type": "Rock" | "Paper" | "Scissors",
            "x": number,
            "y": number
        }
    
    Returns:
        JSON response with success/error
    """
    global spawn_queue
    
    # Check if game is running
    if spawn_queue is None:
        return jsonify({
            'success': False,
            'error': 'Game not running. Start the game with --api-enabled flag.',
            'code': 'GAME_NOT_RUNNING'
        }), 503
    
    # Get request data
    data = request.get_json()
    
    if data is None:
        return jsonify({
            'success': False,
            'error': 'Invalid JSON or Content-Type. Use application/json',
            'code': 'INVALID_JSON'
        }), 400
    
    # Validate and create spawn request
    spawn_request, error = spawn_api.validate_and_create_request(data)
    
    if error:
        return jsonify(error), 400
    
    # Check if queue is full
    if spawn_queue.is_full():
        return jsonify({
            'success': False,
            'error': 'Spawn queue is full. Try again later.',
            'code': 'QUEUE_FULL',
            'queue_size': spawn_queue.size()
        }), 503
    
    # Add to queue
    if not spawn_queue.add(spawn_request):
        return jsonify({
            'success': False,
            'error': 'Failed to add spawn request to queue',
            'code': 'QUEUE_ERROR'
        }), 500
    
    # Return success (agent will be spawned in next game frame)
    return jsonify({
        'success': True,
        'message': 'Spawn request queued successfully',
        'request': {
            'type': spawn_request.agent_type.capitalize(),
            'x': spawn_request.x,
            'y': spawn_request.y,
            'adjusted': spawn_request.adjusted
        },
        'queue_size': spawn_queue.size()
    }), 202  # 202 Accepted


@app.route('/api/status', methods=['GET'])
def get_status():
    """Get current game status.
    
    Returns:
        JSON with game status
    """
    global spawn_queue
    
    if spawn_queue is None:
        return jsonify({
            'running': False,
            'message': 'Game not running'
        })
    
    return jsonify({
        'running': True,
        'queue_size': spawn_queue.size(),
        'queue_capacity': 1000,
        'screen_width': config.screen_width,
        'screen_height': config.screen_height
    })


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint.
    
    Returns:
        JSON with health status
    """
    return jsonify({
        'status': 'healthy',
        'service': 'RPS World API'
    })


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({
        'success': False,
        'error': 'Endpoint not found',
        'code': 'NOT_FOUND'
    }), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({
        'success': False,
        'error': 'Internal server error',
        'code': 'INTERNAL_ERROR'
    }), 500


def run_server(host='127.0.0.1', port=5000, debug=False):
    """Run the Flask server.
    
    Args:
        host: Host to bind to
        port: Port to listen on
        debug: Enable debug mode
    """
    print(f"Starting RPS World API server on {host}:{port}")
    print(f"Spawn endpoint: POST http://{host}:{port}/api/spawn")
    print(f"Status endpoint: GET http://{host}:{port}/api/status")
    app.run(host=host, port=port, debug=debug, threaded=True)


if __name__ == '__main__':
    # Standalone mode (for testing)
    import argparse
    
    parser = argparse.ArgumentParser(description='RPS World API Server')
    parser.add_argument('--host', default='127.0.0.1', help='Host to bind to')
    parser.add_argument('--port', type=int, default=5000, help='Port to listen on')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode')
    
    args = parser.parse_args()
    
    # Create a dummy queue for standalone testing
    spawn_queue = SpawnQueue()
    
    run_server(host=args.host, port=args.port, debug=args.debug)

