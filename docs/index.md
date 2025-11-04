# 🪨 Rock–Paper–Scissors World

Welcome to the **Rock–Paper–Scissors World** - an interactive simulation built with **Python & Pygame** 🎮

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![License](https://img.shields.io/badge/license-MIT-lightgrey)
![Pygame](https://img.shields.io/badge/Pygame-2.5.0+-orange)

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

Clone and run in 3 simple steps:

```bash
git clone https://github.com/cretzuwashere/RPS.git
cd RPS
pip install -r requirements.txt
python -m rps.app
```

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

- [Quick Reference Guide](https://github.com/cretzuwashere/RPS/blob/master/QUICK_REFERENCE.md)
- [Setup Instructions](https://github.com/cretzuwashere/RPS/blob/master/SETUP.md)
- [Development Plan](https://github.com/cretzuwashere/RPS/blob/master/RPS-plan.txt)
- [Usage Examples](https://github.com/cretzuwashere/RPS/blob/master/USAGE_EXAMPLES.md)

## 🤝 Contributing

Pull requests and ideas are always welcome! The project follows TDD principles - all core components have unit tests.

```bash
# Run tests
python run_tests.py
```

## 📄 License

This project is licensed under the **MIT License** - see [LICENSE](https://github.com/cretzuwashere/RPS/blob/master/LICENSE) for details.

---

**Made with ❤️ by [@cretzuwashere](https://github.com/cretzuwashere)**

