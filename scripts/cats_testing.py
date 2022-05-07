import pygame as pg
from pygame.locals import *
from cats import *
pg.init()

width = 1280
height = 720

bg = pg.image.load("assets/imgs/Background.png")
pg.display.set_caption("Cat positioning")

screen = pg.display.set_mode((width, height))

# Background Cats
dj_cat = Cat("dj", 460, 350)
speaker_cat = Cat("speaker", 500, 65)

# Team 1 Cats
piano_cat = Cat("piano", 1000, 300)
guitar_cat = Cat("guitar", 700, 350)
drum_cat = Cat("drum", 850, 225)

# Team 2 Cats
piano_cat_2 = Cat("piano", -50, 300, True)
guitar_cat_2 = Cat("guitar", 205, 350, True)
drum_cat_2 = Cat("drum", 77, 225, True)

#game clock (fps)
clock = pg.time.Clock()

#game loop
    
dt = clock.tick(60)/1000
# print("tick " + str(pygame.time.get_ticks()))

running = True
while running:

    screen.blit(bg, (0, 0))
    dj_cat.display(screen)
    drum_cat.display(screen)
    piano_cat.display(screen)
    speaker_cat.display(screen)
    guitar_cat.display(screen)

    drum_cat_2.display(screen)
    piano_cat_2.display(screen)
    guitar_cat_2.display(screen)
    

    pg.display.update()


    