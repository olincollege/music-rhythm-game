from math import prod
import pygame as pg
from sys import exit
from arrow import Arrow
import arrow as ar
import random
import pygame
import threading
from score import score_calc
from cats import Cat
pg.init()
game_timer = 0
showarrows = True
WIDTH, HEIGHT = 1280, 720
BPM = 100  # tempo of the song
# DELAY = 3.59
DELAY = 3.74
# DELAY = 3.44 # Changes based on arrow speed.


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
            self.scenes['game']: the Game class, the next scene, if the space bar
                                 is pressed
            self: essentially, nothing, if none of the events is the space bar.
        """
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return self.scenes['exit']
        return self

    def exit(self):
        """
        Stops the music upon exit to avoid layering of soundtracks.
        """
        self.channel.stop()

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


def produce_arrow():
    """
    A function that produces a random arrow when called.
    """
    arrows = ["up", "left", "right", "down"]

    random_arrow = random.choice(arrows)

    if random_arrow == "up":
        new_arrow = Arrow(90, 10, 600)
        up_arrows.append(new_arrow)

    elif random_arrow == "left":
        new_arrow = Arrow(180, 100, 600)
        left_arrows.append(new_arrow)

    elif random_arrow == "right":
        new_arrow = Arrow(0, 255, 590)
        right_arrows.append(new_arrow)

    elif random_arrow == "down":
        new_arrow = Arrow(270, 180, 600)
        down_arrows.append(new_arrow)

    arrows_on_screen.append(new_arrow)

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
    
    for note in song_info:
        quarter_note_length = 60*1000/BPM
        # error correction for game lag
        if note == 4:
            quarter_note_length = quarter_note_length - 48
        if note == 2:
            quarter_note_length = quarter_note_length - 60
        if note == 1:
            quarter_note_length = quarter_note_length - 13
        if note == 0.5:
            quarter_note_length = quarter_note_length - 50
        if note == 0.25:
            quarter_note_length = quarter_note_length - 115

        next_notes.append(quarter_note_length*note/1000)
    return next_notes

def computer_produce_arrow():
    """
    A function that produces a random arrow when called and adds the
    directional arrow to a corresponding list. This function is specifically
    used to produce arrows on the computer's side.
    """
    arrows = ["up", "left", "right", "down"]

    random_arrow = random.choice(arrows)
    new_arrow = ar.ComputerArrow(random_arrow)
    new_arrow.position()

    computer_arrows.append(new_arrow)
  
    arrows_on_screen.append(random_arrow)

def player_produce_arrow():
  """
  This function produces arrows on the arrow's side based off the pattern
  of arrows that the computer sides function.
  """
  if arrows_on_screen[0] == "up": 
    copy_arrow = ar.PlayerArrow("up")
    copy_arrow.position()
    player_arrows[0].append(copy_arrow)

  elif arrows_on_screen[0] == "left":
    copy_arrow = ar.PlayerArrow("left")
    copy_arrow.position()
    player_arrows[1].append(copy_arrow)

  elif arrows_on_screen[0] == "right":
    copy_arrow = ar.PlayerArrow("right")
    copy_arrow.position()
    player_arrows[2].append(copy_arrow)

  elif arrows_on_screen[0] == "down":
    copy_arrow = ar.PlayerArrow("down")
    copy_arrow.position()
    player_arrows[3].append(copy_arrow)
    
# screen size
size = (WIDTH, HEIGHT)
screen = pg.display.set_mode(size)

# window title
pg.display.set_caption("catJAM")

# game clock (fps)
clock = pg.time.Clock()

dt = clock.tick(60)/1000

screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
clock = pygame.time.Clock()

# All the scenes.
scenes = {}
scenes["menu"] = Menu(screen, scenes)
scenes["game"] = Game(screen, scenes)
scenes["exit"] = Exit(screen, scenes)
# Start with the menu.
scene = scenes["menu"]
scene.start()

# Produce arrows only when arrows are needed

# initialized stationary arrows at top of screen
comp_up = Arrow("up")
comp_up.set_position(10,20)
comp_left = Arrow("left")
comp_left.set_position(100, 20)
comp_down = Arrow("down")
comp_down.set_position(180, 20)
comp_right = Arrow("right")
comp_right.set_position(255,10)


p_up = Arrow("up")
p_up.set_position(910,20)
p_left = Arrow("left")
p_left.set_position(1000, 20)
p_down = Arrow("down")
p_down.set_position(1080, 20)
p_right = Arrow("right")
p_right.set_position(1155,10)
# # Background Cats

# dj_cat = Cat("dj", 460, 350)
# speaker_cat = Cat("speaker", 500, 65)

# # Team 1 Cats
# piano_cat = Cat("piano", 1000, 300)
# guitar_cat = Cat("guitar", 700, 350)
# drum_cat = Cat("drum", 850, 225)

# # Team 2 Cats
# piano_cat_2 = Cat("piano", -50, 300, True)
# guitar_cat_2 = Cat("guitar", 205, 350, True)
# drum_cat_2 = Cat("drum", 77, 225, True)
# # lists to keep track of arrows on screen

up_arrows = []
left_arrows = []
right_arrows = []
down_arrows = []

song_information = [1, 1, 1, 1, 4,
                    1, 1, 1, 1, 4,
                    1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 0.5, 0.5,
                    0.5,
                    1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 0.5, 0.5,
                    0.5,
                    0.5, 0.5, 0.5, 0.5, 1, 2, 0.5, 0.5, 1, 1,
                    0.5, 0.5, 0.5, 0.5, 1, 2, 0.5, 0.5, 1, 1,
                    0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25,
                    0.25, 0.25, 0.5, 0.5, 1, 1, 1, 1,
                    0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25,
                    0.25, 0.25, 0.5, 0.5, 1, 1, 1, 1,
                                    ]
num_notes = [5, 10, 24, 38,48,58,76,94]
arrows_on_screen = []
computer_arrows = []
player_arrows = [[], [], [], []]
total_score = 0


add_arrow = pg.USEREVENT + 0
add_arrow_event = pg.event.Event(add_arrow)


deletion = 0
counter = 0
saved_time = 0
next_notes = melody_arrow_generator(BPM, song_information)
print(next_notes)
next_note = next_notes[0]
melody = 0
while True:

    # if game_timer % length == True:
    #     pg.time.set_timer(add_arrow, length)
    game_timer = game_timer + dt
    # print (f"game timer {game_timer}")

    if scene == scenes["game"]:
        if deletion == 1:
            # print(f"game timer before{game_timer}")
            game_timer -= 0.012
            # print(f"game timer after{game_timer}")
            deletion = 0

        # The intro before the game begins = DELAY
        if game_timer > DELAY:
            if game_timer > next_note + saved_time and counter < len\
                (next_notes):
                pg.event.post(add_arrow_event)
                print(f"post time added {game_timer - saved_time}")
                next_note = next_notes[counter]
                saved_time = game_timer
                # print(f"counter {counter}")
                counter += 1

    events = pg.event.get()
    # print(type(events))
    # print(game_timer)
    # Switch scenes if there is a new scene.
    new_scene = scene.update(events, dt)
    # print (i)

    if new_scene is not scene:
        # print("new scene")
        # If there is a new scene, make sure to allow the old
        # scene to exit and the new scene to start.
        scene.exit()
        scene = new_scene
        game_timer = 0
        scene.start()

    # pygame.display.update()

    for event in events:
        if event.type == pg.QUIT:
            pg.quit()
            exit()

        if event.type == add_arrow and game_timer > DELAY:
            print(f"melody: {melody}")
            print(f"counter: {counter}")
            if counter <= num_notes[melody]:
                if melody % 2 == 0:
                    computer_produce_arrow()
                else:
                    player_produce_arrow()
                    arrows_on_screen.pop(0)
            else:
                melody += 1
            
        #keybinds
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
            #if the number of up arrows in the player's side is not zero, 
            # then you can delete the first arrow when key is pressed
                if len(player_arrows[0]) != 0:
                    total_score += score_calc(player_arrows[0][0]._y, "up")
                try:
                    del player_arrows[0][0]
                except:
                    pass

            elif event.key == pg.K_LEFT:
                if len(player_arrows[1]) != 0:
                    total_score += score_calc(player_arrows[1][0]._y, "left")
                try:
                    del player_arrows[1][0]
                except:
                    pass
            
            elif event.key == pg.K_RIGHT:
                if len(player_arrows[2]) != 0:
                    total_score += score_calc(player_arrows[2][0]._y, "right")
                try:
                    del player_arrows[2][0]
                except:
                    pass
            
            elif event.key == pg.K_DOWN:
                if len(player_arrows[3]) != 0:
                    total_score += score_calc(player_arrows[3][0]._y, "down")
                try:
                    del player_arrows[3][0]
                except: 
                    pass
            

    # display the arrows at the top of the screen if not in menu
    if scene != scenes["menu"]:
        new_computer_arrows = [[], [], [], []]
        new_player_arrows = [[], [], [], []]
          # display moving arrows if not in menu scene
        for arrow in computer_arrows:
            arrow.display_arrow(screen)
            arrow.update()

        for class_type in player_arrows:
            for arrow in class_type:
                arrow.display_arrow(screen)
                arrow.update()

        # stationary arrows
        comp_left.display_arrow(screen)
        comp_down.display_arrow(screen)
        comp_up.display_arrow(screen)
        comp_right.display_arrow(screen)
        
        p_left.display_arrow(screen)
        p_down.display_arrow(screen)
        p_up.display_arrow(screen)
        p_right.display_arrow(screen)
        # dj_cat.display(screen)
        
        # drum_cat.display(screen)
        # piano_cat.display(screen)
        # speaker_cat.display(screen)
        # guitar_cat.display(screen)

        # drum_cat_2.display(screen)
        # piano_cat_2.display(screen)
        # guitar_cat_2.display(screen)
    
#potential off screen delete solution
    for arrow in computer_arrows + player_arrows[0] + player_arrows[1] + \
        player_arrows[2] + player_arrows[3]:
        if arrow.at_top_screen():
            if arrow.class_type() == "computer":
                computer_arrows.remove(arrow)
            
            elif arrow.class_type() == "player":
                if arrow.get_direction() == "up":
                    #player_arrows[0].remove(arrow)
                    player_arrows[0].remove(arrow)

                elif arrow.get_direction() == "left":
                    player_arrows[1].remove(arrow)

                elif arrow.get_direction() == "right":
                    player_arrows[2].remove(arrow)

                elif arrow.get_direction() == "down":
                    player_arrows[3].remove(arrow)
    # updates whats on screen everytime loop runs through
    pg.display.update()
    # 60 fps
    clock.tick(60)/1000
