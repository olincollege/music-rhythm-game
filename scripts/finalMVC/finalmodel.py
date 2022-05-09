"""
Model of catJAM game
Note from Isa:
Some more unused arguments--richard take a look and see if we actually need
those
"""
# Disabled pylint warnings that would break our game if fixed
# pylint: disable=wildcard-import
# pylint: disable=no-member
# pylint: disable=unused-wildcard-import
# pylint: disable=invalid-name

import pygame
import random
from finalview import *
from finalcontroller import *
pygame.init()

class Game():
    """
    A Game interface scene for catJAM

    Attributes:
        scenes: the dictionary containing all of the scenes to be cycled through
        screen: the dimensions of the screen the scene will be placed on
        music: the music associated with the menu screen
        channel: the channel that said music will be played on
        background: an instance of the Background class with the background
                    image

    """

    def __init__(self, screen, scenes):
        """
        Creates an instance of the Game class.
        """
        self.scenes = scenes
        self.screen = screen
        self.font = pygame.font.SysFont('freesansbold.ttf', 32)
        self.music = pygame.mixer.Sound(
            "../assets/soundtrack/melodies with intro.wav")
        self.channel = pygame.mixer.Channel(0)
        self.game_timer = 0
        self.background = Background('../assets/imgs/Background.png', [0, 0])

    def start(self):
        """
        Starts the scene by laying down the background image and playing the
        music
        """
        self.channel.play(self.music, loops=0, fade_ms=0)
        self.screen.blit(self.background.image, self.background.rect)
        #print("playing" + str(game_timer))


    def update(self, events, dt):
        """
        Updates the screen based on what events have occured. If the soundtrack
        has finished playing, return to the menu class.

        Args:
            events (list): a list of all of the events that have occured in one
                           cycle of the game loop
            dt (int): the amount of time that has passed since the last cycle of
                      the game loop

        Returns:
            self.scenes['menu']: the Menu class, the next scene, if 40 seconds
                                 pass.
            self: essentially, nothing, if 40 seconds has not passed.
        """
        self.game_timer += dt
        if self.game_timer >= 40:
            return self.scenes['exit']
        self.screen.blit(self.background.image, self.background.rect)

        return self

    def exit(self):
        """
        Stops the music upon exit to avoid layering of soundtracks.
        """
        self.channel.stop()


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
        self._surface = pg.image.load("../assets/imgs/arrow_sprite.png").\
            convert_alpha()

        if direction == "up":
            self._surface = pg.image.load("../assets/imgs/green_arrow.png")\
                .convert_alpha()
            self._surface = pg.transform.rotate(self._surface, 90)
        if direction == "down":
            self._surface = pg.image.load("../assets/imgs/blue_arrow.png").\
                convert_alpha()
            self._surface = pg.transform.rotate(self._surface, 270)
        if direction == "right":
            self._surface = pg.image.load("../assets/imgs/yellow_arrow.png").\
                convert_alpha()
            self._surface = pg.transform.rotate(self._surface, 0)
        if direction == "left":
            self._surface = pg.image.load("../assets/imgs/pink_arrow.png").\
                convert_alpha()
            self._surface = pg.transform.rotate(self._surface, 180)

        self._surface = pg.transform.smoothscale(self._surface, (95, 95))
        self._direction = direction
        self._x = 0
        self._y = 0

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
        self._y -= 10

    def at_top_screen(self):
        """
        Returns True when the arrow is partially off-screen, or when the
        arrow's y-position is less than -60. If the arrow is still
        properly on-screen, returns False.
        """
        if self._y < -60:
            return True
        return False

    def __repr__(self) -> (str):
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

    def class_type(self):
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

    def class_type(self):
        """
        Returns a string that indicates to a user which class arrow it is.
        """
        return "computer"        
        
def melody_arrow_generator(BPM, song_info):
    """
    Each int in the song_info list corresponds to how many beats that note will
    last.
    For example, a 1 means it will last 1 beat (a quarter note). A 4 means it
    will last 4 beats (a whole note)

    Args:
        BPM: an int containing the beats per minute of a tempo
        song_info: a list containing the length of the melody notes for a song. 

    Returns: A list containing the arrow information for a melody
    """
    next_notes = []
    
    multiplier = 1.75
    for note in song_info:
        quarter_note_length = 60*1000/BPM
        # error correction for game lag
        if note == 4:
            quarter_note_length = quarter_note_length - 60*multiplier
        if note == 2:
            quarter_note_length = quarter_note_length - 48*multiplier
        if note == 1:
            quarter_note_length = quarter_note_length - 36*multiplier
        if note == 0.5:
            quarter_note_length = quarter_note_length - 48*multiplier
        if note == 0.25:
            quarter_note_length = quarter_note_length - 70*multiplier

        next_notes.append(quarter_note_length*note/1000)
    return next_notes

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
    # print(new_arrow.get_position())

    computer_arrows.append(new_arrow)

    arrows_on_screen.append(random_arrow)

    return computer_arrows, arrows_on_screen

def score_calc(y_position, arrow_type):
    """
    Function to determine the score a player receives after they stop the arrow
    from moving

    Arguments:
        -y_position: an integer value representing the y-position of the arrow
                     when the player stopped it.
        -arrow_type: a string representing the type of arrow (left, right, down,
                     up)
    
    Returns:
        -score: the score gained (will need to be added on total score in main 
                function)
    """

    
    if arrow_type == "right":
        ARROW_POSITION = 10
    else:
        ARROW_POSITION = 20

    diff = abs(ARROW_POSITION - y_position)
    score = 0

    if diff == 0:
        score += 1
    elif diff > 0 and diff <= 10:
        score += .9
    elif diff > 10 and diff <= 20:
        score += .8
    elif diff > 20 and diff <= 30:
        score += .7
    elif diff > 30 and diff <= 40:
        score += .6
    elif diff > 40 and diff <= 50:
        score += .5
    elif diff > 50 and diff <= 60:
        score += .4
    elif diff > 60 and diff <= 70:
        score += .3
    elif diff > 70 and diff <= 80:
        score += .2
    elif diff > 80 and diff <= 90:
        score += .1
    elif diff > 90:
        score += 0

    return score

