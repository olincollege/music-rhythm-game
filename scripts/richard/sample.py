"""
catJAM, a rhythm-based music game!
"""

import pygame 
from sample_game import *

def main():
    timer = 0 
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
    clock  = pygame.time.Clock()

    # All the scenes.
    scenes = {}
    scenes['menu'] = Menu(screen, scenes)
    scenes['tutorial'] = Tutorial(screen, scenes)
    scenes['transition'] = Transition(screen,scenes)
    scenes['game'] = Game(screen, scenes)

    # Start with the menu.
    scene = scenes['menu']
    scene.start()
    
    
    while True:
        dt = clock.tick(60)/1000
        timer = timer + dt
        # print(timer)
        # print("tick " + str(pygame.time.get_ticks()))
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return

        # Switch scenes if there is a new scene.
        new_scene = scene.update(events, dt)
        
        if new_scene is not scene:
            # If there is a new scene, make sure to allow the old
            # scene to exit and the new scene to start.
            scene.exit()
            scene = new_scene
            scene.start()

        pygame.display.update()


if __name__ == '__main__':
    main()