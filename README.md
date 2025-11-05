# 🪨 Rock–Paper–Scissors World ✂️

![Python CI](https://github.com/cretzuwashere/rock-paper-scissors-game/workflows/Python%20CI/badge.svg)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![License](https://img.shields.io/badge/license-MIT-lightgrey)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-green)
![Pygame](https://img.shields.io/badge/Pygame-2.5.0+-orange)

A Python application with a graphical interface that simulates a Rock–Paper–Scissors world where agents move, hunt, and interact according to the classic game rules.

> **New here?** Check out **[START_HERE.md](START_HERE.md)** for a quick 3-step guide! 🚀
> 
> **Română?** Vezi **[README.ro.md](README.ro.md)** pentru versiunea în limba română! 🇷🇴
>
> **Live Demo:** [GitHub Pages](https://cretzuwashere.github.io/rock-paper-scissors-game/)

## Features

- Three types of objects (Rock, Paper, Scissors) that move freely across the screen
- **Named agents** - Each agent has a unique name (Boulder, Scroll, Blade, etc.) 🏷️
- **Kill tracking** - Agents track their eliminations for scoreboard rankings 🏆
- **Victory detection** - Game automatically detects when one faction wins! 🎉
- **Scoreboard** - Beautiful victory screen showing top killers with gold/silver/bronze ranks
- **Global hunting** - Agents hunt prey across the entire board (no range limit) 🎯
- **Clueless prey** - Prey acts unaware of danger (no flee behavior) 😴
- **Factory pattern** - Clean, extensible agent creation system
- **Random spawn** - Press `B` for random numbers of each faction (30-60 each)
- **Multilingual support** - Toggle between English and Romanian with `L` key 🌍
- Collision-based interactions following classic R-P-S rules
- Real-time visualization with Pygame
- Toggleable hunting mode (press `H`)
- Analysis and logging of interactions
- Spawn objects manually or in batches

## 🚀 Quick Start

### For Complete Beginners (Windows) - EASIEST METHOD

**Don't have Python?**
1. Download from [python.org/downloads](https://www.python.org/downloads/)
2. Run installer, ✅ check "Add Python to PATH"
3. Restart your computer

**Download & Play:**
1. Click the green **"Code"** button above → **"Download ZIP"**
2. Extract the ZIP file to your Desktop
3. **Double-click `install.bat`** ← This installs everything!
4. **Double-click `run.bat`** ← This runs the game!

**That's it!** Press `B` to start a battle! 🎮

---

### Alternative Method (Any OS)

```bash
# If you cloned with Git or the .bat files don't work:
pip install -r requirements.txt
python run.py
```

---

### For Developers

```bash
# Clone the repository
git clone https://github.com/cretzuwashere/rock-paper-scissors-game.git
cd rock-paper-scissors-game

# Option 1: Use the provided scripts
./install.bat    # Windows
python run.py

# Option 2: Manual setup with virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python -m rps.app

# Option 3: Install as a package
pip install -e .
rps-world
```

## Controls

### Spawning
- `R` - Spawn Rock at mouse position
- `P` - Spawn Paper at mouse position
- `S` - Spawn Scissors at mouse position
- `1` - Spawn 10 Rocks randomly
- `2` - Spawn 10 Papers randomly
- `3` - Spawn 10 Scissors randomly
- `B` - Random spawn (30-60 of each faction) ⭐ NEW!

### Game Control
- `Space` - Pause/Resume
- `H` - Toggle hunting behavior
- `N` - Toggle names display (show/hide agent names)
- `C` - Clear all objects (also resets victory screen)
- `D` - Toggle debug mode
- `F5` - New random seed + auto-spawn balanced population
- `ESC` - Quit

### Analysis
- `F9` - Export analysis to CSV

## Project Structure

```
rps/
├── app.py              # Main entry point
├── core/
│   ├── agent.py        # Base Agent and subclasses
│   ├── world.py        # World orchestration
│   ├── collision.py    # Collision detection/resolution
│   ├── config.py       # Configuration and constants
│   └── spatial.py      # Spatial optimization (future)
├── ui/
│   └── hud.py          # HUD overlay
├── analysis/
│   ├── logger.py       # Event logging
│   └── exporter.py     # Data export utilities
└── assets/
    └── sprites/        # Sprite images

tests/                  # Unit and integration tests
```

## Game Rules

- Rock beats Scissors (and hunts them globally!)
- Paper beats Rock (and hunts them globally!)
- Scissors beat Paper (and hunt them globally!)
- When objects collide, the loser disappears and the winner continues
- **Agents hunt prey across the entire board** (global detection)
- **Prey acts clueless** - no flee behavior, unaware of danger
- **Victory** - When only one faction remains, game shows scoreboard with top killers
- Each agent tracks kills and has a unique name (e.g., "Boulder", "Scroll", "Blade")

## Documentation

- **`QUICK_REFERENCE.md`** - Quick reference guide with all controls and features ⭐
- **`RPS-plan.txt`** - Complete development plan and architecture details
- **`SETUP.md`** - Detailed setup and installation instructions
- **`USAGE_EXAMPLES.md`** - Usage examples and experimental scenarios

## Implementation Status

✅ Complete implementation with:
- Agent base class with Rock/Paper/Scissors subclasses
- Physics simulation (movement, wrap/bounce boundaries)
- Collision detection and resolution
- World orchestration and state management
- HUD overlay with real-time statistics
- Event logging and CSV export for analysis
- Enhanced sprite graphics for each agent type
- Comprehensive test suite
- Command-line interface with options
- Deterministic reproduction via seed control

## Development

The project follows Test-Driven Development principles. All core components have unit tests.

Run tests with:
```bash
python run_tests.py
```

## Future Enhancements

Potential extensions as outlined in the development plan:
- Spatial hash grid for performance optimization with large populations
- Sound effects for collisions
- Settings UI panel
- Heatmap visualizations
- Obstacles and walls
- Replay/recording to video
- Scenario file loader (JSON format)

