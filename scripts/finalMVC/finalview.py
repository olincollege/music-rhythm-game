"""
View for catJAM game
Note from Isa:
This file has some unused argument pylint warnings--are the arguments essential
to our game?
"""
import pygame as pg


# Disable pylint warnings that would break our game if fixed
# pylint: disable=too-few-public-methods
# pylint: disable=invalid-name
# pylint: disable=no-member
class Background(pg.sprite.Sprite):
    """
    A Background class that helps define

    Args:
        A pygame.sprite.Sprite: an image file to convert into the background
    """
    def __init__(self, image_file, location):
        """
        Creates a new instance of a background

        Args:
            image_file (.png): an image file
            location (string): the place to put that image.
        """
        pg.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pg.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


class Menu():
    """
    A menu interface scene for catJAM

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
        Creates a new instance of Menu.
        """
        self.scenes = scenes
        self.screen = screen
        self.music = pg.mixer.Sound("../assets/soundtrack/base beat.wav")
        self.channel = pg.mixer.Channel(0)
        self.background = Background('../assets/imgs/menu.png', [0, 0])

    def start(self):
        """
        Starts the scene by laying down the background image and playing the
        music
        """
        self.screen.blit(self.background.image, self.background.rect)
        self.channel.play(self.music, loops=-1, fade_ms=0)

    def update(self, events, dt):
        """
        Updates the screen based on what events have occured. If the space bar
        has been pressed in the menu, move to the Game class.

        Args:
            events (list): a list of all of the events that have occured in one
                           cycle of the game loop
            dt (int): the amount of time that has passed since the last cycle of
                      the game loop

        Returns:
            self.scenes['game']: the Game class, the next scene, if the space
                                 bar is pressed
            self: essentially, nothing, if none of the events is the space bar.
        """
        for event in events:
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                return self.scenes['game']
        return self

    def exit(self):
        """
        Stops the music upon exit to avoid layering of soundtracks.
        """
        self.channel.stop()


class Exit():
    """
    A menu interface scene for catJAM

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
        Creates a new instance of Exit.
        """
        self.scenes = scenes
        self.screen = screen
        self.music = pg.mixer.Sound("../assets/soundtrack/tutorial.wav")
        self.font = pg.font.Font('Eczar-SemiBold.ttf', 40)
        self.channel = pg.mixer.Channel(0)
        self.background = Background("../assets/imgs/end screen.png", [0, 0])

    def start(self):
        """
        Starts the scene by laying down the background image and playing the
        music
        """
        self.screen.blit(self.background.image, self.background.rect)
        self.channel.play(self.music, loops=-1, fade_ms=0)

    def update(self, events, total_score):
        """
        Updates the screen based on what events have occured.

        Args:
            events (list): a list of all of the events that have occured in one
                           cycle of the game loop
            dt (int): the amount of time that has passed since the last cycle of
                      the game loop

        Returns:
            self.scenes['game']: the Game class, the next scene, if the space
                                 bar is pressed
            self: essentially, nothing, if none of the events is the space bar.
        """
        for event in events:
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()

        text = self.font.render(str(total_score), True, (255, 16, 240))
        self.screen.blit(text, (645,610))
        return self

    def exit(self):
        """
        Stops the music upon exit to avoid layering of soundtracks.
        """
        self.channel.stop()


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
                ("../assets/imgs/pianocat.png").convert_alpha()
            self._surface = pg.transform.smoothscale(self._surface, (300, 300))
        elif cat == "speaker":
            self._surface = pg.image.load\
            ("../assets/imgs/Speakers Cat Temp Sprite.png").convert_alpha()
            self._surface = pg.transform.smoothscale(self._surface, (250, 250))
        elif cat == "guitar":
            self._surface = pg.image.load\
               ("../assets/imgs/guitarcat.png").convert_alpha()
            self._surface = pg.transform.smoothscale(self._surface, (350, 350))
        elif cat == "dj":
            self._surface = pg.image.load("../assets/imgs/djcat.png")\
            .convert_alpha()
            self._surface = pg.transform.smoothscale(self._surface, (325, 325))
        elif cat == "drum":
            self._surface = pg.image.load("../assets/imgs/drumcat.png")\
            .convert_alpha()
            self._surface = pg.transform.smoothscale(self._surface, (300, 300))

        if mirrored:
            if cat == "piano":
                self._surface = pg.image.load\
                ("../assets/imgs/backcat2.png").convert_alpha()
                self._surface = pg.transform.smoothscale(self._surface, \
                    (300, 300))
                self._surface = pg.transform.flip(self._surface, True, False)

            elif cat == "guitar":
                self._surface = pg.image.load\
                ("../assets/imgs/guitarcat2.png").convert_alpha()
                self._surface = pg.transform.smoothscale(self._surface, \
                    (350, 350))
                self._surface = pg.transform.flip(self._surface, True, False)
            elif cat == "drum":
                self._surface = pg.image.load("../assets/imgs/backcat.png")\
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
        
    