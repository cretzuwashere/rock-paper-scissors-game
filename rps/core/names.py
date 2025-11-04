"""Name generation for agents."""

import random

# Name lists for each agent type
ROCK_NAMES = [
    "Boulder", "Granite", "Obsidian", "Flint", "Slate", "Marble", "Basalt", "Quartz",
    "Pebble", "Stone", "Cliff", "Rocky", "Crusher", "Titan", "Golem", "Brick",
    "Cobble", "Gravel", "Shale", "Pumice", "Onyx", "Jade", "Ruby", "Diamond",
    "Emerald", "Topaz", "Opal", "Amber", "Crystal", "Gem", "Spike", "Crag",
    "Mesa", "Canyon", "Ridge", "Peak", "Summit", "Monolith", "Megalith", "Dolmen"
]

PAPER_NAMES = [
    "Scroll", "Parchment", "Manuscript", "Document", "Letter", "Note", "Page", "Sheet",
    "Papyrus", "Vellum", "Folio", "Leaflet", "Pamphlet", "Flyer", "Poster", "Banner",
    "Card", "Ticket", "Receipt", "Invoice", "Contract", "Treaty", "Charter", "Deed",
    "Certificate", "Diploma", "License", "Permit", "Warrant", "Writ", "Summons", "Subpoena",
    "Origami", "Confetti", "Tissue", "Napkin", "Towel", "Wrapper", "Envelope", "Label"
]

SCISSORS_NAMES = [
    "Blade", "Shear", "Clipper", "Cutter", "Slicer", "Snipper", "Trimmer", "Razor",
    "Knife", "Dagger", "Sword", "Saber", "Scimitar", "Katana", "Rapier", "Cutlass",
    "Machete", "Cleaver", "Scalpel", "Shiv", "Stiletto", "Dirk", "Tanto", "Wakizashi",
    "Excalibur", "Masamune", "Kusanagi", "Durandal", "Joyeuse", "Tyrfing", "Gram", "Naegling",
    "Snip", "Slash", "Cut", "Chop", "Slice", "Dice", "Mince", "Julienne"
]


class NameGenerator:
    """Generates unique names for agents."""
    
    def __init__(self, seed: int = None):
        """Initialize the name generator.
        
        Args:
            seed: Random seed for reproducibility
        """
        self.rng = random.Random(seed)
        self.used_names = {
            'rock': set(),
            'paper': set(),
            'scissors': set()
        }
    
    def generate_name(self, kind: str) -> str:
        """Generate a unique name for an agent.
        
        Args:
            kind: Agent type ('rock', 'paper', or 'scissors')
            
        Returns:
            Unique name string
        """
        if kind == 'rock':
            name_list = ROCK_NAMES
        elif kind == 'paper':
            name_list = PAPER_NAMES
        elif kind == 'scissors':
            name_list = SCISSORS_NAMES
        else:
            return f"Agent-{self.rng.randint(1000, 9999)}"
        
        # Get available names
        available = [name for name in name_list if name not in self.used_names[kind]]
        
        # If all names used, add numbers
        if not available:
            base_name = self.rng.choice(name_list)
            counter = 2
            while f"{base_name}-{counter}" in self.used_names[kind]:
                counter += 1
            name = f"{base_name}-{counter}"
        else:
            name = self.rng.choice(available)
        
        self.used_names[kind].add(name)
        return name
    
    def release_name(self, kind: str, name: str):
        """Release a name back to the pool.
        
        Args:
            kind: Agent type
            name: Name to release
        """
        self.used_names[kind].discard(name)
    
    def reset(self):
        """Reset all used names."""
        for kind in self.used_names:
            self.used_names[kind].clear()

