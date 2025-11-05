# 🪨 Rock–Paper–Scissors World

Welcome to the **Rock–Paper–Scissors World** - an interactive simulation built with **Python & Pygame** 🎮

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![License](https://img.shields.io/badge/license-MIT-lightgrey)
![Pygame](https://img.shields.io/badge/Pygame-2.5.0+-orange)

**English Version** | **[Versiune Română](index.ro.md)**

## 🎮 About

A dynamic simulation where autonomous agents (Rock, Paper, Scissors) move, hunt, and battle in real-time. Watch as populations rise and fall, with victory screens celebrating the champions!

### ✨ Key Features

- **Named Agents** - Each agent has a unique identity (Boulder, Scroll, Blade, etc.)
- **Kill Tracking** - Scoreboard rankings with gold/silver/bronze medals
- **Global Hunting** - Predators hunt prey across the entire map
- **Victory Detection** - Automatic game-over when one faction dominates
- **Multilingual** - Toggle between English and Romanian
- **Real-time Stats** - Live HUD showing population and game state

## 🚀 Play It Locally

### Step 0: Install Python (if you don't have it)

**Windows:**
1. Download Python from [python.org/downloads](https://www.python.org/downloads/)
2. Run the installer
3. ✅ **IMPORTANT:** Check "Add Python to PATH" during installation
4. Click "Install Now"
5. Verify: Open Command Prompt and type `python --version`

### Step 1: Download the Game

**Option A: Using Git** (if you have it)
```bash
git clone https://github.com/cretzuwashere/rock-paper-scissors-game.git
cd rock-paper-scissors-game
```

**Option B: Direct Download** (easier for beginners)
1. Go to [github.com/cretzuwashere/rock-paper-scissors-game](https://github.com/cretzuwashere/rock-paper-scissors-game)
2. Click the green **"Code"** button
3. Click **"Download ZIP"**
4. Extract the ZIP file
5. Open Command Prompt in that folder (Shift + Right-click → "Open PowerShell window here")

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run the Game!

```bash
python -m rps.app
```

**Quick Controls:**
- Press `B` to spawn a battle
- Press `Space` to pause
- Press `L` to switch language (English/Romanian)

## 🎯 Game Rules

- **Rock** 🪨 beats **Scissors** ✂️
- **Scissors** ✂️ beats **Paper** 📄
- **Paper** 📄 beats **Rock** 🪨

Agents actively hunt their prey across the entire board. When they collide, the loser is eliminated and the winner continues!

## 🎮 Controls

### Spawning
- `R` / `P` / `S` - Spawn at mouse position
- `1` / `2` / `3` - Spawn 10 agents randomly
- `B` - Random spawn (30-60 of each faction)

### Game Control
- `Space` - Pause/Resume
- `H` - Toggle hunting behavior
- `N` - Toggle names display
- `C` - Clear all and reset
- `F5` - New random seed + auto-spawn
- `L` - Toggle language (EN/RO)

## 🛠️ Tech Stack

- **Python 3.10+** - Core language
- **Pygame 2.5+** - Graphics and game loop
- **NumPy** - Efficient calculations
- **Test-Driven Development** - Comprehensive test suite

## 📚 Documentation

- [Quick Reference Guide](https://github.com/cretzuwashere/rock-paper-scissors-game/blob/master/QUICK_REFERENCE.md)
- [Setup Instructions](https://github.com/cretzuwashere/rock-paper-scissors-game/blob/master/SETUP.md)
- [Development Plan](https://github.com/cretzuwashere/rock-paper-scissors-game/blob/master/RPS-plan.txt)
- [Usage Examples](https://github.com/cretzuwashere/rock-paper-scissors-game/blob/master/USAGE_EXAMPLES.md)

## 🤝 Contributing

Pull requests and ideas are always welcome! The project follows TDD principles - all core components have unit tests.

```bash
# Run tests
python run_tests.py
```

## 📄 License

This project is licensed under the **MIT License** - see [LICENSE](https://github.com/cretzuwashere/rock-paper-scissors-game/blob/master/LICENSE) for details.

---

**Made with ❤️ by [@cretzuwashere](https://github.com/cretzuwashere)**

