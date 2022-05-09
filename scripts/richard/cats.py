"""
Classes for the Cat Sprites
"""

import pygame as pg

class Cat(pg.sprite.Sprite):
    """
    Cat Sprite
    Attributes:
        -_surface: An image of the Cat Sprite
        -_x: An integer representing the x-coordinate of the top left corner of 
             the cat sprite
        -_y: An integer representing the y-coordinate of the top left corner of 
             the cat sprite
    """
    def __init__(self, cat, x, y, mirrored = False):
        """
        Create a new instance of the cat sprite that is scaled properly

        Arguments:
            -cat: a string representing the type of cat the sprite will be
            -x: An integer representing the x-coordinate of the top left corner
                of the cat sprite
            -y: An integer representing the y-coordinate of the top left corner
                of the cat sprite
            -mirrored: A boolean representing if the cat is mirrored from the
                       original position
        """
        if cat == "piano":
            self._surface = pg.image.load\
                ("../assets/imgs/Piano Cat Temp Sprite.png").convert_alpha()
            self._surface = pg.transform.smoothscale(self._surface, (300, 300))
        elif cat == "speaker":
            self._surface = pg.image.load\
            ("../assets/imgs/Speakers Cat Temp Sprite.png").convert_alpha()
            self._surface = pg.transform.smoothscale(self._surface, (250, 250))
        elif cat == "guitar":
            self._surface = pg.image.load\
               ("../assets/imgs/guitar cat 2.png").convert_alpha()
            self._surface = pg.transform.smoothscale(self._surface, (350, 350))
        elif cat == "dj":
            self._surface = pg.image.load("../assets/imgs/DJ Cat Temp Sprite.png")\
            .convert_alpha()
            self._surface = pg.transform.smoothscale(self._surface, (325, 325))
        elif cat == "drum":
            self._surface = pg.image.load("../assets/imgs/sample_cat.png")\
            .convert_alpha()
            self._surface = pg.transform.smoothscale(self._surface, (300, 300))

        if mirrored:
            if cat == "piano":
                self._surface = pg.image.load\
                ("../assets/imgs/Piano Cat Temp Sprite.png").convert_alpha()
                self._surface = pg.transform.smoothscale(self._surface, \
                    (300, 300))
                self._surface = pg.transform.flip(self._surface, True, False)

            elif cat == "guitar":
                self._surface = pg.image.load\
                ("../assets/imgs/guitar cat 1.png").convert_alpha()
                self._surface = pg.transform.smoothscale(self._surface, \
                    (350, 350))
                self._surface = pg.transform.flip(self._surface, True, False)
            elif cat == "drum":
                self._surface = pg.image.load("../assets/imgs/sample_cat.png")\
                    .convert_alpha()
                self._surface = pg.transform.smoothscale(self._surface, \
                    (300, 300))
                self._surface = pg.transform.flip(self._surface, True, False)
            
        self._surface.get_rect(topleft = (x, y))
        self._x = x
        self._y = y

    def display(self, screen):
        """
        Display the cat sprite at (_x,_y)

        Arguments:
            -screen: A pygame display 
        """
        screen.blit(self._surface, (self._x, self._y))