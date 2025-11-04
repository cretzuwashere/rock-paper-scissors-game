# Lumea Piatră–Hârtie–Foarfece

O aplicație Python cu interfață grafică care simulează o lume Piatră–Hârtie–Foarfece unde obiectele se mișcă și interacționează conform regulilor clasice ale jocului.

> **Nou aici?** Verifică **[START_HERE.md](START_HERE.md)** pentru un ghid rapid în 3 pași! 🚀

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

## Instalare

```bash
pip install -r requirements.txt
```

## Rulare Aplicație

```bash
python -m rps.app
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


