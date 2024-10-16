import pygame
import sys
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from config import *  # Import your config settings

def select_sound():
    """Open a file dialog to select a .mp3 or .wav file."""
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(
        title="Select Sound File",
        filetypes=AUDIO_FILE_TYPES
    )
    return file_path if file_path else None

def check_sound_duration(file_path):
    """Check if the sound file is less than or equal to the max allowed duration."""
    try:
        sound = pygame.mixer.Sound(file_path)
        duration = sound.get_length()
        if duration <= 120:
            return True
        else:
            messagebox.showerror("Invalid File", "The file exceeds 2 minutes.")
            return False
    except pygame.error as e:
        messagebox.showerror("Error", f"Could not load sound: {e}")
        return False

def countdown_timer():
    """Main countdown timer logic."""
    pygame.init()
    font = pygame.font.SysFont(None, 60)  # Use default system font
    small_font = pygame.font.SysFont(None, 24)
    button_font = pygame.font.SysFont(None, 30)

    screen = pygame.display.set_mode((600, 700))
    pygame.display.set_caption('Bubbles The Dev - Countdown Timer')

    pygame.mixer.init()

    sound_file = None
    sound_file_name = "No sound selected"
    peanut_butter = None

    clock = pygame.time.Clock()
    duration = 60  # Default timer duration in seconds
    start_ticks = 0
    is_running = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 100 <= event.pos[0] <= 500 and 580 <= event.pos[1] <= 630:
                    selected_file = select_sound()
                    if selected_file and check_sound_duration(selected_file):
                        sound_file = selected_file
                        peanut_butter = pygame.mixer.Sound(sound_file)
                        peanut_butter.set_volume(SOUND_VOLUME)
                        sound_file_name = os.path.basename(sound_file)

                elif 100 <= event.pos[0] <= 250 and 480 <= event.pos[1] <= 530:
                    duration += 10

                elif 350 <= event.pos[0] <= 500 and 480 <= event.pos[1] <= 530:
                    duration = max(0, duration - 10)

                elif 100 <= event.pos[0] <= 250 and 530 <= event.pos[1] <= 580:
                    if not is_running:
                        is_running = True
                        start_ticks = pygame.time.get_ticks()

                elif 350 <= event.pos[0] <= 500 and 530 <= event.pos[1] <= 580:
                    is_running = False

                elif 100 <= event.pos[0] <= 500 and 630 <= event.pos[1] <= 680:
                    duration = 60  # Reset to default duration
                    is_running = False

        minutes, seconds = divmod(duration, 60)
        timer_str = '{:02d}:{:02d}'.format(minutes, seconds)

        screen.fill((0, 0, 0))
        text = font.render(timer_str, True, (255, 255, 255))
        text_rect = text.get_rect(center=(300, 150))
        screen.blit(text, text_rect)

        sound_text = small_font.render(f"Playing sound: {sound_file_name}", True, (255, 255, 255))
        sound_rect = sound_text.get_rect(center=(300, 210))
        screen.blit(sound_text, sound_rect)

        pygame.draw.rect(screen, (0, 255, 255), (100, 480, 150, 50))
        increase_text = button_font.render("+10 sec", True, (0, 0, 0))
        increase_rect = increase_text.get_rect(center=(175, 505))
        screen.blit(increase_text, increase_rect)

        pygame.draw.rect(screen, (255, 0, 0), (350, 480, 150, 50))
        decrease_text = button_font.render("-10 sec", True, (0, 0, 0))
        decrease_rect = decrease_text.get_rect(center=(425, 505))
        screen.blit(decrease_text, decrease_rect)

        pygame.draw.rect(screen, (0, 255, 0), (100, 530, 150, 50))
        start_text = button_font.render("Start", True, (0, 0, 0))
        start_rect = start_text.get_rect(center=(175, 555))
        screen.blit(start_text, start_rect)

        pygame.draw.rect(screen, (255, 0, 0), (350, 530, 150, 50))
        stop_text = button_font.render("Stop", True, (0, 0, 0))
        stop_rect = stop_text.get_rect(center=(425, 555))
        screen.blit(stop_text, stop_rect)

        pygame.draw.rect(screen, (0, 255, 0), (100, 580, 400, 50))
        button_text = button_font.render("Import Sound", True, (0, 0, 0))
        button_rect = button_text.get_rect(center=(300, 605))
        screen.blit(button_text, button_rect)

        pygame.draw.rect(screen, (255, 255, 0), (100, 630, 400, 50))
        clear_text = button_font.render("Clear Timer", True, (0, 0, 0))
        clear_rect = clear_text.get_rect(center=(300, 655))
        screen.blit(clear_text, clear_rect)

        pygame.display.update()

        if is_running:
            elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
            if elapsed_time >= 1 and duration > 0:
                duration -= 1
                start_ticks = pygame.time.get_ticks()

        clock.tick(FPS)

        if duration == ALERT_DURATION and peanut_butter and not pygame.mixer.get_busy():
            peanut_butter.play()

        if duration == 0:
            is_running = False
            break

    pygame.quit()

if __name__ == "__main__":
    countdown_timer()
