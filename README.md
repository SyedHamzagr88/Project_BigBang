# 📡 Project BIGBANG — Morse Code Translator

A desktop app that converts text to Morse code and back — and actually plays the dots and dashes as real beep sounds.

Built as my first independent Python project after finishing core Python fundamentals.

---

## ✨ Features

- **Text → Morse** — type any sentence, get instant Morse code output
- **Morse → Text** — paste Morse code, decode it back to plain English
- **Live sound playback** — hear the actual beep pattern (short beep = dot, long beep = dash)
- Clean dark-themed desktop GUI

---

## 🛠️ Built With

- **Python 3**
- **Tkinter** — GUI
- **Winsound** — sound playback (Windows built-in)

No external APIs, no paid services, no internet required after setup.

---

## 🚀 How to Run

1. Clone this repository
   ```bash
   git clone https://github.com/YOUR-USERNAME/morse-code-translator.git
   cd morse-code-translator
   ```

2. Run the app (Windows only, due to `winsound`)
   ```bash
   python gui.py
   ```

No external libraries to install — everything used is built into Python.

---

## 📂 Project Structure

```
morse-code-translator/
│
├── gui.py            # Main app window, buttons, sound logic
├── translator.py      # Text <-> Morse conversion logic
├── morse_dict.py       # Morse code lookup dictionary
└── README.md
```

---

## 📖 What I Learned

- Using dictionaries for character-mapping logic
- Structuring a project across multiple files
- Building a GUI with Tkinter
- Debugging real errors in my own code (typos taught me more than tutorials)

---

## 🔭 What's Next

This is my first project after learning Python fundamentals — more projects coming as I go deeper into Python and eventually data science.

---

## 👤 Author

**Syed Mohd Hamza**
