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
    
    def __init__(self, direction):
        """
        Create a new instance of the arrow sprite that is scaled and rotated.
        """
        self._surface = pg.image.load("assets/imgs/arrow_sprite.png").convert_alpha()
        self._surface = pg.transform.smoothscale(self._surface, (100, 100))

        if direction == "up":
            self._surface = pg.transform.rotate(self._surface, 90)
        if direction == "down":
            self._surface = pg.transform.rotate(self._surface, 270)
        if direction == "right":
            self._surface = pg.transform.rotate(self._surface, 0)
        if direction == "left":
            self._surface = pg.transform.rotate(self._surface, 180)
        self._direction = direction
        self._x = 0
        self._y = 0

    def set_position(self, x, y):
        self._x = x
        self._y = y

    def get_direction(self):
        return self._direction



    def direction(self):
        if self._direction == "up":
            self._surface = pg.transform.rotate(self._surface, 90)
        if self._direction == "down":
            self._surface = pg.transform.rotate(self._surface, 270)
        if self._direction == "right":
            self._surface = pg.transform.rotate(self._surface, 0)
        if self._direction == "left":
            self._surface = pg.transform.rotate(self._surface, 180)


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


    def at_top_screen(self):
        if self._y < 0:
            return True
        return False

    def __repr__(self) -> str:
        return f"{self._direction}"


class PlayerArrow(Arrow):
    def __init__(self, direction):
        super().__init__(direction)

    def position(self):
        if self._direction == "up":
            self.set_position(500, 600)
        if self._direction == "left":
            self.set_position(590, 600)
        if self._direction == "right":
            self.set_position(670, 600)
        if self._direction == "down":
            self.set_position(800, 600)

    def type(self):
        return "player"
            

class ComputerArrow(Arrow):
    def __init__(self, direction):
        super().__init__(direction)

    def position(self):
        if self._direction == "up":
            self.set_position(10, 600)
        if self._direction == "left":
            self.set_position(100, 600)
        if self._direction == "right":
            self.set_position(180, 600)
        if self._direction == "down":
            self.set_position(255, 600)

    def type(self):
        return "computer"
        