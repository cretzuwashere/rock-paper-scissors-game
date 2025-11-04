# Visual Guide to RPS World

This guide shows what you'll see when running the application and explains each visual element.

## Application Window Layout

```
╔═══════════════════════════════════════════════════════════════════════════╗
║  RPS World                                                    ┌─────────┐ ║
║  Rock: 15    [gray color]                                     │ DEBUG   │ ║
║  Paper: 12   [yellow color]                                   └─────────┘ ║
║  Scissors: 8 [red color]                                                  ║
║  Total: 35                                                                ║
║  Collisions: 47                                                           ║
║  FPS: 60.0                                                                ║
║  Seed: 42                                                                 ║
║  ┌────────────────────────────────────────────────────────────────────┐  ║
║  │                                                                    │  ║
║  │        ●  Rock (gray)                                              │  ║
║  │                  ▭  Paper (yellow)                                 │  ║
║  │                                                                    │  ║
║  │                        ✂  Scissors (red)                           │  ║
║  │          ●                                                         │  ║
║  │                                    ▭                               │  ║
║  │                  ✂                                                 │  ║
║  │                            ●                                       │  ║
║  │                                      ▭                             │  ║
║  │      ✂                                                             │  ║
║  │                 ●                                                  │  ║
║  │                          ▭                                         │  ║
║  │                                   ✂                                │  ║
║  │           PLAYFIELD AREA                                           │  ║
║  │           (Agents move freely here)                                │  ║
║  │                                                                    │  ║
║  │                                                                    │  ║
║  └────────────────────────────────────────────────────────────────────┘  ║
║                                                                           ║
║  Controls: R/P/S=Spawn at mouse | 1/2/3=Batch spawn | Space=Pause        ║
║  C=Clear | D=Debug | F9=Export CSV | F5=New seed | ESC=Quit              ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

## Visual Elements Explained

### 1. HUD (Top-Left Corner)

```
┌─────────────────────────┐
│ RPS World               │  ← Title
│ Rock: 15                │  ← Count in gray color
│ Paper: 12               │  ← Count in yellow color
│ Scissors: 8             │  ← Count in red color
│ Total: 35               │  ← Total agents
│ Collisions: 47          │  ← Total collision events
│ FPS: 60.0               │  ← Current frames per second
│ Seed: 42                │  ← Random seed (for reproducibility)
└─────────────────────────┘
```

**Background**: Semi-transparent black overlay (80% opacity)
**Text Colors**: White for labels, colored for counts

### 2. Agent Sprites

#### Rock Sprite (Gray)
```
      ╱╲
     ╱  ╲
    │  ▒▒│
    │ ▒▒▒│
     ╲  ╱
      ╲╱
```
- **Shape**: Irregular polygon (8 vertices)
- **Color**: Gray (#787878)
- **Details**: Shading circles for texture
- **Border**: Darker gray outline
- **Size**: 15 pixels radius (default)

#### Paper Sprite (Yellow)
```
    ┌───────┐
    │  │  │ │
    │  │  │ │
    │  │  │◢│
    └───────┘
```
- **Shape**: Rotated rectangle
- **Color**: Yellow (#FFFF64)
- **Details**: Fold lines, corner fold
- **Border**: Darker yellow outline
- **Size**: 12 pixels radius (default)

#### Scissors Sprite (Red)
```
      ╲ ╱
       ╳
      ╱ ╲
```
- **Shape**: Two crossing blades
- **Color**: Red (#FF6464)
- **Details**: Center pivot point
- **Border**: Darker red outline
- **Size**: 13 pixels radius (default)

### 3. Status Indicators

#### When Paused
```
╔═════════════════════════════════════════╗
║                                         ║
║            ⚠ PAUSED ⚠                   ║
║                                         ║
║        (in bright yellow)               ║
╚═════════════════════════════════════════╝
```
- **Position**: Center-top of screen
- **Color**: Bright yellow (#FFFF00)
- **Font**: Large (36pt)

#### When Debug Mode Active
```
╔═══════════════════════════════════╗
║                     ┌─────────┐   ║
║                     │ DEBUG   │   ║
║                     └─────────┘   ║
╚═══════════════════════════════════╝
```
- **Position**: Top-right corner
- **Color**: Green (#00FF00)
- **Font**: Small (24pt)

### 4. Debug Visualization

When debug mode is active (press `D`):

```
        ○  ←─── White circle (collision radius)
       ╱│╲
      ╱ │ ╲
     ╱  │  ╲    ←─── Green line (velocity vector)
    ╱   ●   ╲       points in movement direction
   ╱    │    ╲
  ╱     │     ╲
 ╱      │      ╲
        ↓
