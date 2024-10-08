# Countdown Timer with Sound

A Python-based countdown timer built using Pygame and Tkinter. This application allows users to adjust the timer, import sound files (`.mp3` or `.wav`), and play a sound when the timer reaches a specific time. The user-friendly interface includes buttons to start, stop, increase, decrease, and clear the timer.

## 📥 How to Download the Repo for First-Time Users

- Click the link to read [**Instructions**](https://www.gitprojects.fnbubbles420.org/how-to-download-repos).

### **[Download_Bubbles_The_Dev-Countdown-Timer.zip](https://github.com/KernFerm/countdown-timer-obs/releases/tag/countdown-timer-exe)**

## Features

- Adjustable countdown timer.
- Import sound files (`.mp3` or `.wav`) to play when the timer reaches a set time.
- Simple, user-friendly interface built with Pygame.
- Buttons to start, stop, increase, decrease, and reset the timer.

## Requirements

- Python 3.11
- Pygame
- Tkinter (usually comes pre-installed with Python on most systems)

 ### If you dont have a pet python here is a couple below:
- **YOU ONLY NEED ONLY VERSION OF PYTHON TO RUN THIS !!**
- [Python 3.11.6](https://github.com/KernFerm/Py3.11.6installer)
- [Python 3.11.9](https://github.com/KernFerm/Py3.11.9installer)
- [Python 3.12.1](https://github.com/KernFerm/Py3.12.1-installer-batch)

## Installation

1. **Clone the repository**:
```
git clone https://github.com/kernferm/countdown-timer-obs.git
cd countdown-timer-obs
```

2. **Install dependencies:** Install the required dependencies using pip:
```
pip install pygame
```
```
pip install tk
```

3. **Run the script:** Once dependencies are installed, run the script using Python:
```
python main.py
```

## Usage

- **Adjust Timer:** Use the `+10 sec` and `-10 sec` buttons to increase or decrease the countdown time.
- **Start/Stop Timer:** Use the `Start` button to start the countdown, and the `Stop` button to pause it.
- **Import Sound:** Use the Import Sound button to select a `.mp3` or `.wav` file that will play when the timer reaches a specific time (e.g., 40 seconds).
- **Clear Timer:** Use the `Clear Timer` button to reset the timer to its initial duration.

## Example
When running the script, the interface will display:

- A countdown timer.
- Buttons to adjust the timer, `start/stop` it, `import` a sound, and `reset` the timer.
- Information about the sound file that is selected.

### Timer Controls

| Button         | Description                              |
|----------------|------------------------------------------|
| **+10 sec**    | Increases the countdown timer by 10 sec   |
| **-10 sec**    | Decreases the countdown timer by 10 sec   |
| **Start**      | Starts the countdown timer                |
| **Stop**       | Pauses the countdown timer                |
| **Import Sound** | Imports a `.mp3` or `.wav` sound file   |
| **Clear Timer** | Resets the timer to the initial value    |

## Code Overview
**Timer Functionality**
- The countdown timer is updated every second, and the user can adjust the time using the buttons:
```
# Increase the timer by 10 seconds
duration += 10

# Decrease the timer by 10 seconds
duration = max(0, duration - 10)
```

## Sound Import
- The user can import `.mp3` or `.wav` files, which will play when the timer reaches a specified point:
```
selected_file = filedialog.askopenfilename(
    title="Select Sound File",
    filetypes=[("Audio Files", "*.mp3 *.wav")]
)
```
