"""
View for catJAM game
Note from Isa:
This file has some unused argument pylint warnings--are the arguments essential
to our game?
"""
import pygame

# Disable pylint warnings that would break our game if fixed
# pylint: disable=too-few-public-methods
# pylint: disable=invalid-name
# pylint: disable=no-member
class Background(pygame.sprite.Sprite):
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
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pygame.image.load(image_file)
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
        self.music = pygame.mixer.Sound("../assets/soundtrack/base beat.wav")
        self.channel = pygame.mixer.Channel(0)
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
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
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
        self.music = pygame.mixer.Sound("../assets/soundtrack/tutorial.wav")
        self.channel = pygame.mixer.Channel(0)
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
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                pass
        return self

    def exit(self):
        """
        Stops the music upon exit to avoid layering of soundtracks.
        """
        self.channel.stop()
