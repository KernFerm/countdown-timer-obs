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
    nuke_siren = pygame.mixer.Sound('example.mp3') # place your .mp3 or .wav which ever you want to use just make sure to replace .mp3 if it is a .wav same if it is a .wav to .mp3 
    nuke_siren.set_volume(0.26)  # Set volume to 50%

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
            start_ticks = pygame.time.get_ticks()  # Reset the start time

        clock.tick(60)

        # Play the nuke siren when timer is at 30 seconds
        if duration == 30: 
            nuke_siren.play()

    pygame.quit()

if __name__ == "__main__":
    countdown_timer(60)  # 1 minute
