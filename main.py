import pygame
import sys

def countdown_timer(duration):
    pygame.init()
    font = pygame.font.SysFont('Arial', 60)
    width, height = 400, 100
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Countdown Timer')

    # Initialize mixer for sound playback
    pygame.mixer.init()
    peanut_butter = pygame.mixer.Sound('example.mp3')  # Replace 'example.mp3' with your actual sound file
    peanut_butter.set_volume(0.26)  # Adjust volume as needed

    clock = pygame.time.Clock()
    start_ticks = pygame.time.get_ticks()

    while duration:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        minutes, seconds = divmod(duration, 60)
        timer_str = '{:02d}:{:02d}'.format(minutes, seconds)

        screen.fill((0, 0, 0))
        text = font.render(timer_str, True, (255, 255, 255))
        text_rect = text.get_rect(center=(width // 2, height // 2))
        screen.blit(text, text_rect)

        pygame.display.update()

        # Check the time elapsed
        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
        if elapsed_time >= 1:
            duration -= 1
            start_ticks = pygame.time.get_ticks()  # Optional: reset after each second

        clock.tick(30)  # Reduces CPU usage

        # Play the sound when timer is at x seconds
        if duration == 40 and not pygame.mixer.get_busy():  # Play once when the timer hits 40 seconds
            peanut_butter.play()

    pygame.quit()

if __name__ == "__main__":
    countdown_timer(60)  # Adjust the timer duration as needed
