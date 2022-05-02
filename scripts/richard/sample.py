"""
catJAM, a rhythm-based music game!
"""

import pygame 
import time

base_beat = "../assets/soundtrack/base beat.wav"
transition_music = "../assets/soundtrack/transition music.wav"
demo_4_melodies = "../assets/soundtrack/demo 4 melodies.wav"


_songs = [base_beat,transition_music,demo_4_melodies]

def play_next_song():
    global _songs
    _songs = _songs[1:] + [_songs[0]] # move current song to the back of the list 
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode([1280,720])       
    running = True
    # MUSIC
    if pygame.mixer and not pygame.mixer.get_init():
        print("Warning, no sound")
        pygame.mixer = None
    
    
    # creating sep channels for layering music
    # ch1 = pygame.mixer.Channel(0)
    # ch2 = pygame.mixer.Channel(1)

    
    play_next_song()

    main_game = True
    # GAME
    screen.fill((255, 255, 255))
    
    while main_game is True:
    # Form screen        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                music = False

        

        clock.tick(40)

        

    pygame.quit()


if __name__ == '__main__': main()