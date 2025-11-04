# Architecture Documentation

## System Overview

```
┌─────────────────────────────────────────────────────────────┐
│                         RPS World                            │
│                     (Python + Pygame)                        │
└─────────────────────────────────────────────────────────────┘

                    ┌──────────────┐
                    │   app.py     │
                    │   RPSApp     │
                    └──────┬───────┘
                           │
           ┌───────────────┼───────────────┐
           │               │               │
           ▼               ▼               ▼
    ┌──────────┐    ┌──────────┐   ┌──────────┐
    │  World   │    │   HUD    │   │  Logger  │
    │  (core)  │    │  (ui)    │   │(analysis)│
    └────┬─────┘    └──────────┘   └──────────┘
         │
         ├──────┬──────────┬─────────────┐
         │      │          │             │
         ▼      ▼          ▼             ▼
    ┌────────┐ ┌────────┐ ┌──────────┐ ┌────────┐
    │ Agent  │ │Collision│ │ Config  │ │Sprites │
    │ System │ │Resolver │ │         │ │(assets)│
    └────────┘ └────────┘ └──────────┘ └────────┘
```

## Module Breakdown

### 1. Application Layer (`app.py`)

**RPSApp Class**
- Responsibilities:
  - Initialize Pygame
  - Coordinate all subsystems
  - Main game loop
  - Event handling (keyboard, mouse)
  - Command-line interface

```python
RPSApp
├── __init__(config)
├── handle_events()
├── update(dt)
├── draw()
└── run()  # Main loop
```

### 2. Core Layer (`rps/core/`)

#### Agent System (`agent.py`)

**Agent Base Class**
```
Agent
├── Properties
│   ├── id, kind
│   ├── pos, vel (Vector2)
│   ├── radius, color
│   ├── alive status
│   └── collision cooldown
│
├── Movement
│   ├── update(dt)
│   ├── _wrap_boundaries()
│   └── _bounce_boundaries()
│
├── Collision
│   ├── collides_with(other)
│   ├── compare(other)  # RPS logic
│   └── soft_bounce(other)
│
└── Rendering
    ├── _create_sprite()
    └── draw(surface)
```

**Specialized Classes**
```
Rock(Agent)      → kind='rock', beats scissors
Paper(Agent)     → kind='paper', beats rock
Scissors(Agent)  → kind='scissors', beats paper
```

#### World Orchestration (`world.py`)

**World Class**
```
World
├── State Management
│   ├── agents: List[Agent]
│   ├── by_kind: Dict[str, List[Agent]]
│   ├── tick counter
│   └── pause/debug flags
│
├── Spawning
│   ├── spawn(kind, pos, vel)
│   ├── spawn_random(kind, count)
│   └── spawn_batch()
│
├── Simulation
│   ├── update(dt)
│   ├── resolve_collisions()
│   └── remove_dead()
│
├── Utilities
│   ├── clear()
│   ├── reset(seed)
│   ├── get_counts()
│   └── draw(surface)
│
└── Integrations
    ├── collision_resolver
    └── logger
```

#### Collision System (`collision.py`)

**CollisionResolver Class**
```
CollisionResolver
├── detect_collisions(agents, tick)
│   ├── O(n²) pair checking
│   ├── Cooldown filtering
│   └── Returns collision pairs
│
└── resolve_collisions(pairs, tick, logger)
    ├── Deterministic ordering
    ├── RPS comparison
    ├── Winner/loser determination
    ├── Logging integration
    └── Tie handling (bounce)
```

#### Configuration (`config.py`)

**Config Dataclass**
```
Config
├── Display
│   ├── screen_width, screen_height
│   ├── fps
│   └── background_color
│
├── Agents
│   ├── radius (per type)
│   ├── speed ranges (per type)
│   └── colors (per type)
│
├── Simulation
│   ├── collision_cooldown_frames
│   ├── bounce_on_tie
│   ├── boundary_mode
│   └── max_population
│
└── Other
    ├── seed
    └── log_events flag
```

**Game Rules**
```python
BEATS = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper'
}
```

### 3. UI Layer (`rps/ui/`)

#### HUD (`hud.py`)

**HUD Class**
```
HUD
├── Fonts
│   ├── font_large (36pt)
│   ├── font_small (24pt)
│   └── font_tiny (18pt)
│
├── draw(surface, ...)
│   ├── Background overlay
│   ├── Title
│   ├── Agent counts (color-coded)
│   ├── Statistics (collisions, FPS)
│   ├── Seed display
│   ├── Status indicators
│   └── Control hints
│
└── draw_message(surface, message)
    └── Temporary message display
```

