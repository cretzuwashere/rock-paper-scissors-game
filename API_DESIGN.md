# RPS World - External Spawn API Design

## Overview

REST API endpoint for spawning agents from external sources (Discord bot, web interface, etc.).

## API Specification

### Endpoint

```
POST /api/spawn
```

### Request Format

**Content-Type**: `application/json`

**Body**:
```json
{
  "type": "Rock" | "Paper" | "Scissors",
  "x": number,
  "y": number
}
```

### Field Validation

| Field | Type | Required | Validation |
|-------|------|----------|------------|
| `type` | string | Yes | Must be exactly "Rock", "Paper", or "Scissors" (case-sensitive) |
| `x` | number | Yes | Any number (will be adjusted if off-screen) |
| `y` | number | Yes | Any number (will be adjusted if off-screen) |

### Response Format

#### Success (200 OK)

```json
{
  "success": true,
  "agent": {
    "id": 123,
    "type": "Rock",
    "x": 150.5,
    "y": 200.3,
    "adjusted": false
  },
  "message": "Agent spawned successfully"
}
```

If coordinates were adjusted:
```json
{
  "success": true,
  "agent": {
    "id": 124,
    "type": "Paper",
    "x": 50.0,
    "y": 100.0,
    "adjusted": true,
    "original_x": -100,
    "original_y": 100
  },
  "message": "Agent spawned successfully (coordinates adjusted to be on-screen)"
}
```

#### Error Responses

**400 Bad Request** - Invalid input:
```json
{
  "success": false,
  "error": "Invalid agent type. Must be 'Rock', 'Paper', or 'Scissors'",
  "code": "INVALID_TYPE"
}
```

```json
{
  "success": false,
  "error": "Missing required field: type",
  "code": "MISSING_FIELD"
}
```

```json
{
  "success": false,
  "error": "Invalid coordinate format. x and y must be numbers",
  "code": "INVALID_COORDINATES"
}
```

**503 Service Unavailable** - Population cap reached:
```json
{
  "success": false,
  "error": "Population cap reached. Cannot spawn more agents.",
  "code": "POPULATION_CAP",
  "current_population": 500,
  "max_population": 500
}
```

**500 Internal Server Error** - Server error:
```json
{
  "success": false,
  "error": "Internal server error",
  "code": "INTERNAL_ERROR"
}
```

## Coordinate Adjustment Rules

### Off-Screen Detection

Coordinates are considered off-screen if:
- `x < 0` or `x >= screen_width`
- `y < 0` or `y >= screen_height`

### Adjustment Algorithm

```python
def adjust_coordinates(x, y, screen_width, screen_height, margin=50):
    """
    Adjust off-screen coordinates to be on-screen with margin.
    
    Args:
        x, y: Original coordinates
        screen_width, screen_height: Screen dimensions
        margin: Minimum distance from edge (default: 50 pixels)
    
    Returns:
        adjusted_x, adjusted_y, was_adjusted
    """
    adjusted = False
    
    if x < 0:
        x = margin
        adjusted = True
    elif x >= screen_width:
        x = screen_width - margin
        adjusted = True
    
    if y < 0:
        y = margin
        adjusted = True
    elif y >= screen_height:
        y = screen_height - margin
        adjusted = True
    
    return x, y, adjusted
```

## Implementation Architecture

### Components

```
┌─────────────────────────────────────────────────────┐
│                  Discord Bot                        │
│              (External Client)                      │
└────────────────────┬────────────────────────────────┘
                     │ HTTP POST
                     │ /api/spawn
                     ▼
┌─────────────────────────────────────────────────────┐
│              Flask/FastAPI Server                   │
│                 (api_server.py)                     │
│  ┌──────────────────────────────────────────────┐  │
│  │  SpawnAPI                                     │  │
│  │  - validate_request()                        │  │
│  │  - adjust_coordinates()                      │  │
│  │  - spawn_agent()                             │  │
│  └──────────────────────────────────────────────┘  │
└────────────────────┬────────────────────────────────┘
                     │ Thread-safe queue
                     ▼
┌─────────────────────────────────────────────────────┐
│              RPS World Application                  │
│                  (rps/app.py)                       │
│  ┌──────────────────────────────────────────────┐  │
│  │  SpawnQueue                                   │  │
│  │  - process_spawn_requests()                  │  │
│  │  - add_to_queue()                            │  │
│  └──────────────────────────────────────────────┘  │
│                                                     │
│  ┌──────────────────────────────────────────────┐  │
│  │  World                                        │  │
│  │  - spawn() via factory                       │  │
│  └──────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────┘
```

### Threading Model

- **API Server**: Runs in separate thread
- **Game Loop**: Runs in main thread
- **Communication**: Thread-safe queue for spawn requests
- **Processing**: Game loop processes queue each frame

### Files to Create

1. **`rps/api/spawn_api.py`** - API endpoint logic
2. **`rps/api/spawn_queue.py`** - Thread-safe spawn queue
3. **`api_server.py`** - Flask/FastAPI server
4. **`requirements_api.txt`** - API dependencies

