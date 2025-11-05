# Ghid de Început Rapid

Pornește cu Lumea RPS în 3 pași!

## Pasul 1: Instalează Dependențele

### Windows
Dublu-click pe `install.bat` sau rulează în terminal:
```cmd
install.bat
```

### Linux/Mac
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Pasul 2: Rulează Aplicația

### Windows
Dublu-click pe `run.bat` sau:
```cmd
python run.py
```

### Linux/Mac
```bash
python3 run.py
```

## Pasul 3: Creează Câțiva Agenți!

Odată ce fereastra se deschide:
1. Apasă `1` pentru a crea 10 Pietre
2. Apasă `2` pentru a crea 10 Hârtii
3. Apasă `3` pentru a crea 10 Foarfece
4. Urmărește-i cum interacționează!

## Comenzi Esențiale

| Tastă | Acțiune |
|-------|---------|
| `1`, `2`, `3` | Creează 10 agenți aleatoriu |
| `R`, `P`, `S` | Creează la poziția mouse-ului |
| `B` | Creare aleatorie (30-60 din fiecare) |
| `Space` | Pauză/Reluare |
| `L` | Comută limba (Engleză ↔ Română) |
| `C` | Șterge ecranul |
| `ESC` | Ieșire |

## Ce Vei Vedea

- **Sprite-uri gri** = Pietre (bat Foarfecele)
- **Sprite-uri galbene** = Hârtii (bat Piatra)
- **Sprite-uri roșii** = Foarfece (bat Hârtia)

Când agenții se ciocnesc, cel învins dispare!

## Următorii Pași

- Apasă `D` pentru modul debug (vezi razele de coliziune)
- Apasă `F9` pentru a exporta datele de analiză
- Apasă `F5` pentru a reseta cu seed aleatoriu nou
- Citește `USAGE_EXAMPLES.md` pentru idei de experimente
- Verifică `SETUP.md` pentru configurare avansată

## Depanare

**Nu apare nicio fereastră?**
- Asigură-te că pygame este instalat: `pip install pygame`
- Verifică că Python 3.10+ este instalat: `python --version`

**Aplicația este lentă?**
- Apasă `C` pentru a șterge agenții
- Reduce numărul de creări (apasă `1`/`2`/`3` mai puține ori)

**Ai nevoie de ajutor?**
- Vezi `README.ro.md` pentru documentație completă
- Verifică `SETUP.md` pentru instrucțiuni detaliate

---

**Distrează-te urmărind lumea Piatră-Hârtie-Foarfece evoluând!** 🎮