### 4. Analysis Layer (`rps/analysis/`)

#### Logger (`logger.py`)

**Event Types**
```
SpawnEvent
├── id, kind
├── x, y
└── tick

CollisionEvent
├── winner_id, winner_kind
├── loser_id, loser_kind
├── x, y
└── tick
```

**AnalysisLogger Class**
```
AnalysisLogger
├── Storage
│   ├── spawn_events: List[SpawnEvent]
│   └── collision_events: List[CollisionEvent]
│
├── Logging
│   ├── log_spawn(...)
│   └── log_collision(...)
│
├── Export
│   ├── export_csv(directory)
│   └── Creates timestamped CSV files
│
└── Utilities
    ├── clear()
    └── get_stats()
```

### 5. Assets Layer (`rps/assets/`)

#### Sprites (`sprites.py`)

**Sprite Generation**
```
create_rock_sprite()
├── Irregular polygon (8 vertices)
├── Shading circles
└── Border

create_paper_sprite()
├── Rotated rectangle
├── Fold lines
├── Corner fold detail
└── Border

create_scissors_sprite()
├── Two crossing blades
├── Center pivot
└── Borders
```

## Data Flow

### Initialization Flow
```
1. Parse CLI args
2. Create Config
3. Initialize Pygame
4. Create World (with Config, Logger)
5. Create HUD
6. Enter game loop
```

### Game Loop Flow
```
┌─────────────────────────────────────────┐
│           Main Game Loop                │
└─────────────────────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────┐
│  1. Handle Events                       │
│     - Keyboard input                    │
│     - Mouse input                       │
│     - Window events                     │
└──────────────┬──────────────────────────┘
               ▼
┌─────────────────────────────────────────┐
│  2. Update (dt)                         │
│     ┌───────────────────────────┐       │
│     │ For each agent:           │       │
│     │   - Update position       │       │
│     │   - Handle boundaries     │       │
│     └───────────┬───────────────┘       │
│                 ▼                       │
│     ┌───────────────────────────┐       │
│     │ Collision Detection       │       │
│     │   - Find pairs            │       │
│     │   - Check cooldowns       │       │
│     └───────────┬───────────────┘       │
│                 ▼                       │
│     ┌───────────────────────────┐       │
│     │ Collision Resolution      │       │
│     │   - Compare agents        │       │
│     │   - Determine winners     │       │
│     │   - Log events            │       │
│     └───────────┬───────────────┘       │
│                 ▼                       │
│     ┌───────────────────────────┐       │
│     │ Remove Dead Agents        │       │
│     └───────────────────────────┘       │
└──────────────┬──────────────────────────┘
               ▼
┌─────────────────────────────────────────┐
│  3. Draw                                │
│     - Clear screen                      │
│     - Draw all agents                   │
│     - Draw HUD                          │
│     - Draw messages                     │
│     - Flip display                      │
└──────────────┬──────────────────────────┘
               ▼
┌─────────────────────────────────────────┐
│  4. Tick clock (maintain FPS)           │
└──────────────┬──────────────────────────┘
               │
               └──────► (repeat)
```

### Collision Resolution Detail
```
Collision Detected
      │
      ▼
┌─────────────────┐
│  Agent A vs B   │
└────────┬────────┘
         │
         ▼
┌─────────────────────────┐
│ Compare using BEATS map │
└────────┬────────────────┘
         │
    ┌────┴────┐
    ▼         ▼
┌───────┐  ┌──────────┐
│ A wins│  │ B wins   │
└───┬───┘  └────┬─────┘
    │           │
    ▼           ▼
┌────────┐  ┌────────┐
│Kill B  │  │Kill A  │
└───┬────┘  └────┬───┘
    │            │
    └────┬───────┘
         ▼
┌─────────────────┐
│ Log collision   │
└─────────────────┘
```

### Spawn Flow
```
User Input (R/P/S or 1/2/3)
      │
      ▼
┌──────────────────────┐
│ World.spawn() or     │
│ World.spawn_random() │
└──────┬───────────────┘
       │
       ▼
┌──────────────────────┐
│ Check population cap │
└──────┬───────────────┘
       │ (if OK)
       ▼
┌──────────────────────┐
│ Create Agent object  │
│ (Rock/Paper/Scissors)│
└──────┬───────────────┘
       │
       ▼
┌──────────────────────┐
│ Add to World lists   │
│ - agents[]           │
│ - by_kind[kind][]    │
└──────┬───────────────┘
       │
       ▼
┌──────────────────────┐
│ Log spawn event      │
└──────────────────────┘
```

