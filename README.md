# Apostle Encounters

A faith-based word guessing game with voice guidance from an "Apostle" character.

Test your Bible knowledge, enjoy beautiful voice lines, and grow in faith while having fun!

## Game Features

- Single-player word guessing gameplay
- Multiple apostle voice responses (18+ unique lines)
- Atmospheric religious-themed music & sound effects
- Clean, minimal GUI experience
- Packaged as a single executable (no installation needed)

## How to Play

1. Run `ApostleEncounters.exe`
2. Listen to the Apostle's hints
3. Guess the hidden word (Bible-related terms, characters, places, etc.)
4. Enjoy the journey of discovery!

## Controls

- Type your guess i.e. 1, 2, 3, 4 → Enter
- Listen carefully to the Apostle's guidance
- Have fun and be blessed! ✝️

## Audio Assets Included

- Main theme & menu music
- Correct answer sound
- Game over sound
- 19 apostle speaking variations (apostle_speaks_0 to apostle_speaks_18)

## Requirements

- Windows 10 / 11 (64-bit recommended)
- No Python installation needed – everything is bundled

## Building from Source (Developers)

1. Make sure you have Python 3.8+ and PyInstaller installed
2. Place all required files in the same folder:
   - Jesus.py (main script)
   - game_icon.ico
   - All .wav audio files
   - version_info.txt (for file properties)
3. Run `build.py` to create a fresh executable

```bash
python build.py
