# Hunting Behavior System

## Overview

The RPS World now features intelligent **hunting behavior** where agents actively seek their prey and flee from their predators, creating dynamic and engaging gameplay.

## How It Works

### Steering Behavior

Each agent uses **steering forces** to navigate the world:

- **Seek**: Agents steer toward their prey (agents they can beat)
- **Flee**: Agents steer away from predators (agents that can beat them)

### Detection Range

Agents can detect other agents within a configurable **detection range** (default: 200 pixels). This creates interesting local interactions where agents only respond to nearby threats and opportunities.

### Priority System

When an agent detects both prey and predators:
- **Fleeing has higher priority** (weight: 1.3)
- **Seeking has lower priority** (weight: 0.7)

This ensures agents prioritize survival over hunting.

### Target Selection

- Agents target the **nearest prey** within detection range
- Multiple predators are weighted by proximity (closer = stronger influence)

## Game Rules with Hunting

- **Rock** hunts **Scissors**, flees from **Paper**
- **Paper** hunts **Rock**, flees from **Scissors**
- **Scissors** hunt **Paper**, flee from **Rock**

## Configuration

### Enable/Disable Hunting

Press **`H`** during gameplay to toggle hunting behavior on/off.

- **ON** (default): Agents actively hunt and flee
- **OFF**: Agents move randomly (classic behavior)

### Settings in Config

```python
# Steering behavior
enable_steering: bool = True
agent_detection_range: float = 200.0  # Detection radius in pixels
```

### Speed Limits

Each agent has:
- **max_speed**: Maximum velocity
- **max_force**: Maximum steering force (10% of max_speed)

This creates smooth, natural-looking movement.

## Visual Indicators

### HUD Display

Top-right corner shows:
- **"HUNT ON"** (green) - Hunting enabled
- **"HUNT OFF"** (red) - Hunting disabled

### Debug Mode

Press **`D`** to see:
- White circles: Detection/collision radii
- Green arrows: Velocity vectors showing movement direction

## Factory Pattern

All agents are now created through the **AgentFactory**:

```python
factory = AgentFactory(config, rng)

# Create single agent
rock = factory.create_agent('rock', (100, 100))

# Create random agent
paper = factory.create_random_agent('paper')

# Create batch
scissors_batch = factory.create_batch('scissors', 10)

# Create balanced population
population = factory.create_balanced_population(5)
```

### Benefits

- **Encapsulation**: All creation logic in one place
- **Consistency**: Guaranteed proper initialization
- **Extensibility**: Easy to add new agent types
- **Testing**: Simplified mocking and testing

## Gameplay Impact

### With Hunting ON

- **More dynamic**: Agents chase and flee, creating swirling patterns
- **Faster resolution**: Predators actively hunt down prey
- **Emergent behavior**: Clustering, chasing, fleeing patterns
- **Strategic positioning**: Spawn location matters more

### With Hunting OFF

- **Classic behavior**: Random movement, chance encounters
- **Slower resolution**: Collisions happen by chance
- **Uniform distribution**: Agents spread evenly
- **Pure probability**: Outcome based on initial numbers

## Technical Details

### Steering Algorithm

```python
def _apply_steering(self, nearby_agents, dt):
    # Find prey and predators
    prey = [agent for agent in nearby_agents if self.beats(agent)]
    predators = [agent for agent in nearby_agents if agent.beats(self)]
    
    # Calculate forces
    seek_force = self._seek(nearest_prey.pos) if prey else Vector2(0, 0)
    flee_force = sum(self._flee(pred.pos) * weight for pred in predators)
    
    # Combine with priority
    steering = seek_force * 0.7 + flee_force * 1.3
    
    # Apply with force limit
    if steering.length() > max_force:
        steering.scale_to_length(max_force)
    
    velocity += steering
```

### Performance

- **O(n²) worst case**: Each agent checks all others
- **Early filtering**: Detection range reduces actual comparisons
- **Optimized**: Only living agents within range are processed

For large populations (300+), consider:
- Spatial hash grid (future optimization)
- Reduced detection range
- Lower update frequency

## Experiments to Try

### 1. Predator-Prey Dynamics
```
1. Press H to enable hunting
2. Spawn 5 Scissors (press 3)
3. Spawn 20 Papers (press 2 twice)
4. Watch Scissors actively hunt down Papers
```

### 2. Escape Behavior
```
1. Spawn 1 Rock at center (R + click center)
2. Spawn 10 Scissors around it (S + click around)
3. Watch Scissors flee from Rock
```

### 3. Chase Patterns
```
1. Enable debug mode (D)
2. Spawn a few of each type
3. Watch velocity vectors show pursuit
```

### 4. Compare Behaviors
```
1. Spawn balanced population (1, 2, 3)
2. Observe with hunting ON
3. Press H to disable hunting
4. Notice the difference in patterns
```

## Code Examples

### Creating Agents via Factory

```python
from rps.core.factory import AgentFactory
from rps.core.config import Config
import random

config = Config(seed=42)
rng = random.Random(42)
factory = AgentFactory(config, rng)

# Single agent at specific position
rock = factory.create_agent('rock', (100, 100))

# Random position
paper = factory.create_random_agent('paper')

# Batch creation
scissors = factory.create_batch('scissors', 5)

# Balanced population
population = factory.create_balanced_population(10)
# Returns: {'rock': [10 rocks], 'paper': [10 papers], 'scissors': [10 scissors]}
```

### Custom Agent Types

```python
from rps.core.agent import Agent

class Lizard(Agent):
    """Custom agent type."""
    def __init__(self, pos, vel, config, rng):
        super().__init__(
            kind='lizard',
            pos=pos,
            vel=vel,
            radius=14,
            color=(100, 200, 100),
            config=config,
            rng=rng
        )

# Register with factory
factory.register_agent_type('lizard', Lizard)

# Create lizard
lizard = factory.create_agent('lizard', (200, 200))
```

## Performance Tips

### For Smooth 60 FPS

- **< 100 agents**: Perfect performance
- **100-200 agents**: Good performance
- **200-300 agents**: Acceptable (45-60 FPS)
- **300+ agents**: May drop below 60 FPS

### Optimization Options

1. **Reduce detection range**:
   ```python
   config.agent_detection_range = 150.0  # Default: 200.0
   ```

2. **Disable hunting for some agents**:
   ```python
   config.enable_steering = False
   ```

3. **Lower spawn batch size**:
   ```python
   config.spawn_batch_size = 5  # Default: 10
   ```

## Future Enhancements

Potential improvements:
- **Spatial hash grid**: O(n) collision detection
- **Flocking behavior**: Agents of same type group together
- **Territory**: Agents defend areas
- **Energy system**: Hunting costs energy
- **Evolution**: Successful hunters reproduce
- **Team behavior**: Coordinated hunting

---

**Try it now!** Press `1`, `2`, `3` to spawn agents and watch them hunt! 🎮🪨📄✂️

