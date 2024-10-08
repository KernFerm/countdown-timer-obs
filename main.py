import pygame
import sys
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def select_sound():
    """Open a file dialog to select a .mp3 or .wav file."""
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(
        title="Select Sound File",
        filetypes=[("Audio Files", "*.mp3 *.wav")]
    )
    return file_path if file_path else None

def check_sound_duration(file_path):
    """Check if the sound file is less than or equal to 2 minutes."""
    if file_path.endswith('.mp3') or file_path.endswith('.wav'):
        sound = pygame.mixer.Sound(file_path)
        duration = sound.get_length()
        if duration <= 120:  # 120 seconds = 2 minutes
            return True
        else:
            messagebox.showerror("Invalid File", "The file exceeds 2 minutes.")
            return False
    return False

def countdown_timer(initial_duration):
    pygame.init()
    font = pygame.font.SysFont('Arial', 60)
    small_font = pygame.font.SysFont('Arial', 24)  # Font for showing sound file name
    button_font = pygame.font.SysFont('Arial', 30)  # Font for button text
    width, height = 600, 700  # Window size with more height for button layout
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Bubbles The Dev - Countdown Timer')

    # Initialize mixer for sound playback
    pygame.mixer.init()

    sound_file = None
    sound_file_name = "No sound selected"
    peanut_butter = None

    clock = pygame.time.Clock()
    duration = initial_duration
    start_ticks = 0
    is_running = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Handle button click to import sound
                if 100 <= event.pos[0] <= 500 and 580 <= event.pos[1] <= 630:
                    selected_file = select_sound()
                    if selected_file and check_sound_duration(selected_file):
                        sound_file = selected_file
                        peanut_butter = pygame.mixer.Sound(sound_file)
                        peanut_butter.set_volume(0.26)
                        sound_file_name = os.path.basename(sound_file)  # Get just the file name
                
                # Increase the timer by 10 seconds
                elif 100 <= event.pos[0] <= 250 and 480 <= event.pos[1] <= 530:
                    duration += 10

                # Decrease the timer by 10 seconds, but don't go below 0
                elif 350 <= event.pos[0] <= 500 and 480 <= event.pos[1] <= 530:
                    duration = max(0, duration - 10)

                # Start the timer
                elif 100 <= event.pos[0] <= 250 and 530 <= event.pos[1] <= 580:
                    if not is_running:
                        is_running = True
                        start_ticks = pygame.time.get_ticks()

                # Stop the timer
                elif 350 <= event.pos[0] <= 500 and 530 <= event.pos[1] <= 580:
                    is_running = False

                # Clear the timer
                elif 100 <= event.pos[0] <= 500 and 630 <= event.pos[1] <= 680:
                    duration = initial_duration  # Reset the timer back to the initial value
                    is_running = False  # Stop the timer if it's running

        minutes, seconds = divmod(duration, 60)
        timer_str = '{:02d}:{:02d}'.format(minutes, seconds)

        screen.fill((0, 0, 0))
        text = font.render(timer_str, True, (255, 255, 255))
        text_rect = text.get_rect(center=(width // 2, height // 2 - 200))
        screen.blit(text, text_rect)

        # Show the selected sound file
        sound_text = small_font.render(f"Playing sound: {sound_file_name}", True, (255, 255, 255))
        sound_rect = sound_text.get_rect(center=(width // 2, height // 2 - 140))
        screen.blit(sound_text, sound_rect)

        # First row: Increase, Decrease
        pygame.draw.rect(screen, (0, 255, 255), (100, 480, 150, 50))  # Increase button
        increase_text = button_font.render("+10 sec", True, (0, 0, 0))
        increase_rect = increase_text.get_rect(center=(175, 505))
        screen.blit(increase_text, increase_rect)

        pygame.draw.rect(screen, (255, 0, 0), (350, 480, 150, 50))  # Decrease button
        decrease_text = button_font.render("-10 sec", True, (0, 0, 0))
        decrease_rect = decrease_text.get_rect(center=(425, 505))
        screen.blit(decrease_text, decrease_rect)

        # Second row: Start, Stop
        pygame.draw.rect(screen, (0, 255, 0), (100, 530, 150, 50))  # Start button
        start_text = button_font.render("Start", True, (0, 0, 0))
        start_rect = start_text.get_rect(center=(175, 555))
        screen.blit(start_text, start_rect)

        pygame.draw.rect(screen, (255, 0, 0), (350, 530, 150, 50))  # Stop button
        stop_text = button_font.render("Stop", True, (0, 0, 0))
        stop_rect = stop_text.get_rect(center=(425, 555))
        screen.blit(stop_text, stop_rect)

        # Third row: Import Sound and Clear Timer
        pygame.draw.rect(screen, (0, 255, 0), (100, 580, 400, 50))  # Import Sound button
        button_text = button_font.render("Import Sound", True, (0, 0, 0))
        button_rect = button_text.get_rect(center=(300, 605))
        screen.blit(button_text, button_rect)

        pygame.draw.rect(screen, (255, 255, 0), (100, 630, 400, 50))  # Clear Timer button
        clear_text = button_font.render("Clear Timer", True, (0, 0, 0))
        clear_rect = clear_text.get_rect(center=(300, 655))
        screen.blit(clear_text, clear_rect)

        pygame.display.update()

        # Check the time elapsed only if the timer is running
        if is_running:
            elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
            if elapsed_time >= 1 and duration > 0:
                duration -= 1
                start_ticks = pygame.time.get_ticks()  # Reset after each second

        clock.tick(30)  # Reduces CPU usage

        # Play the sound when timer is at 40 seconds
        if duration == 40 and peanut_butter and not pygame.mixer.get_busy():  # Play once when the timer hits 40 seconds
            peanut_butter.play()

        # Stop the timer when it reaches 0
        if duration == 0:
            is_running = False
            break

    pygame.quit()

if __name__ == "__main__":
    countdown_timer(60)  # Initial timer duration set to 60 seconds
