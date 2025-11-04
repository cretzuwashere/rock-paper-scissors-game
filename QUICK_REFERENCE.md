# Quick Reference - RPS World

## 🎮 Quick Start

```bash
# Install
pip install -r requirements.txt

# Run
python -m rps.app --seed 100

# Test
python run_tests.py
```

---

## ⌨️ All Controls

| Key | Action |
|-----|--------|
| **R** | Spawn Rock at mouse |
| **P** | Spawn Paper at mouse |
| **S** | Spawn Scissors at mouse |
| **1** | Spawn 10 Rocks |
| **2** | Spawn 10 Papers |
| **3** | Spawn 10 Scissors |
| **B** | Random spawn (30-60 each) ⭐ |
| **Space** | Pause/Resume |
| **H** | Toggle hunting |
| **N** | Toggle names display ⭐ |
| **L** | Toggle language (EN ↔ RO) ⭐ |
| **C** | Clear all / Reset victory |
| **D** | Debug mode |
| **F5** | New seed + auto-spawn ⭐ |
| **F9** | Export CSV |
| **ESC** | Quit |

---

## 🎯 New Features

### 1. Named Agents
- Each agent has a unique name
- 40 names per type (Rock, Paper, Scissors)
- Examples: Boulder, Scroll, Blade
- Press **N** to toggle name display on/off

### 2. Kill Tracking
- Every agent tracks eliminations
- Displayed in victory scoreboard
- Sorted by kills (descending)
- **Shows ALL agents from winning faction** (including dead ones)

### 3. Victory Screen
- Appears when one faction wins
- Shows top 20 agents (with full count at bottom)
- **Includes ALL agents from winning faction** (even those who died)
- Gold/Silver/Bronze ranks for top 3
- Agents with 0 kills shown in gray
- Press C to clear and restart

### 4. Global Hunting
- Agents detect prey anywhere
- No range limit (was 200px)
- Always targets nearest prey
- Much faster games

### 5. Clueless Prey
- No flee behavior
- Prey acts unaware
- More dramatic hunting
- Easier catches

### 6. Random Spawn (B)
- Spawns 30-60 of each type
- Different counts each time
- Creates varied, large-scale battles

### 7. Auto-Spawn on Seed Change (F5)
- Press F5 to generate new random seed
- Automatically spawns balanced population (10 of each)
- Quick way to start fresh games

### 8. Multilingual Support (L)
- Press L to toggle between English and Romanian
- All UI elements translate instantly
- Victory screen, HUD, messages all localized
- Supports: English (EN) and Romanian (RO) 🌍

---

## 🪨📄✂️ Game Rules

```
Rock → Scissors  (Rock hunts Scissors)
Paper → Rock     (Paper hunts Rock)
Scissors → Paper (Scissors hunts Paper)
```

- **Global Detection**: Agents see prey everywhere
- **No Fleeing**: Prey acts clueless
- **Victory**: Last faction standing wins
- **Scoreboard**: Top killers ranked

---

## 📊 Example Game

```bash
# 1. Start game
python -m rps.app --seed 100

# 2. Press B for random spawn
"Random Spawn: 18 Rocks, 25 Papers, 31 Scissors"

# 3. Watch the battle unfold
- Scissors hunt Papers globally
- Rocks hunt Scissors
- Papers hunt Rocks

# 4. Victory screen appears
"PAPERS WIN!"
Scoreboard:
  #1 Scroll      12 kills  (Gold)
  #2 Parchment   10 kills  (Silver)
  #3 Manuscript   8 kills  (Bronze)
  ...

# 5. Press C to start new game
```

---

## 🏷️ Agent Names

### Rocks (40 names)
Boulder, Granite, Obsidian, Flint, Slate, Marble, Basalt, Quartz, Pebble, Stone, Cliff, Rocky, Crusher, Titan, Golem, Brick, Cobble, Gravel, Shale, Pumice, Onyx, Jade, Ruby, Diamond, Emerald, Topaz, Opal, Amber, Crystal, Gem, Spike, Crag, Mesa, Canyon, Ridge, Peak, Summit, Monolith, Megalith, Dolmen

### Papers (40 names)
Scroll, Parchment, Manuscript, Document, Letter, Note, Page, Sheet, Papyrus, Vellum, Folio, Leaflet, Pamphlet, Flyer, Poster, Banner, Card, Ticket, Receipt, Invoice, Contract, Treaty, Charter, Deed, Certificate, Diploma, License, Permit, Warrant, Writ, Summons, Subpoena, Origami, Confetti, Tissue, Napkin, Towel, Wrapper, Envelope, Label

### Scissors (40 names)
Blade, Shear, Clipper, Cutter, Slicer, Snipper, Trimmer, Razor, Knife, Dagger, Sword, Saber, Scimitar, Katana, Rapier, Cutlass, Machete, Cleaver, Scalpel, Shiv, Stiletto, Dirk, Tanto, Wakizashi, Excalibur, Masamune, Kusanagi, Durandal, Joyeuse, Tyrfing, Gram, Naegling, Snip, Slash, Cut, Chop, Slice, Dice, Mince, Julienne

---

## 🧪 Testing

```bash
# Run all tests
python run_tests.py

# Expected output
Ran 38 tests in 0.349s
OK
```

---

## 📁 Key Files

| File | Purpose |
|------|---------|
| `rps/core/agent.py` | Agent logic, hunting, movement |
| `rps/core/names.py` | Name generation |
| `rps/core/world.py` | World orchestration, victory |
| `rps/ui/victory_screen.py` | Victory UI |
| `rps/app.py` | Main application |
| `NEW_FEATURES_SUMMARY.md` | Detailed feature docs |
| `README.md` | Project overview |

---

## 🎨 Victory Screen Layout

```
┌─────────────────────────────────────────┐
│                                         │
│            ROCKS WIN!                   │
│                                         │
│     SCOREBOARD - Top Killers            │
│                                         │
│  #1  Boulder        15 kills   (Gold)   │
│  #2  Granite        12 kills   (Silver) │
│  #3  Obsidian       10 kills   (Bronze) │
│  #4  Flint           8 kills            │
│  #5  Slate           7 kills            │
│  ...                                    │
│                                         │
│  Press C to clear and start new game    │
└─────────────────────────────────────────┘
```

---

## 💡 Tips

### For Fast Games
```
1. Press B (random spawn)
2. Watch global hunting in action
3. Victory in ~30-60 seconds
```

### For Observation
```
1. Press 1, 2, 3 (balanced spawn)
2. Press H to toggle hunting on/off
3. Watch natural movement vs hunting
```

### For Analysis
```
1. Run with seed: python -m rps.app --seed 42
2. Press F9 to export CSV
3. Analyze collision patterns
```

---

## 🚀 Command Line Options

```bash
# With seed
python -m rps.app --seed 100

# With API enabled
python -m rps.app --api-enabled

# Both
python -m rps.app --seed 100 --api-enabled
```

---

## ✅ Status

- ✅ Named agents
- ✅ Toggle name display (N)
- ✅ Kill tracking
- ✅ Victory detection
- ✅ Scoreboard
- ✅ Global hunting
- ✅ Clueless prey
- ✅ Random spawn (B)
- ✅ Auto-spawn on seed change (F5)
- ✅ Multilingual support (English/Romanian)
- ✅ All tests passing
- ✅ Ready to play!

---

**Have fun! 🎮🪨📄✂️**

