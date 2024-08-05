# Countdown Timer for OBS with Sound Alert

This Python script creates a countdown timer overlay for OBS (Open Broadcaster Software) and plays which ever sound you choose when the timer reaches a specific point.

## Features

- Countdown timer display
- Plays a sound alert at 30 seconds remaining

## Requirements

- [Python 3.11.6](https://github.com/KernFerm/Py3.11.6installer)
- `pygame` library

## Installation

1. **Clone this repository:**
  
  ```
  git clone https://github.com/kernferm/countdown-timer-obs.git
  cd countdown-timer-obs
  ```

2. **Create and activate a virtual environment (optional but recommended):**

  ```
  python -m venv .venv
  # On Windows
  .venv\Scripts\activate
  # On macOS/Linux
  source .venv/bin/activate
  ```

3. **Install the required packages:**

  ```
  pip install -r requirements.txt
  ```

## Usage

1. Place your MP3 file (`example.mp3`) in the same directory as the script.
2. **Run the script:**

  ```
  python main.py
  ```

## Customization

- Modify the `duration` parameter in the `countdown_timer` function to change the length of the countdown.
- Change the `sound.set_volume(0.26)` line to adjust the volume of the alert sound.
- Replace `'example.mp3'` with the name of your sound file.

## Info 

- To get sounds if you `do not` have any on your computer.
- youtube.com then find your sound you want to use as entrance theme.
- go to `URL` remove the letters `ebu`
- `URL` now should say yout.com/whatever url you have at the end of yout.com
 
