"""
Class for the arrow sprite
"""
import pygame as pg

class Arrow:
    """
    Arrow Sprite with basic rotation functionality

    Attributes:
        -_arrow_sprite: An image of the arrow sprite
    """
    
    def __init__(self):
        """
        Create a new instance of the arrow sprite
        """
        _arrow_sprite = pg.image.load("assets/arrow_sprite.png")


    def rotate(self,angle):
        """
        Rotates the arrow sprite

        Arguments:
            -Angle: an integer representing how much you want to rotate the 
                    arrow
        
        Returns:
            -None
        """
        self._arrow_sprite = pg.transform.rotate(self._arrow_sprite, angle)