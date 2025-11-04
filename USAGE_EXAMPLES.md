# Usage Examples for RPS World

## Basic Usage

### Example 1: Simple Observation
1. Launch the application: `python run.py`
2. Press `1` to spawn 10 Rocks
3. Press `2` to spawn 10 Papers
4. Press `3` to spawn 10 Scissors
5. Watch the interactions unfold!

### Example 2: Manual Placement
1. Launch the application
2. Move your mouse to desired position
3. Press `R`, `P`, or `S` to spawn individual agents
4. Create specific patterns or scenarios

### Example 3: Testing Balance
1. Start with equal populations: Press `1`, `2`, `3` multiple times
2. Observe which type dominates over time
3. Press `F9` to export data
4. Press `F5` to reset and try again with new seed

## Analysis Workflows

### Workflow 1: Reproducible Experiments
```bash
# Run with specific seed
python -m rps.app --seed 12345

# In the app:
# 1. Press 1, 2, 3 to spawn agents
# 2. Let simulation run
# 3. Press F9 to export data
# 4. Check analysis_output/ directory for CSV files
```

### Workflow 2: Comparing Seeds
```bash
# Terminal 1
python -m rps.app --seed 100

# Terminal 2
python -m rps.app --seed 200

# Compare the dynamics in both windows
```

### Workflow 3: Performance Testing
```bash
# Test with many agents
python -m rps.app --width 1920 --height 1080 --fps 120

# In app, spawn many batches and monitor FPS in HUD
```

## Experimental Scenarios

### Scenario 1: Predator-Prey Dynamics
1. Spawn 50 Scissors (press `3` five times)
2. Spawn 5 Papers (press `2` once, then `P` for a few more)
3. Watch Papers eliminate Scissors
4. When Scissors are rare, spawn some Rocks
5. Observe the cycle

### Scenario 2: Spatial Patterns
1. Enable debug mode with `D`
2. Manually spawn agents in clusters
   - Cluster of Rocks in top-left
   - Cluster of Papers in top-right
   - Cluster of Scissors in bottom-center
3. Watch how clusters interact and merge

### Scenario 3: Survival Analysis
1. Launch: `python -m rps.app --seed 42`
2. Press `1`, `2`, `3` once each (10 of each type)
3. Note the spawn seed shown in HUD
4. Let simulation run until only one type remains
5. Press `F9` to export data
6. Open `analysis_output/collisions_*.csv` to see all interactions
7. Open `analysis_output/spawns_*.csv` to see initial positions

### Scenario 4: Finding Winning Positions
1. Run multiple simulations with same seed
2. Export data after each run
3. Analyze CSV to find which spawn positions lead to:
   - Longest survival time
   - Most kills
   - Early elimination
4. Use this data to understand spatial advantages

## Keyboard Shortcuts Reference

| Key | Action |
|-----|--------|
| `R` | Spawn Rock at mouse |
| `P` | Spawn Paper at mouse |
| `S` | Spawn Scissors at mouse |
| `1` | Spawn 10 Rocks randomly |
| `2` | Spawn 10 Papers randomly |
| `3` | Spawn 10 Scissors randomly |
| `Space` | Pause/Resume |
| `C` | Clear all agents |
| `D` | Toggle debug mode |
| `F5` | New random seed |
| `F9` | Export analysis CSV |
| `ESC` | Quit |

## Understanding the Display

### HUD Information
- **Rock/Paper/Scissors counts**: Current alive agents
- **Total**: Sum of all alive agents
- **Collisions**: Total number of collision events
- **FPS**: Current frames per second
- **Seed**: Random seed (for reproducibility)
- **PAUSED**: Shows when simulation is paused
- **DEBUG**: Shows when debug mode is active

### Visual Elements
- **Gray circles/sprites**: Rock agents
- **Yellow rectangles/sprites**: Paper agents
- **Red X-shapes/sprites**: Scissors agents

### Debug Mode (press D)
- White circles show collision radius
- Green lines show velocity vectors
- Helps understand movement and collision detection

## CSV Output Format

### spawns_*.csv
```csv
id,kind,x,y,tick
0,rock,543.2,234.1,0
1,paper,876.5,432.0,0
```

### collisions_*.csv
```csv
winner_id,winner_kind,loser_id,loser_kind,x,y,tick
0,rock,2,scissors,550.3,240.0,45
1,paper,0,rock,600.0,250.0,89
```

## Tips and Tricks

1. **Start Small**: Begin with 10-20 agents total to understand mechanics
2. **Use Pause**: Press Space to pause and examine the state
3. **Debug Mode**: Press D to see collision radii and velocities
4. **Clear Often**: Press C to clear and start fresh experiments
5. **Export Early**: Press F9 frequently to save interesting scenarios
6. **Seed Control**: Use `--seed` flag to reproduce interesting patterns
7. **Watch FPS**: If FPS drops below 30, clear some agents with C

## Common Patterns to Observe

1. **Rock-Paper-Scissors Cycles**: Watch populations cycle up and down
2. **Clustering**: Agents of same type tend to cluster after eliminating threats
3. **Edge Effects**: With wrap mode, agents reappear on opposite side
4. **Stochastic Outcomes**: Same seed gives same result, different seeds vary widely
5. **Winner-Takes-All**: Often one type eventually dominates completely

