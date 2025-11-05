# 🪨 Lumea Piatră–Hârtie–Foarfece ✂️

![Python CI](https://github.com/cretzuwashere/rock-paper-scissors-game/workflows/Python%20CI/badge.svg)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![License](https://img.shields.io/badge/license-MIT-lightgrey)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-green)
![Pygame](https://img.shields.io/badge/Pygame-2.5.0+-orange)

O aplicație Python cu interfață grafică care simulează o lume Piatră–Hârtie–Foarfece unde agenții se mișcă, vânează și interacționează conform regulilor clasice ale jocului.

> **Nou aici?** Verifică **[QUICKSTART.ro.md](QUICKSTART.ro.md)** pentru un ghid rapid în 3 pași! 🚀
> 
> **English?** See **[README.md](README.md)** for the English version! 🇬🇧
>
> **Demo Live:** [GitHub Pages](https://cretzuwashere.github.io/rock-paper-scissors-game/)

## Caracteristici

- Trei tipuri de obiecte (Piatră, Hârtie, Foarfece) care se mișcă liber pe ecran
- **Agenți cu nume** - Fiecare agent are un nume unic (Boulder, Scroll, Blade, etc.) 🏷️
- **Urmărire eliminări** - Agenții urmăresc eliminările lor pentru clasamente 🏆
- **Detectare victorie** - Jocul detectează automat când o facțiune câștigă! 🎉
- **Clasament** - Ecran frumos de victorie arătând cei mai buni eliminatori cu ranguri aur/argint/bronz
- **Vânătoare globală** - Agenții vânează prada pe întreaga tablă (fără limită de rază) 🎯
- **Pradă inconștientă** - Prada acționează fără să fie conștientă de pericol (fără comportament de fugă) 😴
- **Pattern Factory** - Sistem curat și extensibil de creare agenți
- **Creare aleatorie** - Apasă `B` pentru numere aleatorii din fiecare facțiune (30-60 fiecare)
- **Suport multilingv** - Comută între Engleză și Română cu tasta `L` 🌍
- Interacțiuni bazate pe coliziuni urmând regulile clasice P-H-F
- Vizualizare în timp real cu Pygame
- Mod de vânătoare comutabil (apasă `H`)
- Analiză și înregistrare interacțiuni
- Creează obiecte manual sau în loturi

## 🚀 Început Rapid

### Pentru Începători Completi (Windows) - METODA CEA MAI UȘOARĂ

**Nu ai Python instalat?**
1. Descarcă de la [python.org/downloads](https://www.python.org/downloads/)
2. Rulează installerul, ✅ bifează "Add Python to PATH"
3. Repornește calculatorul

**Descarcă & Joacă:**
1. Click pe butonul verde **"Code"** de mai sus → **"Download ZIP"**
2. Extrage fișierul ZIP pe Desktop
3. **Dublu-click pe `install.bat`** ← Acesta instalează tot!
4. **Dublu-click pe `run.bat`** ← Acesta pornește jocul!

**Asta e tot!** Apasă `B` pentru o bătălie! 🎮

---

### Metodă Alternativă (Orice SO)

```bash
# Dacă ai clonat cu Git sau fișierele .bat nu funcționează:
pip install -r requirements.txt
python run.py
```

---

### Pentru Programatori

```bash
# Clonează repository-ul
git clone https://github.com/cretzuwashere/rock-paper-scissors-game.git
cd rock-paper-scissors-game

# Opțiunea 1: Folosește scripturile furnizate
./install.bat    # Windows
python run.py

# Opțiunea 2: Configurare manuală cu mediu virtual
python -m venv venv
source venv/bin/activate   # Pe Windows: venv\Scripts\activate
pip install -r requirements.txt
python -m rps.app

# Opțiunea 3: Instalează ca pachet
pip install -e .
rps-world
```

## Comenzi

### Creare
- `R` - Creează Piatră la poziția mouse-ului
- `P` - Creează Hârtie la poziția mouse-ului
- `S` - Creează Foarfece la poziția mouse-ului
- `1` - Creează 10 Pietre aleatoriu
- `2` - Creează 10 Hârtii aleatoriu
- `3` - Creează 10 Foarfece aleatoriu
- `B` - Creare aleatorie (30-60 din fiecare facțiune) ⭐ NOU!

### Control Joc
- `Space` - Pauză/Reluare
- `H` - Comută comportament vânătoare
- `N` - Comută afișare nume (arată/ascunde nume agenți)
- `L` - Comută limbă (Engleză ↔ Română) ⭐ NOU!
- `C` - Șterge toate obiectele (resetează și ecranul de victorie)
- `D` - Comută modul debug
- `F5` - Seed aleatoriu nou + creare automată populație echilibrată
- `ESC` - Ieșire

### Analiză
- `F9` - Exportă analiză în CSV

## Reguli Joc

- Piatra bate Foarfecele (și le vânează global!)
- Hârtia bate Piatra (și o vânează global!)
- Foarfecele bat Hârtia (și o vânează global!)
- Când obiectele se ciocnesc, cel învins dispare și câștigătorul continuă
- **Agenții vânează prada pe întreaga tablă** (detectare globală)
- **Prada acționează inconștient** - fără comportament de fugă, inconștientă de pericol
- **Victorie** - Când rămâne doar o facțiune, jocul arată clasament cu cei mai buni eliminatori
- Fiecare agent urmărește eliminările și are un nume unic (ex. "Boulder", "Scroll", "Blade")

## Documentație

- **`QUICK_REFERENCE.md`** - Ghid de referință rapidă cu toate comenzile și caracteristicile ⭐
- **`RPS-plan.txt`** - Plan complet de dezvoltare și detalii arhitectură
- **`SETUP.md`** - Instrucțiuni detaliate de instalare și configurare
- **`USAGE_EXAMPLES.md`** - Exemple de utilizare și scenarii experimentale

## Status Implementare

✅ Implementare completă cu:
- Clasă de bază Agent cu subclase Rock/Paper/Scissors
- Simulare fizică (mișcare, limite wrap/bounce)
- Detectare și rezolvare coliziuni
- Orchestrare și management stare lume
- Overlay HUD cu statistici în timp real
- Înregistrare evenimente și export CSV pentru analiză
- Grafică sprite îmbunătățită pentru fiecare tip de agent
- Suite cuprinzătoare de teste
- Interfață linie de comandă cu opțiuni
- Reproducere deterministă prin control seed
- **Suport multilingv (Engleză/Română)**

## Dezvoltare

Proiectul urmează principiile Test-Driven Development. Toate componentele principale au teste unitare.

Rulează testele cu:
```bash
python run_tests.py
```

## Îmbunătățiri Viitoare

Extensii potențiale conform planului de dezvoltare:
- Grilă hash spațială pentru optimizare performanță cu populații mari
- Efecte sonore pentru coliziuni
- Panou UI setări
- Vizualizări heatmap
- Obstacole și pereți
- Replay/înregistrare video
- Încărcător fișiere scenarii (format JSON)


