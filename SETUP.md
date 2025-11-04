# Setup Guide for RPS World

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation Steps

### 1. Clone or Download the Project

```bash
cd C:\Projects\Discord\RPS
```

### 2. Create Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

### Start the Simulation

```bash
# Using the launcher script
python run.py

# Or using the module directly
python -m rps.app
```

### Command Line Options

```bash
python -m rps.app --help
```

Available options:
- `--seed SEED` - Set random seed for reproducibility
- `--width WIDTH` - Set window width (default: 1200)
- `--height HEIGHT` - Set window height (default: 800)
- `--fps FPS` - Set target FPS (default: 60)
- `--no-log` - Disable event logging

Example:
```bash
python -m rps.app --seed 42 --width 1920 --height 1080 --fps 120
```

## Running Tests

```bash
# Run all tests
python run_tests.py

# Run specific test file
python -m unittest tests.test_agent

# Run with verbose output
python -m unittest discover -v tests
```

## Controls Quick Reference

### Spawning
- `R` - Spawn Rock at mouse position
- `P` - Spawn Paper at mouse position
- `S` - Spawn Scissors at mouse position
- `1` - Spawn 10 Rocks randomly
- `2` - Spawn 10 Papers randomly
- `3` - Spawn 10 Scissors randomly

### Game Control
- `Space` - Pause/Resume simulation
- `C` - Clear all agents
- `D` - Toggle debug mode (shows collision radii and velocity vectors)
- `F5` - Reset with new random seed
- `ESC` - Quit application

### Analysis
- `F9` - Export analysis data to CSV files

## Troubleshooting

### Pygame not found
```bash
pip install pygame>=2.5.0
```

### Display issues on Linux
If you encounter display issues on Linux, ensure SDL2 is installed:
```bash
# Ubuntu/Debian
sudo apt-get install libsdl2-dev

# Fedora
sudo dnf install SDL2-devel
```

### Performance issues
- Reduce population (clear with `C` if too many agents)
- Lower FPS: `python -m rps.app --fps 30`
- Disable logging: `python -m rps.app --no-log`

## Project Structure

```
RPS/
├── rps/                    # Main package
│   ├── app.py             # Application entry point
│   ├── core/              # Core game logic
│   │   ├── agent.py       # Agent classes
│   │   ├── world.py       # World simulation
│   │   ├── collision.py   # Collision detection
│   │   └── config.py      # Configuration
│   ├── ui/                # User interface
│   │   └── hud.py         # Heads-up display
│   ├── analysis/          # Analysis tools
│   │   └── logger.py      # Event logging
│   └── assets/            # Graphics assets
│       └── sprites.py     # Sprite generation
├── tests/                 # Test suite
├── requirements.txt       # Python dependencies
├── run.py                 # Quick launcher
└── README.md             # Documentation
```

## Next Steps

1. Start with a small number of agents to understand the dynamics
2. Try different spawn patterns to see emergent behavior
3. Use F9 to export data and analyze results
4. Experiment with different random seeds for reproducibility

