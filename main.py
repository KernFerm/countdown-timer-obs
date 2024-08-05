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
    "# make sure to place name of the .mp3 or .wav example:  peanut_butter in this place remove quotes" = pygame.mixer.Sound('example.mp3') # place your .mp3 or .wav which ever you want to use just make sure to replace .mp3 if it is a .wav same if it is a .wav to .mp3 
    peanut_butter.set_volume(0.26)  # Set volume to 50%  # see i did the same peanut_butter.set_volume(0.25)   make sure to put your actual .mp3 name in place of peanut_butter

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
            peanut_butter.play() # make sure to put your actual .mp3 name in place of peanut_butter

    pygame.quit()

if __name__ == "__main__":
    countdown_timer(60)  # 1 minute
