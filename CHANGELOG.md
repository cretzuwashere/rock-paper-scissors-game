# Changelog

All notable changes to RPS World will be documented in this file.

## [0.1.0] - 2025-11-04

### Initial Release

#### Added
- Core agent system with base Agent class
- Rock, Paper, and Scissors agent types with classic rules
- Physics simulation with movement and boundary handling (wrap/bounce modes)
- Collision detection and resolution system
- Deterministic collision ordering for reproducibility
- Collision cooldown mechanism
- World orchestration and state management
- Spawn system (manual, random, and batch)
- Population cap enforcement
- Real-time HUD overlay showing:
  - Agent counts by type
  - Total collision count
  - FPS monitoring
  - Random seed display
  - Pause/debug indicators
- Event logging system
- CSV export for spawn and collision analysis
- Enhanced sprite graphics for each agent type:
  - Irregular polygon for Rock
  - Folded rectangle for Paper
  - Crossed blades for Scissors
- Keyboard controls for spawning and game control
- Debug mode with visualization of:
  - Collision radii
  - Velocity vectors
- Command-line interface with options:
  - Custom seed
  - Window dimensions
  - FPS target
  - Logging toggle
- Comprehensive test suite:
  - Agent behavior tests
  - Collision detection tests
  - World orchestration tests
  - Deterministic behavior verification
- Project documentation:
  - README with quick start
  - SETUP guide with detailed instructions
  - USAGE_EXAMPLES with scenarios
  - RPS-plan.txt with architecture details

#### Technical Details
- Python 3.8+ compatible
- Pygame-based rendering
- Modular architecture (core, ui, analysis, assets)
- Random seed control for reproducibility
- Headless testing support

## Future Versions

### Planned Features
- Spatial hash grid for performance optimization
- Sound effects and visual effects
- Settings UI panel
- Heatmap visualizations
- Scenario file loader (JSON)
- Replay system
- Additional boundary modes
- Particle effects
- Network synchronization

