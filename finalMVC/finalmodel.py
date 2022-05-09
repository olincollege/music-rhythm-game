"""
-Game Class: put here cuz tis the game duh lmao
"""


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
        pass

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
            self.scenes['menu']: the Menu class, the next scene, if 42.3 seconds
                                 pass.
            self: essentially, nothing, if 42.3 seconds has not passed.
        """
        self.game_timer += dt
        if self.game_timer >= 42.3:
            return self.scenes['exit']
        self.screen.blit(self.background.image, self.background.rect)

        return self

    def exit(self):
        """
        Stops the music upon exit to avoid layering of soundtracks.
        """
        self.channel.stop()