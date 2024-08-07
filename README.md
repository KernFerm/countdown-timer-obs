# Open Source

# Countdown Timer for OBS with Sound Alert

This Python script creates a countdown timer overlay for OBS (Open Broadcaster Software) or Various like Cooking timer , Timeout timer and plays which ever sound you choose when the timer reaches a specific point.

## how to download the repo first time users

  - click link to read [**Instructions**](https://www.gitprojects.fnbubbles420.org/how-to-download-repos)

## Pull Request
- make a `pull request` for [OpenSource-Sounds-For-Coundown-Timer](https://github.com/KernFerm/countdown-timer-OBS/tree/main/OpenSource-Sounds-For-Coundown-Timer)
- make a github account `free to make`
- `fork` the repo `copy main branch`
- `drag` n `drop` sounds into OpenSource-Sounds-For-Coundown-Timer Folder for others to use
- `.mp3` or . `wav`
- check [CONTRIBUTING.md](https://github.com/KernFerm/countdown-timer-OBS/blob/main/CONTRIBUTING.md)


## Features

- Countdown timer display
- Plays a sound alert at 30 seconds remaining
- `.mp3` or `.wav`

### You can use it for other stuff like 
- timeout timer
- cooking timer
- etc
- use it as a timer only , do the same steps but leave out the `obs steps`

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
  ```
  # On Windows ( copy and paste below in `cmd.exe` )
  ```
  .venv\Scripts\activate
  ```
  
  # On macOS/Linux ( copy and paste below in `terminal` )
  ```
  source .venv/bin/activate
  ```

3. **Install the required packages:**

  ```
  pip install -r requirements.txt
  ```

- use this `create_and_activate_venv_install_dependencies.bat`
- or
- use this `install_requirements.bat`
 
## Usage

1. Place your MP3 file or WAV file (`example.mp3`) in the same directory as the script.
2. **Run the script:**

  ```
  python main.py
  ```

## Customization

- Modify the `duration` parameter in the `countdown_timer` function to change the length of the countdown.
- Change the `sound.set_volume(0.26)` line to adjust the volume of the alert sound.
- Replace `'example.mp3'` or `example.wav` with the name of your sound file.

## Info 

- To get sounds if you `do not` have any on your computer.
- youtube.com then find your sound you want to use as entrance theme.
- go to `URL` remove the letters `ebu`
- `URL` now should say yout.com/whatever url you have at the end of yout.com

## Add to OBS
**Run the Countdown Timer Script:**

**Ensure your countdown timer script is running.**
- Add Window Capture Source in OBS:

## Open OBS.
- In the `Sources` panel, click on the + button at the bottom.
- Select `Window Capture`.
- Name the new source (e.g., "Countdown Timer") and click `OK`.
- In the properties window, select the countdown timer window from the `Window` dropdown menu.
- Adjust the size and position of the window capture to fit your stream layout.
- Click `OK` to add the source.

# Add Audio Output Capture Source in OBS:
- In the `Sources` panel, click on the + button at the bottom.
- Select `Audio Output Capture`.
- Name the new source (e.g., "System Audio") and click `OK`.
- In the properties window, select the appropriate audio device (usually the default audio device or speakers).
- Click `OK` to add the source.

