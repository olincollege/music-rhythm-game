"""
test functions for the Arrow class
"""
import pytest
from model import Arrow, PlayerArrow, ComputerArrow
import pygame as pg

#initializing pygame in order to test the functions
pg.init()
size = (1280, 720)
screen = pg.display.set_mode(size)

#creating instances of the class to test
test_arrow = Arrow("up")
test_player_arrow = PlayerArrow("up")
test_computer_arrow = ComputerArrow("up")

#TESTING FUNCTIONS

def test_update():
    """
    Checks that the update function changes the y-position.
    """
    test_arrow.update()
    assert test_arrow._y == -2

def test_at_top_screen():
    """
    Checks that the off-screen checking function returns False
    when the x and y of the arrow is at 0.
    """
    assert test_arrow.at_top_screen() == False

def test_PlayerArrow_position():
    """
    Checks that the position function of the PlayerArrow subclass
    changes the x and y values to what it is meant to be.
    """
    test_player_arrow.position()
    assert test_player_arrow.get_position() == (913, 600)

def test_ComputerArrow_position():
    """
    Checks that the position function of the ComputerArrow subclass
    changes the x and y values to what it is meant to be.
    """
    test_computer_arrow.position()
    assert test_computer_arrow.get_position() == (15,600)

def test_PlayerArrow_type():
    """
    Checks that the type function of the PlayerArrow subclass returns a string
    of what type of class the arrow instance is.
    """
    assert test_player_arrow.type() == "player"

def test_ComputerArrow_type():
    """
    Checks that the type function of the ComputerArrow subclass returns a
    string of what type of class the arrow instance is.
    """
    assert test_computer_arrow.type() == "computer"