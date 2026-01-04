import os
import platform
import subprocess

# Script and icon file names
script_name = "Jesus.py"
icon_name = "game_icon.ico"

# Check if critical files exist
for file in [script_name, icon_name]:
    if not os.path.exists(file):
        print(f"Error: Required file '{file}' not found in current directory.")
        exit(1)

# All expected audio assets from your manifest
asset_files = [
    "apostle_speaks.wav",
    "apostle_speaks_1.wav",
    "apostle_speaks_2.wav",
    "apostle_speaks_3.wav",
    "apostle_speaks_4.wav",
    "apostle_speaks_5.wav",
    "apostle_speaks_6.wav",
    "apostle_speaks_7.wav",
    "apostle_speaks_8.wav",
    "apostle_speaks_9.wav",
    "apostle_speaks_10.wav",
    "apostle_speaks_11.wav",
    "apostle_speaks_12.wav",
    "apostle_speaks_13.wav",
    "apostle_speaks_14.wav",
    "apostle_speaks_15.wav",
    "apostle_speaks_16.wav",
    "apostle_speaks_17.wav",
    "apostle_speaks_18.wav",
    "correct.wav",
    "game_over.wav",
    "main_theme.wav",
    "menu_music.wav"
]

# Only include files that actually exist
existing_assets = [f for f in asset_files if os.path.exists(f)]

if not existing_assets:
    print("Warning: None of the listed .wav files were found in the current directory!")
else:
    print(f"Found {len(existing_assets)} audio asset file(s) to include.")

# OS-specific separator for --add-data
separator = ";" if platform.system() == "Windows" else ":"

# Build the PyInstaller command
command = [
    "pyinstaller",
    "--onefile",                       # Pack everything into a single .exe
    "--icon", icon_name,               # Use your game icon
    "--noconsole",                     # No console window (recommended for GUI/game)
    "--clean",                         # Remove old build/dist folders first
    "--name", "ApostleEncounters",     # Name of the final executable
    "--version-file", "version_info.txt",  # ← Now correctly using the generated txt file
    script_name                        # Your main Python script
]

# Add every existing asset
for asset in existing_assets:
    command.extend(["--add-data", f"{asset}{separator}."])

# Show what we're about to run
print("\nRunning PyInstaller with the following command:")
print(" ".join(command))
print("\n" + "="*70)

try:
    result = subprocess.run(command, check=True, text=True, capture_output=True)
    print("Build finished successfully!")
    print("Final executable should be here:")
    print(f"  • Windows →  dist/ApostleEncounters.exe")
    print(f"  • macOS/Linux →  dist/ApostleEncounters")
    print("\nPyInstaller output summary:")
    print(result.stdout[-1500:])  # Show last part of output (most interesting)
except subprocess.CalledProcessError as e:
    print(f"Build FAILED (return code {e.returncode})")
    print("Error output:\n" + e.stderr)
    print("\nStandard output:\n" + e.stdout)
    exit(1)