"""Main application entry point."""

import pygame
import sys
import threading
from .core.config import Config
from .core.world import World
from .core.language import Language
from .ui.hud import HUD
from .ui.victory_screen import VictoryScreen
from .analysis.logger import AnalysisLogger
from .api.spawn_queue import SpawnQueue


class RPSApp:
    """Main application class for RPS World."""
    
    def __init__(self, config: Config = None, api_enabled: bool = False):
        """Initialize the application.
        
        Args:
            config: Optional game configuration
            api_enabled: Enable API server for external spawning
        """
        self.config = config or Config()
        self.api_enabled = api_enabled
        
        # Initialize Pygame
        pygame.init()
        self.screen = pygame.display.set_mode(
            (self.config.screen_width, self.config.screen_height)
        )
        pygame.display.set_caption("Rock-Paper-Scissors World")
        
        self.clock = pygame.time.Clock()
        
        # Initialize components
        self.logger = AnalysisLogger() if self.config.log_events else None
        self.language = Language(self.config.language)
        self.world = World(self.config, self.logger)
        self.hud = HUD(self.config, self.language)
        self.victory_screen = VictoryScreen(self.language)
        
        # API spawn queue
        self.spawn_queue = SpawnQueue() if api_enabled else None
        self.api_thread = None
        
        # App state
        self.running = True
        self.message = None
        self.message_timer = 0
        
        print(f"RPS World initialized with seed: {self.config.seed}")
        
        # Start API server if enabled
        if self.api_enabled:
            self._start_api_server()
    
    def handle_events(self):
        """Handle pygame events."""
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            elif event.type == pygame.KEYDOWN:
                self._handle_keydown(event, mouse_pos)
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    self._handle_mouse_click(mouse_pos)
    
    def _handle_keydown(self, event, mouse_pos):
        """Handle keydown events.
        
        Args:
            event: Pygame event
            mouse_pos: Current mouse position
        """
        if event.key == pygame.K_ESCAPE:
            self.running = False
        
        elif event.key == pygame.K_SPACE:
            self.world.paused = not self.world.paused
            status = self.language.get('paused_msg') if self.world.paused else self.language.get('resumed')
            self.show_message(status)
        
        elif event.key == pygame.K_c:
            count = self.world.get_total_count()
            self.world.clear()
            self.show_message(f"{self.language.get('cleared')} {count} {self.language.get('agents')}")
        
        elif event.key == pygame.K_d:
            self.world.debug_mode = not self.world.debug_mode
            status = self.language.get('debug_on') if self.world.debug_mode else self.language.get('debug_off')
            self.show_message(status)
        
        elif event.key == pygame.K_h:
            self.config.enable_steering = not self.config.enable_steering
            status = self.language.get('hunting_on') if self.config.enable_steering else self.language.get('hunting_off')
            self.show_message(status)
        
        elif event.key == pygame.K_n:
            self.config.show_names = not self.config.show_names
            status = self.language.get('names_on_msg') if self.config.show_names else self.language.get('names_off_msg')
            self.show_message(status)
        
        elif event.key == pygame.K_l:
            # Toggle language
            new_lang = 'ro' if self.config.language == 'en' else 'en'
            self.config.language = new_lang
            self.language.set_language(new_lang)
            self.show_message(self.language.get('lang_changed'))
        
        elif event.key == pygame.K_F5:
            # Reset with new seed and spawn initial population
            import time
            new_seed = int(time.time() * 1000) % 1000000
            self.config.seed = new_seed
            self.world.reset()
            
            # Auto-spawn balanced population
            self.world.spawn_batch()
            
            self.show_message(f"{self.language.get('new_seed_msg')}: {new_seed} - {self.language.get('spawned_balanced')}")
        
        elif event.key == pygame.K_F9:
            if self.logger:
                spawn_file, collision_file = self.logger.export_csv()
                print(f"Exported to:\n  {spawn_file}\n  {collision_file}")
                self.show_message(self.language.get('exported'))
            else:
                self.show_message("Logging disabled")
        
        # Spawn at mouse position
        elif event.key == pygame.K_r:
            self.world.spawn('rock', mouse_pos)
            self.show_message(f"{self.language.get('spawned')} {self.language.get('rock')}")
        
        elif event.key == pygame.K_p:
            self.world.spawn('paper', mouse_pos)
            self.show_message(f"{self.language.get('spawned')} {self.language.get('paper')}")
        
        elif event.key == pygame.K_s:
            self.world.spawn('scissors', mouse_pos)
            self.show_message(f"{self.language.get('spawned')} {self.language.get('scissors')}")
        
        # Batch spawn
        elif event.key == pygame.K_1:
            count = len(self.world.spawn_random('rock', self.config.spawn_batch_size))
            self.show_message(f"{self.language.get('spawned')} {count} {self.language.get('rocks')}")
        
        elif event.key == pygame.K_2:
            count = len(self.world.spawn_random('paper', self.config.spawn_batch_size))
            self.show_message(f"{self.language.get('spawned')} {count} {self.language.get('papers')}")
        
        elif event.key == pygame.K_3:
            count = len(self.world.spawn_random('scissors', self.config.spawn_batch_size))
            self.show_message(f"{self.language.get('spawned')} {count} {self.language.get('scissors')}")
        
        # Random spawn with different counts per faction
        elif event.key == pygame.K_b:
            # Generate random counts for each faction (30-60 each)
            rock_count = self.world.rng.randint(30, 60)
            paper_count = self.world.rng.randint(30, 60)
            scissors_count = self.world.rng.randint(30, 60)
            
            r = len(self.world.spawn_random('rock', rock_count))
            p = len(self.world.spawn_random('paper', paper_count))
            s = len(self.world.spawn_random('scissors', scissors_count))
            
            self.show_message(f"{self.language.get('random_spawn_msg')}: {r} {self.language.get('rocks')}, {p} {self.language.get('papers')}, {s} {self.language.get('scissors')}")
    
    def _handle_mouse_click(self, pos):
        """Handle mouse click events.
        
        Args:
            pos: Mouse position (x, y)
        """
        # Could implement click-to-spawn here
        pass
    
    def show_message(self, text: str, duration: float = 2.0):
        """Show a temporary message on screen.
        
        Args:
            text: Message text
            duration: Duration in seconds
        """
        self.message = text
        self.message_timer = duration
    
    def update(self, dt: float):
        """Update game state.
        
        Args:
            dt: Time delta in seconds
        """
        # Process API spawn requests
        if self.spawn_queue:
            self._process_api_spawns()
        
        self.world.update(dt)
        
        # Update message timer
        if self.message_timer > 0:
            self.message_timer -= dt
            if self.message_timer <= 0:
                self.message = None
    
    def draw(self):
        """Draw the game."""
        # Clear screen
        self.screen.fill(self.config.background_color)
        
        # Draw world
        self.world.draw(self.screen)
        
        # Draw HUD
        fps = self.clock.get_fps()
        total_collisions = len(self.logger.collision_events) if self.logger else 0
        
        self.hud.draw(
            self.screen,
            self.world.get_counts(),
            total_collisions,
            fps,
            self.config.seed,
            self.world.paused,
            self.world.debug_mode,
            self.world.tick
        )
        
        # Draw victory screen if game over
        if self.world.game_over:
            scoreboard = self.world.get_scoreboard()
            self.victory_screen.draw(self.screen, self.world.winner_kind, scoreboard)
        
        # Draw message if active
        if self.message and not self.world.game_over:
            self.hud.draw_message(self.screen, self.message)
        
        # Update display
        pygame.display.flip()
    
    def _start_api_server(self):
        """Start the API server in a separate thread."""
        try:
            import api_server
            
            # Set the spawn queue in the API server
            api_server.set_spawn_queue(self.spawn_queue)
            
            # Start server in background thread
            self.api_thread = threading.Thread(
                target=api_server.run_server,
                kwargs={'host': '127.0.0.1', 'port': 5000, 'debug': False},
                daemon=True
            )
            self.api_thread.start()
            
            print("API server started on http://127.0.0.1:5000")
            print("Spawn endpoint: POST http://127.0.0.1:5000/api/spawn")
            self.show_message("API server started on port 5000")
            
        except ImportError:
            print("Warning: Flask not installed. API server disabled.")
            print("Install with: pip install -r requirements_api.txt")
            self.api_enabled = False
            self.spawn_queue = None
    
    def _process_api_spawns(self):
        """Process pending spawn requests from the API."""
        requests = self.spawn_queue.get_all()
        
        for spawn_request in requests:
            # Spawn the agent
            agent = self.world.spawn(
                spawn_request.agent_type,
                (spawn_request.x, spawn_request.y)
            )
            
            if agent:
                # Success - agent spawned
                pass
            else:
                # Failed - probably hit population cap
                # The API will handle this on next request
                pass
    
    def run(self):
        """Main game loop."""
        while self.running:
            # Handle events
            self.handle_events()
            
            # Update
            dt = self.clock.tick(self.config.fps) / 1000.0
            self.update(dt)
            
            # Draw
            self.draw()
        
        # Cleanup
        pygame.quit()
        sys.exit(0)


def main():
    """Entry point for the application."""
    # Parse command line arguments if needed
    import argparse
    
    parser = argparse.ArgumentParser(description="Rock-Paper-Scissors World")
    parser.add_argument('--seed', type=int, help='Random seed')
    parser.add_argument('--width', type=int, default=1200, help='Screen width')
    parser.add_argument('--height', type=int, default=800, help='Screen height')
    parser.add_argument('--fps', type=int, default=60, help='Target FPS')
    parser.add_argument('--no-log', action='store_true', help='Disable event logging')
    parser.add_argument('--api-enabled', action='store_true', help='Enable API server for external spawning')
    
    args = parser.parse_args()
    
    # Create config
    config = Config(
        screen_width=args.width,
        screen_height=args.height,
        fps=args.fps,
        seed=args.seed,
        log_events=not args.no_log
    )
    
    # Create and run app
    app = RPSApp(config, api_enabled=args.api_enabled)
    app.run()


if __name__ == '__main__':
    main()

