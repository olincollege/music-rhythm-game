"""
File for catJAM game controller
"""
import random
import pygame as pg
from model import *
from view import *

# Disabled pylint warnings that would break our code if we fixed
# pylint: disable=invalid-name
# pylint: disable=useless-super-delegation
# pylint: disable=no-self-use
# pylint: disable=not-callable

def player_produce_arrow(player_arrows, arrows_on_screen):
    """
    This function produces arrows on the arrow's side based off the pattern
    of arrows that the computer sides function.

    Arguments:
        -player_arrows: a list of arrows the player must hit
        -arrows_on screen: a list of arrows currently on the screen

    Returns:
        -player_arrows: a list of arrows the player must hit
        -arrows_on screen: a list of arrows currently on the screen
    """
    if arrows_on_screen[0] == "up":
        copy_arrow = PlayerArrow("up")
        copy_arrow.position()
        player_arrows[0].append(copy_arrow)

    elif arrows_on_screen[0] == "left":
        copy_arrow = PlayerArrow("left")
        copy_arrow.position()
        player_arrows[1].append(copy_arrow)

    elif arrows_on_screen[0] == "right":
        copy_arrow = PlayerArrow("right")
        copy_arrow.position()
        player_arrows[2].append(copy_arrow)

    elif arrows_on_screen[0] == "down":
        copy_arrow = PlayerArrow("down")
        copy_arrow.position()
        player_arrows[3].append(copy_arrow)

    return player_arrows, arrows_on_screen
