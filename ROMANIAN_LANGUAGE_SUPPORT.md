# Romanian Language Support / Suport Limbă Română

## Overview / Prezentare Generală

The RPS World game now supports both English and Romanian languages! Toggle between them instantly with the `L` key.

Jocul RPS World suportă acum atât limba engleză cât și română! Comută între ele instant cu tasta `L`.

---

## Features / Caracteristici

### English
- **Complete UI translation** - All interface elements in Romanian
- **Instant switching** - Press `L` to toggle languages
- **Persistent** - Language preference maintained during session
- **Comprehensive** - HUD, victory screen, messages, all translated

### Română
- **Traducere completă UI** - Toate elementele interfeței în română
- **Comutare instantă** - Apasă `L` pentru a schimba limba
- **Persistentă** - Preferința de limbă menținută în sesiune
- **Cuprinzătoare** - HUD, ecran victorie, mesaje, toate traduse

---

## How to Use / Cum se Folosește

### Toggle Language / Comută Limba
```
Press L key / Apasă tasta L
English ↔ Română
```

### What Gets Translated / Ce se Traduce

#### HUD Elements / Elemente HUD
- Agent type names (Rock → Piatră, Paper → Hârtie, Scissors → Foarfece)
- Statistics labels (Total, Collisions → Coliziuni, Seed)
- Status indicators (PAUSED → PAUZĂ, DEBUG, HUNT ON → VÂNĂTOARE ACTIVĂ)
- Language indicator (Language: English → Limbă: Română)

#### Victory Screen / Ecran Victorie
- Winner announcement (ROCKS WIN! → PIETRE CÂȘTIGĂ!)
- Scoreboard title (SCOREBOARD - Top Killers → CLASAMENT - Cei Mai Buni)
- Kill counts (kills → eliminări, kill → eliminare)
- Instructions (Press C to clear... → Apasă C pentru a șterge...)

#### Messages / Mesaje
- Spawn messages (Spawned → Creat)
- Status changes (Paused → Pauză, Resumed → Reluat)
- Mode toggles (Hunting: ON → Vânătoare: ACTIVĂ)
- Export confirmations (Analysis exported! → Analiză exportată!)

---

## Implementation / Implementare

### New Files / Fișiere Noi
- `rps/core/language.py` - Language management system
- `README.ro.md` - Romanian README

### Modified Files / Fișiere Modificate
- `rps/core/config.py` - Added language config option
- `rps/app.py` - Integrated language system, added L key handler
- `rps/ui/hud.py` - All text uses translations
- `rps/ui/victory_screen.py` - Victory text translated
- `README.md` - Added Romanian link
- `INDEX.md` - Added Romanian documentation links
- `QUICK_REFERENCE.md` - Added language toggle info

### Translation Coverage / Acoperire Traduceri

**100% Coverage:**
- ✅ Agent types (Rock, Paper, Scissors)
- ✅ HUD statistics
- ✅ Status indicators
- ✅ Victory screen
- ✅ All user messages
- ✅ Control hints

---

## Examples / Exemple

### English UI
```
Rock: 15
Paper: 0
Scissors: 0
Total: 15

HUNT ON
NAMES OFF
Language: English

ROCKS WIN!
SCOREBOARD - Top Killers
#1 Boulder    12 kills
```

### Romanian UI / Interfață Română
```
Piatră: 15
Hârtie: 0
Foarfece: 0
Total: 15

VÂNĂTOARE ACTIVĂ
NUME OPRITE
Limbă: Română

PIETRE CÂȘTIGĂ!
CLASAMENT - Cei Mai Buni
#1 Boulder    12 eliminări
```

---

## Technical Details / Detalii Tehnice

### Language Class / Clasa Language
```python
from rps.core.language import Language

# Initialize
lang = Language('ro')  # or 'en'

# Get translation
text = lang.get('rock')  # Returns "Piatră" in Romanian

# Switch language
lang.set_language('en')  # Switch to English
```

### Supported Languages / Limbi Suportate
- `en` - English
- `ro` - Romanian (Română)

### Adding More Languages / Adăugare Limbi Noi
To add a new language, edit `rps/core/language.py`:
1. Add a new method like `_french()` or `_german()`
2. Return a dictionary with all translation keys
3. Add to `self._translations` in `__init__`

Pentru a adăuga o limbă nouă, editează `rps/core/language.py`:
1. Adaugă o metodă nouă precum `_french()` sau `_german()`
2. Returnează un dicționar cu toate cheile de traducere
3. Adaugă la `self._translations` în `__init__`

---

## Controls / Comenzi

| Key / Tastă | Action / Acțiune |
|-------------|------------------|
| **L** | Toggle language (EN ↔ RO) / Comută limba (EN ↔ RO) |

---

## Testing / Testare

All tests pass with language support:
```bash
python run_tests.py
# Ran 38 tests in 0.352s
# OK
```

Toate testele trec cu suport pentru limbi:
```bash
python run_tests.py
# Ran 38 tests in 0.352s
# OK
```

---

## Future Enhancements / Îmbunătățiri Viitoare

Potential additions / Adăugări potențiale:
- More languages (French, German, Spanish, etc.)
- Persistent language preference (save to config file)
- Command-line argument to set default language
- Localized agent names (optional)

Mai multe limbi (Franceză, Germană, Spaniolă, etc.)
- Preferință de limbă persistentă (salvare în fișier config)
- Argument linie de comandă pentru setare limbă implicită
- Nume agenți localizate (opțional)

---

## Summary / Rezumat

✅ **Complete bilingual support** - English and Romanian
✅ **Instant switching** - Press L to toggle
✅ **All UI elements** - HUD, victory screen, messages
✅ **Easy to extend** - Add more languages easily
✅ **Fully tested** - All tests passing

✅ **Suport bilingv complet** - Engleză și Română
✅ **Comutare instantă** - Apasă L pentru a schimba
✅ **Toate elementele UI** - HUD, ecran victorie, mesaje
✅ **Ușor de extins** - Adaugă mai multe limbi ușor
✅ **Complet testat** - Toate testele trec

**Enjoy the game in your language! / Bucură-te de joc în limba ta!** 🎮🌍

