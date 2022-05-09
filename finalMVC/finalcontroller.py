"""
File for catJAM game controller
"""
import random
import pygame as pg

# Disabled pylint warnings that would break our code if we fixed
# pylint: disable=invalid-name
# pylint: disable=useless-super-delegation
# pylint: disable=no-self-use
# pylint: disable=not-callable

class Arrow(pg.sprite.Sprite):
    """
    A parent class that initializes the size, direction, and color of all
    moving arrows. Also allows for easy control of arrow movement.

    Attributes:
        _surface:
            An image of the arrow sprite. Different colors of the same arrow
            are loaded for different instances dependent on which direction
            it points in.
        _direction:
            A string representing the direction that the user wants the arrow
            to point in. Direction determines which arrow image gets loaded,
            how much the image is rotated, and where on the screen it initially
            gets placed.
        _x:
            An integer representing the x-position of the sprite on the screen.
            This gets used when displaying the sprite.
        _y:
            An integer representing the y-position of the sprite on the screen.
            This gets used when displaying the sprite.
    """

    def __init__(self, direction):
        """
        Create a new instance of the arrow sprite that is scaled and rotated.
        """
        self._surface = pg.image.load("assets/imgs/arrow_sprite.png").\
            convert_alpha()

        if direction == "up":
            self._surface = pg.image.load("assets/imgs/green_arrow.png")\
                .convert_alpha()
            self._surface = pg.transform.rotate(self._surface, 90)
        if direction == "down":
            self._surface = pg.image.load("assets/imgs/blue_arrow.png").\
                convert_alpha()
            self._surface = pg.transform.rotate(self._surface, 270)
        if direction == "right":
            self._surface = pg.image.load("assets/imgs/yellow_arrow.png").\
                convert_alpha()
            self._surface = pg.transform.rotate(self._surface, 0)
        if direction == "left":
            self._surface = pg.image.load("assets/imgs/pink_arrow.png").\
                convert_alpha()
            self._surface = pg.transform.rotate(self._surface, 180)

        self._surface = pg.transform.smoothscale(self._surface, (95, 95))
        self._direction = direction
        self._x = 0
        self._y = 0

    @property
    def get_position(self):
        """
        Returns the x and y position of image.
        """
        return self._x, self._y

    def set_position(self, x, y):
        """
        Changes the x and y values.

        Args:
            x:
                An integer representing the pixel position on the screen that
                the user wants to set the sprite to.
            y:
                An integer representing the pixel position on the screen that
                the user wants to set the sprite to.

        """
        self._x = x
        self._y = y

    @property
    def get_direction(self):
        """
        Returns the value of the private attribute _direction.
        """
        return self._direction

    def display_arrow(self, screen):
        """
        Displays the arrow on top of the screen.
        Args:
            screen:
                The background surface initialized using pygame on which the
                game is displayed.
        """
        screen.blit(self._surface, (self._x, self._y))

    def update(self):
        """
        Changes the arrow's y position. When run in the game loop, the arrow
        will move up the screen by 2 pixels.
        """
        self._y -= 2

    def at_top_screen(self):
        """
        Returns True when the arrow is partially off-screen, or when the
        arrow's y-position is less than -60. If the arrow is still
        properly on-screen, returns False.
        """
        if self._y < -60:
            return True
        return False

    def __repr__(self) -> str:
        """
        Returns a human-readable format of the direction.
        """
        return f"{self._direction}"


class PlayerArrow(Arrow):
    """
    A subclass of the Arrow class that initializes arrows on the "player"
    side of the screen.
    """
    def __init__(self, direction):
        """
        Constructs all necessary attributes for positioning the
        computer arrows.
        """
        super().__init__(direction)

    def position(self):
        """
        Uses the parent class function set_position to initialize the starting
        position of the player arrows on the screen depending on which
        direction arrow it is.
        """
        if self._direction == "up":
            self.set_position(913, 600)
        if self._direction == "left":
            self.set_position(1000, 600)
        if self._direction == "right":
            self.set_position(1150, 600)
        if self._direction == "down":
            self.set_position(1077, 600)

    def type(self):
        """
        Returns a string that indicates to a user which class arrow it is.
        """
        return "player"


class ComputerArrow(Arrow):
    """
    A subclass of the Arrow class that initializes arrows on the "computer"
    side of the screen.
    """
    def __init__(self, direction):
        """
        Constructs all necessary attributes for positioning the
        computer arrows.
        """
        super().__init__(direction)

    def position(self):
        """
        Uses the parent class function set_position to initialize the starting
        position of the computer arrows on the screen depending on which
        direction arrow it is.
        """
        if self._direction == "up":
            self.set_position(15, 600)
        if self._direction == "left":
            self.set_position(105, 600)
        if self._direction == "right":
            self.set_position(257, 600)
        if self._direction == "down":
            self.set_position(180, 600)

    def type(self):
        """
        Returns a string that indicates to a user which class arrow it is.
        """
        return "computer"


def computer_produce_arrow(computer_arrows, arrows_on_screen):
    """
    A function that produces a random arrow when called and adds the
    directional arrow to a corresponding list. This function is specifically
    used to produce arrows on the computer's side.

    Arguments:
        -computer_arrows: a list of arrows the computer produces
        -arrows_on screen: a list of arrows currently on the screen
    Returns:
        -computer_arrows: a list of arrows the computer produces
        -arrows_on screen: a list of arrows currently on the screen
    """
    arrows = ["up", "left", "right", "down"]

    random_arrow = random.choice(arrows)
    new_arrow = ComputerArrow(random_arrow)
    new_arrow.position()
    print(new_arrow.get_position())

    computer_arrows.append(new_arrow)

    arrows_on_screen.append(random_arrow)

    return computer_arrows, arrows_on_screen

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
