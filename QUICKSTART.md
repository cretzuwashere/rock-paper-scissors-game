# Quick Start Guide

Get up and running with RPS World in 3 steps!

## Step 1: Install Dependencies

### Windows
Double-click `install.bat` or run in terminal:
```cmd
install.bat
```

### Linux/Mac
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Step 2: Run the Application

### Windows
Double-click `run.bat` or:
```cmd
python run.py
```

### Linux/Mac
```bash
python3 run.py
```

## Step 3: Spawn Some Agents!

Once the window opens:
1. Press `1` to spawn 10 Rocks
2. Press `2` to spawn 10 Papers
3. Press `3` to spawn 10 Scissors
4. Watch them interact!

## Essential Controls

| Key | Action |
|-----|--------|
| `1`, `2`, `3` | Spawn 10 agents randomly |
| `R`, `P`, `S` | Spawn at mouse position |
| `Space` | Pause/Resume |
| `C` | Clear screen |
| `ESC` | Quit |

## What You'll See

- **Gray sprites** = Rocks (beat Scissors)
- **Yellow sprites** = Papers (beat Rock)
- **Red sprites** = Scissors (beat Paper)

When agents collide, the loser disappears!

## Next Steps

- Press `D` for debug mode (see collision radii)
- Press `F9` to export analysis data
- Press `F5` to reset with new random seed
- Read `USAGE_EXAMPLES.md` for experiment ideas
- Check `SETUP.md` for advanced configuration

## Troubleshooting

**No window appears?**
- Make sure pygame is installed: `pip install pygame`
- Check that Python 3.8+ is installed: `python --version`

**App is slow?**
- Press `C` to clear agents
- Reduce spawn numbers (press `1`/`2`/`3` fewer times)

**Need help?**
- See `README.md` for full documentation
- Check `SETUP.md` for detailed instructions

---

**Have fun watching the Rock-Paper-Scissors world evolve!** 🎮

