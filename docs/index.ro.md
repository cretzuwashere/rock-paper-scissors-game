# 🪨 Lumea Piatră–Hârtie–Foarfece

Bine ai venit la **Lumea Piatră–Hârtie–Foarfece** - o simulare interactivă construită cu **Python & Pygame** 🎮

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![License](https://img.shields.io/badge/license-MIT-lightgrey)
![Pygame](https://img.shields.io/badge/Pygame-2.5.0+-orange)

**[English Version](index.md)** | **Versiune Română**

## 🎮 Despre

O simulare dinamică unde agenți autonomi (Piatră, Hârtie, Foarfece) se mișcă, vânează și luptă în timp real. Urmărește cum populațiile cresc și scad, cu ecrane de victorie celebrând campionii!

### ✨ Caracteristici Principale

- **Agenți cu Nume** - Fiecare agent are o identitate unică (Boulder, Scroll, Blade, etc.)
- **Urmărire Eliminări** - Clasamente cu medalii de aur/argint/bronz
- **Vânătoare Globală** - Prădătorii vânează prada pe întreaga hartă
- **Detectare Victorie** - Game-over automat când o facțiune domină
- **Multilingv** - Comută între Engleză și Română
- **Statistici Live** - HUD arătând populația și starea jocului în timp real

## 🚀 Joacă Local

### Pasul 0: Instalează Python (dacă nu îl ai)

**Windows:**
1. Descarcă Python de la [python.org/downloads](https://www.python.org/downloads/)
2. Rulează installerul
3. ✅ **IMPORTANT:** Bifează "Add Python to PATH" în timpul instalării
4. Click pe "Install Now"
5. Verifică: Deschide Command Prompt și scrie `python --version`

### Pasul 1: Descarcă Jocul

**Opțiunea A: Folosind Git** (dacă îl ai)
```bash
git clone https://github.com/cretzuwashere/rock-paper-scissors-game.git
cd rock-paper-scissors-game
```

**Opțiunea B: Descărcare Directă** (mai ușor pentru începători)
1. Mergi la [github.com/cretzuwashere/rock-paper-scissors-game](https://github.com/cretzuwashere/rock-paper-scissors-game)
2. Click pe butonul verde **"Code"**
3. Click pe **"Download ZIP"**
4. Extrage fișierul ZIP
5. Deschide Command Prompt în acel folder (Shift + Click-dreapta → "Open PowerShell window here")

### Pasul 2: Instalează Dependențele

```bash
pip install -r requirements.txt
```

### Pasul 3: Rulează Jocul!

```bash
python -m rps.app
```

**Comenzi Rapide:**
- Apasă `B` pentru a crea o bătălie
- Apasă `Space` pentru pauză
- Apasă `L` pentru a schimba limba (Engleză/Română)

## 🎯 Reguli de Joc

- **Piatra** 🪨 bate **Foarfecele** ✂️
- **Foarfecele** ✂️ bat **Hârtia** 📄
- **Hârtia** 📄 bate **Piatra** 🪨

Agenții vânează activ prada pe întreaga tablă. Când se ciocnesc, cel învins este eliminat și câștigătorul continuă!

## 🎮 Comenzi

### Creare
- `R` / `P` / `S` - Creează la poziția mouse-ului
- `1` / `2` / `3` - Creează 10 agenți aleatoriu
- `B` - Creare aleatorie (30-60 din fiecare facțiune)

### Control Joc
- `Space` - Pauză/Reluare
- `H` - Comută comportament vânătoare
- `N` - Comută afișare nume
- `C` - Șterge tot și resetează
- `F5` - Seed aleatoriu nou + creare automată
- `L` - Comută limba (EN/RO)

## 🛠️ Tehnologii

- **Python 3.10+** - Limbaj principal
- **Pygame 2.5+** - Grafică și bucla de joc
- **NumPy** - Calcule eficiente
- **Test-Driven Development** - Suite cuprinzătoare de teste

## 📚 Documentație

- [Ghid de Referință Rapidă](https://github.com/cretzuwashere/rock-paper-scissors-game/blob/master/QUICK_REFERENCE.md)
- [Instrucțiuni de Instalare](https://github.com/cretzuwashere/rock-paper-scissors-game/blob/master/SETUP.md)
- [Plan de Dezvoltare](https://github.com/cretzuwashere/rock-paper-scissors-game/blob/master/RPS-plan.txt)
- [Exemple de Utilizare](https://github.com/cretzuwashere/rock-paper-scissors-game/blob/master/USAGE_EXAMPLES.md)

## 🤝 Contribuții

Pull request-urile și ideile sunt întotdeauna binevenite! Proiectul urmează principiile TDD - toate componentele principale au teste unitare.

```bash
# Rulează testele
python run_tests.py
```

## 📄 Licență

Acest proiect este licențiat sub **Licența MIT** - vezi [LICENSE](https://github.com/cretzuwashere/rock-paper-scissors-game/blob/master/LICENSE) pentru detalii.

---

**Creat cu ❤️ de [@cretzuwashere](https://github.com/cretzuwashere)**

