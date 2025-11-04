"""Language support for the game."""

from typing import Dict, Any


class Language:
    """Language manager for UI text."""
    
    # Available languages
    ENGLISH = 'en'
    ROMANIAN = 'ro'
    
    def __init__(self, lang: str = ENGLISH):
        """Initialize language manager.
        
        Args:
            lang: Language code ('en' or 'ro')
        """
        self.current_lang = lang
        self._translations = {
            'en': self._english(),
            'ro': self._romanian()
        }
    
    def get(self, key: str) -> str:
        """Get translated text.
        
        Args:
            key: Translation key
            
        Returns:
            Translated string
        """
        return self._translations[self.current_lang].get(key, key)
    
    def set_language(self, lang: str):
        """Change current language.
        
        Args:
            lang: Language code ('en' or 'ro')
        """
        if lang in self._translations:
            self.current_lang = lang
    
    @staticmethod
    def _english() -> Dict[str, str]:
        """English translations."""
        return {
            # Agent types
            'rock': 'Rock',
            'paper': 'Paper',
            'scissors': 'Scissors',
            'rocks': 'Rocks',
            'papers': 'Papers',
            
            # HUD
            'total': 'Total',
            'collisions': 'Collisions',
            'seed': 'Seed',
            'paused': 'PAUSED',
            'debug': 'DEBUG',
            'hunt_on': 'HUNT ON',
            'hunt_off': 'HUNT OFF',
            'names_on': 'NAMES ON',
            'names_off': 'NAMES OFF',
            
            # Controls
            'controls': 'Controls',
            'spawn_at_mouse': 'Spawn at mouse',
            'batch_spawn': 'Batch spawn',
            'random_spawn': 'Random Spawn',
            'pause': 'Pause',
            'toggle_hunt': 'Toggle Hunt',
            'toggle_names': 'Toggle Names',
            'clear': 'Clear',
            'debug_mode': 'Debug',
            'export_csv': 'Export CSV',
            'new_seed': 'New seed+spawn',
            'quit': 'Quit',
            
            # Messages
            'spawned': 'Spawned',
            'cleared': 'Cleared',
            'agents': 'agents',
            'paused_msg': 'Paused',
            'resumed': 'Resumed',
            'debug_on': 'Debug mode: ON',
            'debug_off': 'Debug mode: OFF',
            'hunting_on': 'Hunting: ON',
            'hunting_off': 'Hunting: OFF',
            'names_on_msg': 'Names: ON',
            'names_off_msg': 'Names: OFF',
            'exported': 'Analysis exported!',
            'new_seed_msg': 'New seed',
            'spawned_balanced': 'Spawned balanced population',
            'random_spawn_msg': 'Random Spawn',
            
            # Victory screen
            'win': 'WIN!',
            'scoreboard': 'SCOREBOARD - Top Killers',
            'kills': 'kills',
            'kill': 'kill',
            'and_more': '... and',
            'more': 'more',
            'total_count': 'Total',
            'press_c': 'Press C to clear and start new game',
            
            # Language toggle
            'language': 'Language: English',
            'lang_changed': 'Language changed to English',
            
            # Control hints
            'controls_line1': 'Controls: R/P/S=Spawn at mouse | 1/2/3=Batch spawn | B=Random Spawn | Space=Pause',
            'controls_line2': 'H=Toggle Hunt | N=Toggle Names | L=Language | C=Clear | D=Debug | F9=Export CSV | F5=New seed+spawn | ESC=Quit',
        }
    
    @staticmethod
    def _romanian() -> Dict[str, str]:
        """Romanian translations."""
        return {
            # Agent types
            'rock': 'Piatră',
            'paper': 'Hârtie',
            'scissors': 'Foarfece',
            'rocks': 'Pietre',
            'papers': 'Hârtii',
            
            # HUD
            'total': 'Total',
            'collisions': 'Coliziuni',
            'seed': 'Seed',
            'paused': 'PAUZĂ',
            'debug': 'DEBUG',
            'hunt_on': 'VÂNĂTOARE ACTIVĂ',
            'hunt_off': 'VÂNĂTOARE OPRITĂ',
            'names_on': 'NUME ACTIVE',
            'names_off': 'NUME OPRITE',
            
            # Controls
            'controls': 'Comenzi',
            'spawn_at_mouse': 'Creare la mouse',
            'batch_spawn': 'Creare în lot',
            'random_spawn': 'Creare Aleatorie',
            'pause': 'Pauză',
            'toggle_hunt': 'Comută Vânătoare',
            'toggle_names': 'Comută Nume',
            'clear': 'Șterge',
            'debug_mode': 'Debug',
            'export_csv': 'Exportă CSV',
            'new_seed': 'Seed nou+creare',
            'quit': 'Ieșire',
            
            # Messages
            'spawned': 'Creat',
            'cleared': 'Șters',
            'agents': 'agenți',
            'paused_msg': 'Pauză',
            'resumed': 'Reluat',
            'debug_on': 'Mod debug: ACTIV',
            'debug_off': 'Mod debug: OPRIT',
            'hunting_on': 'Vânătoare: ACTIVĂ',
            'hunting_off': 'Vânătoare: OPRITĂ',
            'names_on_msg': 'Nume: ACTIVE',
            'names_off_msg': 'Nume: OPRITE',
            'exported': 'Analiză exportată!',
            'new_seed_msg': 'Seed nou',
            'spawned_balanced': 'Populație echilibrată creată',
            'random_spawn_msg': 'Creare Aleatorie',
            
            # Victory screen
            'win': 'CÂȘTIGĂ!',
            'scoreboard': 'CLASAMENT - Cei Mai Buni',
            'kills': 'eliminări',
            'kill': 'eliminare',
            'and_more': '... și încă',
            'more': 'mai mult',
            'total_count': 'Total',
            'press_c': 'Apasă C pentru a șterge și începe un joc nou',
            
            # Language toggle
            'language': 'Limbă: Română',
            'lang_changed': 'Limba schimbată în Română',
            
            # Control hints
            'controls_line1': 'Comenzi: R/P/S=Creare la mouse | 1/2/3=Creare lot | B=Creare Aleatorie | Space=Pauză',
            'controls_line2': 'H=Comută Vânătoare | N=Comută Nume | L=Limbă | C=Șterge | D=Debug | F9=Export CSV | F5=Seed nou+creare | ESC=Ieșire',
        }

