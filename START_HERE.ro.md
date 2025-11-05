# 🎮 Lumea RPS - ÎNCEPE AICI

Bine ai venit la **Lumea Piatră-Hârtie-Foarfece**! Acest fișier te va ajuta să pornești în mai puțin de 5 minute.

## 🚀 Trei Pași pentru a Începe

### Pasul 1: Instalează Dependențele (1 minut)

**Windows**: Dublu-click pe `install.bat`

**Mac/Linux**:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Pasul 2: Rulează Aplicația (30 secunde)

**Windows**: Dublu-click pe `run.bat`

**Mac/Linux**:
```bash
python run.py
```

### Pasul 3: Creează Câțiva Agenți! (1 minut)

Apasă aceste taste:
- `1` - Creează 10 Pietre (gri)
- `2` - Creează 10 Hârtii (galben)
- `3` - Creează 10 Foarfece (roșu)

**Urmărește-i cum interacționează!** Când se ciocnesc:
- Piatra bate Foarfecele
- Hârtia bate Piatra
- Foarfecele bat Hârtia

Cel învins dispare! 💥

## 🎯 Comenzi Rapide

| Tastă | Ce Face |
|-------|---------|
| `1`, `2`, `3` | Creează 10 agenți aleatoriu |
| `R`, `P`, `S` | Creează la poziția cursorului |
| `B` | Creare aleatorie (30-60 din fiecare) |
| `Space` | Pauză/Reluare |
| `L` | Comută limba (Engleză ↔ Română) |
| `C` | Șterge toți agenții |
| `ESC` | Ieșire |

## 📖 Învață Mai Mult

Vrei să aprofundezi? Verifică:

1. **[QUICKSTART.ro.md](QUICKSTART.ro.md)** - Început rapid detaliat cu depanare
2. **[VISUAL_GUIDE.md](VISUAL_GUIDE.md)** - Vezi cum arată totul
3. **[USAGE_EXAMPLES.md](USAGE_EXAMPLES.md)** - Experimente interesante de încercat
4. **[INDEX.md](INDEX.md)** - Ghid complet de documentație

## 🎨 Ce Vei Vedea

```
┌─────────────────────────────────────┐
│ Lumea RPS              DEBUG        │
│ Piatră: 15    (gri)                 │
│ Hârtie: 12    (galben)              │
│ Foarfece: 8   (roșu)                │
│ Total: 35                           │
│ Coliziuni: 47                       │
│ FPS: 60.0                           │
│ ┌─────────────────────────────────┐ │
│ │                                 │ │
│ │   ●  Piatră                     │ │
│ │        ▭  Hârtie                │ │
│ │            ✂ Foarfece           │ │
│ │                                 │ │
│ │  [Agenții se mișcă și ciocnesc] │ │
│ │                                 │ │
│ │ └─────────────────────────────┘ │ │
│                                     │
│ Comenzi: R/P/S=Creează | Space=Pauză│
└─────────────────────────────────────┘
```

## 💡 Lucruri Interesante de Încercat

### Experimentul 1: Start Echilibrat
```
Apasă: 1, 2, 3
Urmărește: Ce tip supraviețuiește?
```

### Experimentul 2: Plasare Manuală
```
Mută mouse-ul într-un colț
Apasă: R (creează Piatră)
Mută în colțul opus
Apasă: S (creează Foarfece)
Urmărește-i cum se întâlnesc!
```

### Experimentul 3: Exportă Date
```
Apasă: 1, 2, 3 (creează agenți)
Așteaptă: Lasă-i să interacționeze
Apasă: F9 (exportă date)
Verifică: folderul analysis_output/ pentru fișiere CSV
```

## 🐛 Depanare

**Nu se întâmplă nimic?**
- Asigură-te că ai instalat pygame: `pip install pygame`
- Verifică versiunea Python: `python --version` (necesită 3.10+)

**Fereastra se închide imediat?**
- Rulează din terminal pentru a vedea erorile
- Încearcă: `python run.py` în loc de dublu-click

**Prea încet?**
- Apasă `C` pentru a șterge agenții
- Creează mai puțini deodată

## 📚 Documentație Completă

Acest proiect are **documentație extinsă**:

- **11+ fișiere de documentație**
- **2,500+ linii de ghiduri**
- **Tutoriale pas-cu-pas**
- **Diagrame de arhitectură**
- **Exemple de utilizare**

Începe cu **[INDEX.md](INDEX.md)** pentru a naviga totul!

## 🎓 Ce Include Acest Proiect

✅ Aplicație completă funcțională  
✅ Interfață grafică frumoasă  
✅ Reguli clasice de joc P-H-F  
✅ Analiză și export de date  
✅ Suite cuprinzătoare de teste (38 teste)  
✅ Documentație extinsă (11+ fișiere)  
✅ Cross-platform (Windows/Mac/Linux)  
✅ Calitate profesională a codului  

## 🚀 Gata să Începi?

1. Rulează: `python run.py` (sau `run.bat` pe Windows)
2. Apasă: `1`, `2`, `3` pentru a crea agenți
3. Bucură-te: Urmărește lumea Piatră-Hârtie-Foarfece evoluând!

---

**Întrebări?** Verifică **[INDEX.md](INDEX.md)** pentru toată documentația!

**Distrează-te!** 🎮🪨📄✂️