## Usage Examples

### Python Client

```python
import requests

# Spawn a Rock at position (100, 200)
response = requests.post('http://localhost:5000/api/spawn', json={
    'type': 'Rock',
    'x': 100,
    'y': 200
})

print(response.json())
# {'success': True, 'agent': {'id': 1, 'type': 'Rock', ...}}
```

### Discord Bot (discord.py)

```python
import discord
import requests

@bot.command()
async def spawn(ctx, agent_type: str, x: int, y: int):
    """Spawn an agent in RPS World"""
    
    response = requests.post('http://localhost:5000/api/spawn', json={
        'type': agent_type.capitalize(),
        'x': x,
        'y': y
    })
    
    data = response.json()
    
    if data['success']:
        await ctx.send(f"✅ Spawned {data['agent']['type']} at ({data['agent']['x']:.0f}, {data['agent']['y']:.0f})")
    else:
        await ctx.send(f"❌ Error: {data['error']}")

# Usage: !spawn rock 100 200
```

### cURL

```bash
# Spawn Rock
curl -X POST http://localhost:5000/api/spawn \
  -H "Content-Type: application/json" \
  -d '{"type": "Rock", "x": 100, "y": 200}'

# Spawn Paper (off-screen, will be adjusted)
curl -X POST http://localhost:5000/api/spawn \
  -H "Content-Type: application/json" \
  -d '{"type": "Paper", "x": -50, "y": 300}'
```

## Security Considerations

### Rate Limiting

```python
from flask_limiter import Limiter

limiter = Limiter(
    app,
    default_limits=["100 per minute", "1000 per hour"]
)

@app.route('/api/spawn', methods=['POST'])
@limiter.limit("10 per second")
def spawn_agent():
    # ...
```

### Authentication (Optional)

```python
# API Key authentication
API_KEY = os.getenv('RPS_API_KEY')

@app.before_request
def check_api_key():
    if request.headers.get('X-API-Key') != API_KEY:
        return jsonify({'error': 'Invalid API key'}), 401
```

### Input Sanitization

- Validate type is exactly "Rock", "Paper", or "Scissors"
- Ensure x and y are numeric
- Reject extra fields
- Limit coordinate values (e.g., -10000 to 10000)

## Configuration

### Environment Variables

```bash
# .env file
RPS_API_PORT=5000
RPS_API_HOST=0.0.0.0
RPS_API_KEY=your-secret-key-here
RPS_SCREEN_WIDTH=1200
RPS_SCREEN_HEIGHT=800
RPS_MAX_POPULATION=500
```

### Config File

```python
# rps/api/config.py
class APIConfig:
    PORT = int(os.getenv('RPS_API_PORT', 5000))
    HOST = os.getenv('RPS_API_HOST', '127.0.0.1')
    DEBUG = os.getenv('RPS_API_DEBUG', 'False').lower() == 'true'
    
    # Coordinate adjustment
    MARGIN = 50  # Pixels from edge
    
    # Rate limiting
    RATE_LIMIT = "10 per second"
```

## Testing

### Unit Tests

```python
def test_valid_spawn():
    response = client.post('/api/spawn', json={
        'type': 'Rock',
        'x': 100,
        'y': 200
    })
    assert response.status_code == 200
    assert response.json['success'] == True

def test_invalid_type():
    response = client.post('/api/spawn', json={
        'type': 'Invalid',
        'x': 100,
        'y': 200
    })
    assert response.status_code == 400
    assert 'Invalid agent type' in response.json['error']

def test_coordinate_adjustment():
    response = client.post('/api/spawn', json={
        'type': 'Paper',
        'x': -100,
        'y': 200
    })
    assert response.status_code == 200
    assert response.json['agent']['adjusted'] == True
    assert response.json['agent']['x'] >= 0
```

## Deployment

### Local Development

```bash
# Terminal 1: Start API server
python api_server.py

# Terminal 2: Start game
python -m rps.app --api-enabled
```

### Production

```bash
# Using gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 api_server:app

# Using uvicorn (FastAPI)
uvicorn api_server:app --host 0.0.0.0 --port 5000 --workers 4
```

## Monitoring

### Metrics to Track

- Spawn requests per second
- Success/error rate
- Average response time
- Current population
- Queue length

### Logging

```python
import logging

logger = logging.getLogger('rps_api')

@app.route('/api/spawn', methods=['POST'])
def spawn_agent():
    logger.info(f"Spawn request: {request.json}")
    # ...
    logger.info(f"Spawn success: agent_id={agent.id}")
```

## Future Enhancements

- WebSocket support for real-time updates
- Batch spawn endpoint (multiple agents at once)
- Query endpoint to get current game state
- Delete/kill agent endpoint
- Pause/resume game endpoint
- Screenshot/recording endpoint

---

**Ready for implementation!** 🚀

