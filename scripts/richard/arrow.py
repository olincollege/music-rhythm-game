"""
Class for the arrow sprite
"""
import pygame as pg
import random

class Arrow(pg.sprite.Sprite):
    """
    Arrow Sprite with basic rotation functionality

    Attributes:
        -_arrow_sprite: An image of the arrow sprite
    """
    
    def __init__(self, angle, x, y):
        """
        Create a new instance of the arrow sprite that is scaled and rotated.
        """
        self._surface = pg.image.load("../assets/imgs/arrow_sprite.png").convert_alpha()
        self._surface = pg.transform.smoothscale(self._surface, (100, 100))
        self._surface = pg.transform.rotate(self._surface, angle)
        self._rect = self._surface.get_rect(topleft = (x, y))
        self._x = x
        self._y = y



    def display_arrow(self, screen):
        """
        Displays the arrow on top of the screen.
        """
        screen.blit(self._surface, (self._x, self._y))




    def update(self):
        """
        Changes the arrow's y position. When run in the game loop, the arrow will move up the screen by 2 pixels.
        """
        self._y -= 2
        