```

**Elements**:
- White circle outline = collision detection radius
- Green arrow = velocity vector (direction and speed)
- Helps understand agent movement and collisions

### 5. Temporary Messages

```
╔═════════════════════════════════════════╗
║                                         ║
║                                         ║
║     ┌─────────────────────────┐         ║
║     │  Spawned 10 Rocks!     │         ║
║     └─────────────────────────┘         ║
║                                         ║
╚═════════════════════════════════════════╝
```
- **Position**: Lower center of screen
- **Background**: Semi-transparent black
- **Color**: Green (#00FF00)
- **Duration**: 2 seconds
- **Appears**: After spawn, clear, export, etc.

### 6. Control Hints (Bottom)

```
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║  Controls: R/P/S=Spawn at mouse | 1/2/3=Batch spawn...    ║
║  C=Clear | D=Debug | F9=Export CSV | F5=New seed...       ║
╚════════════════════════════════════════════════════════════╝
```
- **Position**: Bottom of screen (2 lines)
- **Color**: Light gray (#B4B4B4)
- **Font**: Tiny (18pt)
- **Always visible**

## Interaction Visualizations

### Collision Between Agents

**Before Collision**:
```
    ●────→        ✂────→
   Rock         Scissors
```

**During Collision**:
```
    ●  ✂
   Rock wins!
```

**After Collision**:
```
    ●────→        (Scissors disappeared)
   Rock continues
```

### Wrap Boundary Mode

```
╔═══════════════════════════════════════╗
║                                       ║
║  ●────→                               ║
║                                    ●─→║
║                                     ╱ ║
║                                    ╱  ║
║                                   ╱   ║
║  ←─● (appears on left)          ╱    ║
║                                ╱     ║
╚═══════════════════════════════════════╝
```
Agent exits right, reappears on left

### Bounce Boundary Mode

```
╔═══════════════════════════════════════╗
║                                       ║
║  ●────→                               ║
║                                    ●─→║
║                                     ↓ ║
║                                    ●  ║
║                                   ↙   ║
║                                  ●    ║
║                                ←─●    ║
╚═══════════════════════════════════════╝
```
Agent bounces off wall, reverses direction

## Color Scheme

### Background
- **Main playfield**: Dark blue-gray (#14141E)

### Agent Colors
- **Rock**: Medium gray (#787878) - appears solid and heavy
- **Paper**: Bright yellow (#FFFF64) - appears light and flexible  
- **Scissors**: Coral red (#FF6464) - appears sharp and aggressive

### UI Colors
- **HUD background**: Black with 70% transparency
- **HUD text**: White (#FFFFFF) for labels
- **HUD counts**: Match agent colors
- **Status text**: 
  - Paused: Yellow (#FFFF00)
  - Debug: Green (#00FF00)
  - Messages: Green (#00FF00)
- **Control hints**: Light gray (#B4B4B4)

### Debug Colors
- **Collision radii**: White (#FFFFFF)
- **Velocity vectors**: Bright green (#00FF00)

## Screen Resolutions

### Default (1200 x 800)
```
┌────────────────────────────────┐
│  Comfortable for most screens  │
│  Good balance of space/detail  │
│  Recommended for learning      │
└────────────────────────────────┘
```

### HD (1920 x 1080)
```
┌──────────────────────────────────────────┐
│  More space for agents                   │
│  Better for large populations            │
│  Use: --width 1920 --height 1080         │
└──────────────────────────────────────────┘
```

### Compact (800 x 600)
```
┌─────────────────────────┐
│  Smaller window         │
│  Good for side-by-side  │
│  Use: --width 800       │
│       --height 600      │
└─────────────────────────┘
```

## Animation States

### Agent Movement
- **Speed**: Varies by type (50-120 pixels/second)
- **Smoothness**: 60 FPS = very smooth motion
- **Rotation**: Sprites don't rotate (face all directions)

### Collision Resolution
- **Instant**: Loser disappears immediately
- **No explosion**: Simple removal (can add effects later)
- **Winner continues**: Maintains velocity

### Spawning
- **Instant**: Agent appears immediately
- **Position**: 
  - At mouse (R/P/S keys)
  - Random location (1/2/3 keys)
- **Initial velocity**: Random direction and speed

## Typical Scenarios

### Early Game (Few Agents)
```
  ●              ▭           ✂
     ●    ▭             ✂        ●
        ✂    ●      ▭        ●
   ▭           ✂         ▭
```
- Sparse distribution
- Slow collision rate
- Easy to track individuals

### Mid Game (Many Agents)
```
●●▭✂ ●▭▭ ✂● ▭✂ ●●
▭✂●● ✂▭ ●▭✂ ▭● ✂▭
✂▭● ▭✂● ●▭ ✂✂ ▭●
●✂▭ ●●▭ ✂▭ ●✂ ▭✂
```
- Dense populations
- Frequent collisions
- Emergent patterns

### End Game (One Type Dominates)
```
  ●       ●         ●
     ●         ●         ●
        ●    ●      ●        ●
   ●          ●          ●
```
- Single type remaining
- No more collisions
- Stable state

## Export Preview

When you press F9, CSV files are created:

### spawns_20251104_143022.csv
```
id,kind,x,y,tick
0,rock,543.2,234.1,0
1,paper,876.5,432.0,0
2,scissors,234.7,654.3,0
...
```

### collisions_20251104_143022.csv
```
winner_id,winner_kind,loser_id,loser_kind,x,y,tick
0,rock,2,scissors,550.3,240.0,45
1,paper,0,rock,600.0,250.0,89
...
```

---

**Now you know what to expect when you run RPS World!** 🎮

Try it yourself: `python run.py`

