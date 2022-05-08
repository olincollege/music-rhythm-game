"""
final combined game loop
"""

# Import the necessary functions and pygame
import pygame as pg
from pygame.locals import *
from sys import exit
from arrow import *
import random
from scene import *

# initialize pygame
pg.init()

# Set up the screen
WIDTH = 1280
HEIGHT = 720
size = (WIDTH, HEIGHT)
screen = pg.display.set_mode(size)

# Function to produce a random arrow
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

# Game setup
game_timer = 0
showarrows = True
BPM = 100  # tempo of the song
DELAY = 3.74

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

# Start with the menu.
scene = scenes["menu"]
scene.start()

# Produce arrows only when arrows are needed

# initialized stationary arrows at top of screen
up = Arrow(90, 10, 20)
left = Arrow(180, 100, 20)
down = Arrow(270, 180, 20)
right = Arrow(0, 255, 10)

# lists to keep track of arrows on screen
arrows_on_screen = []
up_arrows = []
left_arrows = []
right_arrows = []
down_arrows = []

song_information = [1, 1, 1, 1, 4,
                    1, 1, 1, 1, 4,
                    1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
                    1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
                    0.5, 0.5, 0.5, 0.5, 1, 2, 0.5, 0.5, 1, 1,
                    0.5, 0.5, 0.5, 0.5, 1, 2, 0.5, 0.5, 1, 1,
                    0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.5, 0.5, 1, 1 , 1, 1,
                    0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.5,0.5, 1, 1 , 1, 1,
                                    ]


def melody_arrow_generator(BPM, song_info):
    """
    Each int in the song_info list corresponds to how many beats that note will
    last. For example, a 1 means it will last 1 beat (a quarter note). A 4 means
    it will last 4 beats (a whole note)

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
            quarter_note_length = quarter_note_length - 11
        if note == 0.5:
            quarter_note_length = quarter_note_length - 52
        if note == 0.25:
            pass
            quarter_note_length = quarter_note_length - 114

        next_notes.append(quarter_note_length*note/1000)
    return next_notes

add_arrow = pg.USEREVENT + 0
add_arrow_event = pg.event.Event(add_arrow)


deletion = 0
counter = 0
saved_time = 0
next_notes = melody_arrow_generator(BPM, song_information)
print(next_notes)
next_note = next_notes[0]

while True:

    # if game_timer % length == True:
    #     pg.time.set_timer(add_arrow, length)
    game_timer = game_timer + dt
    print (f"game timer {game_timer}")

    if scene == scenes["game"]:
        if deletion == 1:
            # print(f"game timer before{game_timer}")
            game_timer -= 0.012
            # print(f"game timer after{game_timer}")
            deletion = 0

        # The intro before the game begins = DELAY
        if game_timer > DELAY:
            if game_timer > next_note + saved_time and counter <\
                len(next_notes):

                pg.event.post(add_arrow_event)
                # print(f"post time added {game_timer - saved_time}")
                next_note = next_notes[counter]
                saved_time = game_timer
                # print(f"counter {counter}")
                counter += 1

    events = pg.event.get()

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
            # print(f"produce game_timer: {game_timer}")
            produce_arrow()  # creates an arrow every 833 milliseconds

        # keybinds
        if event.type == pg.KEYDOWN:
            # print(f"deleting {i}")
            if event.key == pg.K_UP and up_arrows:
                # point_total += score_points(up_arrows[0]._y)
                deletion += 1
                del up_arrows[0]
            if event.key == pg.K_DOWN and down_arrows:
                deletion += 1
                del down_arrows[0]
            if event.key == pg.K_RIGHT and right_arrows:
                deletion += 1
                del right_arrows[0]
            if event.key == pg.K_LEFT and left_arrows:
                deletion += 1
                del left_arrows[0]

    # display the arrows at the top of the screen if not in menu
    if scene != scenes["menu"]:

        # display moving arrows if not in menu or transition scene
        if scene != scenes["transition"]:
            for arrow in up_arrows + down_arrows + right_arrows + left_arrows:
                # move the arrow
                arrow.update()
                arrow.display_arrow(screen)

                # print("updating")

        # stationary arrows
        left.display_arrow(screen)
        down.display_arrow(screen)
        up.display_arrow(screen)
        right.display_arrow(screen)

    # updates whats on screen everytime loop runs through
    pg.display.update()
    # 60 fps
    clock.tick(60)/1000