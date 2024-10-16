# Bubbles The Dev - Countdown Timer with Sound

A Python-based countdown timer built using Pygame and Tkinter. This application allows users to adjust the timer, import sound files (`.mp3` or `.wav`), and play a sound when the timer reaches 30 seconds. The interface is user-friendly and includes buttons to start, stop, increase, decrease, and reset the timer.

## 📥 How to Download the Repo for First-Time Users

- Click the link to read [**Instructions**](https://www.gitprojects.fnbubbles420.org/how-to-download-repos).

### **[Download_Bubbles_The_Dev-Countdown-Timer.zip](https://github.com/KernFerm/countdown-timer-obs/releases/tag/countdown-timer-exe)**

## Features

- Adjustable countdown timer with a default duration of 60 seconds.
- Import sound files (`.mp3` or `.wav`) to play when the timer reaches 30 seconds.
- Simple, user-friendly interface built with Pygame.
- Buttons to start, stop, increase, decrease, and reset the timer.

## Requirements

- Python 3.11+
- Pygame
- Tkinter (usually comes pre-installed with Python on most systems)

### If you don't have Python installed, here are some options:

- **YOU ONLY NEED ONE VERSION OF PYTHON TO RUN THIS!!**
  - [Python 3.11.6](https://github.com/KernFerm/Py3.11.6installer)
  - [Python 3.11.9](https://github.com/KernFerm/Py3.11.9installer)
  - [Python 3.12.1](https://github.com/KernFerm/Py3.12.1-installer-batch)

```
.
├── .github/                 # GitHub issue templates
├── OpenSource-Sounds-For-Countdown-Timer/  # Directory for countdown sounds
├── image/                   # Directory for images
├── CODE_OF_CONDUCT.md       # Code of Conduct for the project
├── CONTRIBUTING.md          # Guidelines for contributing
├── LICENSE                  # License information
├── SECURITY.md              # Security policy
├── Sounds.txt               # List or details about sound files
├── install_dep.bat          # Batch script to install dependencies
├── main-launcher.bat        # Main batch script to launch the program
├── main.py                  # Main Python file for your program
├── config.py                # Configuration settings
├── readme.md                # Main project documentation (README)
├── requirements.txt         # Python dependencies
└── timer-list.md            # Information about available timers
```

## Installation

1. **Clone the repository**:
```
git clone https://github.com/KernFerm/countdown-timer-obs.git
cd countdown-timer-obs
```

2. **Install dependencies**: Install the required dependencies using pip:

```
pip install pygame
```
```
pip install tk
```

3. **Run the script**: Once dependencies are installed, run the script using Python:

```
python main.py
```

## Usage
- **Adjust Timer**: Use the `+10 sec` and `-10 sec` buttons to increase or decrease the countdown time.
- **Start/Stop Timer**: Use the `Start` button to start the countdown, and the `Stop` button to pause it.
- **Import Sound**: Use the `Import Sound` button to select a `.mp3` or `.wav` file that will play when the timer reaches 30 seconds.
- **Clear Timer**: Use the `Clear Timer` button to reset the timer to 60 seconds.

## Example
When running the script, the interface will display:

- A countdown timer.
- Buttons to adjust the timer, start/stop it, import a sound, and reset the timer.
- Information about the selected sound file.

## Timer Controls
-------------------------
| Button        | Description                              |
|---------------|------------------------------------------|
| +10 sec       | Increases the countdown timer by 10 sec  |
| -10 sec       | Decreases the countdown timer by 10 sec  |
| Start         | Starts the countdown timer               |
| Stop          | Pauses the countdown timer               |
| Import Sound  | Imports a .mp3 or .wav sound file        |
| Clear Timer   | Resets the timer to 60 seconds           |
----------------

## Code Overview

### Timer Functionality

- The countdown timer updates every second. You can increase or decrease the time using the buttons:
```
# Increase the timer by 10 seconds
duration += 10

# Decrease the timer by 10 seconds, ensuring it doesn't go below 0
duration = max(0, duration - 10)
```

## Sound Import
You can import `.mp3` or `.wav` files. The sound will play when the timer reaches 30 seconds:

```
selected_file = filedialog.askopenfilename(
    title="Select Sound File",
    filetypes=AUDIO_FILE_TYPES
)
```

- If the selected sound file's duration is longer than 2 minutes, an error message will appear:

```
if duration > 120:
    messagebox.showerror("Invalid File", "The file exceeds 2 minutes.")
```

## Configuration (`config.py`)

- Here are the configuration settings used in the program:

```
# Configurations for Countdown Timer Application

# Timer settings
ALERT_DURATION = 30  # When to play sound (in seconds)

# Sound settings
SOUND_VOLUME = 0.26

# File dialog settings
AUDIO_FILE_TYPES = [("Audio Files", "*.mp3 *.wav")]

# Frame settings
FPS = 30  # Frames per second for the Pygame clock
```

## Contributing

- We welcome contributions! 
- Please read our `Contributing Guidelines` and `Code of Conduct` before making a pull request.