## Class Relationships

```
┌──────────────────────────────────────────┐
│              RPSApp                      │
│  - screen: Surface                       │
│  - clock: Clock                          │
│  - config: Config                        │
│  - world: World ────────────────┐        │
│  - hud: HUD                     │        │
│  - logger: AnalysisLogger       │        │
└─────────────────────────────────┼────────┘
                                  │
                ┌─────────────────┘
                │
┌───────────────▼──────────────────────────┐
│              World                       │
│  - agents: List[Agent]                   │
│  - by_kind: Dict[str, List[Agent]]       │
│  - collision_resolver: CollisionResolver │
│  - config: Config                        │
│  - logger: AnalysisLogger ───────┐       │
│  - rng: Random                   │       │
└───────┬──────────────────────────┼───────┘
        │                          │
        │ creates/manages          │ observes
        │                          │
┌───────▼─────────────┐    ┌───────▼─────────────┐
│      Agent          │    │  AnalysisLogger     │
│  - id: int          │    │  - spawn_events     │
│  - kind: str        │    │  - collision_events │
│  - pos: Vector2     │    │  + log_spawn()      │
│  - vel: Vector2     │    │  + log_collision()  │
│  - radius: int      │    │  + export_csv()     │
│  + update(dt)       │    └─────────────────────┘
│  + collides_with()  │
│  + compare()        │
│  + draw()           │
└───────┬─────────────┘
        │
        │ inheritance
        │
    ┌───┴───┬───────┬───────┐
    ▼       ▼       ▼       │
┌──────┐ ┌───────┐ ┌──────────┐
│ Rock │ │ Paper │ │ Scissors │
└──────┘ └───────┘ └──────────┘
```

## Key Design Principles

### 1. Separation of Concerns
- **Core**: Game logic only
- **UI**: Display only
- **Analysis**: Data collection only
- **Assets**: Graphics generation only

### 2. Dependency Injection
- Config passed to all components
- RNG passed for determinism
- Logger injected into World

### 3. Single Responsibility
- Each class has one clear purpose
- Collision logic separated from Agent
- Logging separated from World

### 4. Open/Closed Principle
- Easy to add new agent types (extend Agent)
- Easy to add new boundary modes
- Easy to add new event types

### 5. Testability
- Headless mode support
- Deterministic with seeds
- Small, focused methods
- Dependency injection

## Extension Points

### Adding New Agent Type
1. Create subclass of `Agent`
2. Define kind, color, radius, speed
3. Add to `BEATS` mapping in config
4. Create sprite in `sprites.py`
5. Update spawn logic

### Adding New Boundary Mode
1. Add mode to Config
2. Add handling method in Agent
3. Call from `update()`

### Adding New Analysis
1. Define new event type
2. Add logging method to Logger
3. Call from appropriate location
4. Update export logic

### Adding Spatial Optimization
1. Implement `SpatialHashGrid` class
2. Add to World initialization
3. Use in collision detection
4. Profile and tune cell size

## Performance Considerations

### Current Bottlenecks
1. **O(n²) collision detection** - All pairs checked
2. **Sprite recreation** - Each agent creates sprite in __init__
3. **Python overhead** - Interpreted language limits

### Optimization Strategies
1. **Spatial Hash Grid** - Reduce collision checks to O(n)
2. **Sprite Caching** - Create sprites once, reuse
3. **NumPy** - Vectorize position updates
4. **Cython** - Compile hot paths
5. **Culling** - Don't draw off-screen agents

### Scalability
- Current: ~200 agents at 60 FPS
- With spatial hash: ~1000 agents at 60 FPS
- With NumPy: ~2000 agents at 60 FPS
- With Cython: ~5000+ agents at 60 FPS

## Testing Strategy

### Test Coverage
- **Unit Tests**: Agent, Collision, World classes
- **Integration Tests**: Full simulation scenarios
- **Deterministic Tests**: Seed-based reproducibility

### Test Organization
```
tests/
├── test_agent.py       # 10 tests
│   ├── Creation
│   ├── RPS rules
│   ├── Collision detection
│   ├── Movement
│   └── Boundaries
│
├── test_collision.py   # 8 tests
│   ├── Detection
│   ├── Resolution
│   ├── Cooldown
│   └── Determinism
│
└── test_world.py       # 10 tests
    ├── Spawning
    ├── Population cap
    ├── Clearing
    ├── Counting
    └── Reset
```

---

This architecture provides a solid foundation for the RPS World simulation while remaining extensible for future enhancements.

