from score import *
import pygame
from pygame.locals import *

pygame.init()

# screen = pygame.display.set_mode((1280, 720))
# background = pygame.image.load("assets/imgs/Background.png")
# backgroud = pygame.transform.scale(background, (1280, 720))
curr_score = 72

display_surface = pygame.display.set_mode((1280, 720))
BLACK = (0,0,0) #RGB values for black
WHITE = (255,255,255)
CYAN = (23, 232, 255)

font = pygame.font.Font('freesansbold.ttf', 32)
 
text = font.render(str(curr_score), True, BLACK)

while True:
 
    # completely fill the surface object
    # with white color
    display_surface.fill(WHITE)
 
    # copying the text surface object
    # to the display surface object
    # at the center coordinate.
    display_surface.blit(text, (1000,20))
 
    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get():
 
        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT:
 
            # deactivates the pygame library
            pygame.quit()
 
            # quit the program.
            quit()
 
        # Draws the surface object to the screen.
        pygame.display.update()