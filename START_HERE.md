# 🎮 RPS World - START HERE

Welcome to **Rock-Paper-Scissors World**! This file will get you started in under 5 minutes.

## 🚀 Three Steps to Start

### Step 1: Install Dependencies (1 minute)

**Windows**: Double-click `install.bat`

**Mac/Linux**:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Step 2: Run the App (30 seconds)

**Windows**: Double-click `run.bat`

**Mac/Linux**:
```bash
python run.py
```

### Step 3: Spawn Some Agents! (1 minute)

Press these keys:
- `1` - Spawn 10 Rocks (gray)
- `2` - Spawn 10 Papers (yellow)
- `3` - Spawn 10 Scissors (red)

**Watch them interact!** When they collide:
- Rock beats Scissors
- Paper beats Rock
- Scissors beats Paper

The loser disappears! 💥

## 🎯 Quick Controls

| Key | What It Does |
|-----|--------------|
| `1`, `2`, `3` | Spawn 10 agents randomly |
| `R`, `P`, `S` | Spawn at mouse cursor |
| `Space` | Pause/Resume |
| `C` | Clear all agents |
| `ESC` | Quit |

## 📖 Learn More

Want to dive deeper? Check out:

1. **[QUICKSTART.md](QUICKSTART.md)** - Detailed quick start with troubleshooting
2. **[VISUAL_GUIDE.md](VISUAL_GUIDE.md)** - See what everything looks like
3. **[USAGE_EXAMPLES.md](USAGE_EXAMPLES.md)** - Cool experiments to try
4. **[INDEX.md](INDEX.md)** - Complete documentation guide

## 🎨 What You'll See

```
┌─────────────────────────────────────┐
│ RPS World              DEBUG        │
│ Rock: 15    (gray)                  │
│ Paper: 12   (yellow)                │
│ Scissors: 8 (red)                   │
│ Total: 35                           │
│ Collisions: 47                      │
│ FPS: 60.0                           │
│ ┌─────────────────────────────────┐ │
│ │                                 │ │
│ │   ●  Rock                       │ │
│ │        ▭  Paper                 │ │
│ │            ✂ Scissors            │ │
│ │                                 │ │
│ │  [Agents move and collide]      │ │
│ │                                 │ │
│ └─────────────────────────────────┘ │
│                                     │
│ Controls: R/P/S=Spawn | Space=Pause│
└─────────────────────────────────────┘
```

## 💡 Cool Things to Try

### Experiment 1: Balanced Start
```
Press: 1, 2, 3
Watch: Which type survives?
```

### Experiment 2: Manual Placement
```
Move mouse to corner
Press: R (spawn Rock)
Move to opposite corner
Press: S (spawn Scissors)
Watch them meet!
```

### Experiment 3: Export Data
```
Press: 1, 2, 3 (spawn agents)
Wait: Let them interact
Press: F9 (export data)
Check: analysis_output/ folder for CSV files
```

## 🐛 Troubleshooting

**Nothing happens?**
- Make sure you installed pygame: `pip install pygame`
- Check Python version: `python --version` (need 3.8+)

**Window closes immediately?**
- Run from terminal to see errors
- Try: `python run.py` instead of double-clicking

**Too slow?**
- Press `C` to clear agents
- Spawn fewer at a time

## 📚 Full Documentation

This project has **extensive documentation**:

- **11 documentation files**
- **2,500+ lines of guides**
- **Step-by-step tutorials**
- **Architecture diagrams**
- **Usage examples**

Start with **[INDEX.md](INDEX.md)** to navigate everything!

## 🎓 What This Project Includes

✅ Complete working application  
✅ Beautiful graphical interface  
✅ Classic R-P-S game rules  
✅ Analysis and data export  
✅ Comprehensive test suite (28 tests)  
✅ Extensive documentation (10+ files)  
✅ Cross-platform (Windows/Mac/Linux)  
✅ Professional code quality  

## 🚀 Ready to Start?

1. Run: `python run.py` (or `run.bat` on Windows)
2. Press: `1`, `2`, `3` to spawn agents
3. Enjoy: Watch the Rock-Paper-Scissors world evolve!

---

**Questions?** Check **[INDEX.md](INDEX.md)** for all documentation!

**Have fun!** 🎮🪨📄✂️

