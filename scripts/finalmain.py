"""
Main game loop for catJAM
"""
# Disabled pylint errors that would break our game if fixed
# pylint: disable=wildcard-import
# pylint: disable=no-member
# pylint: disable=bare-except
# pylint: disable=protected-access
# pylint: disable=consider-using-sys-exit
# pylint: disable=expression-not-assigned
# pylint: disable=unused-wildcard-import
# pylint: disable=invalid-name
from finalcontroller import *
from finalmodel import *
from finalview import *

pg.init()
game_timer = 0
showarrows = True
WIDTH, HEIGHT = 1280, 720
BPM = 100  # tempo of the song

# Add in a delay for the arrows to error correct
# Changes based on arrow speed.
# DELAY = 3.59
DELAY = 3.74
# DELAY = 3.22 
# DELAY = 3

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

dj_cat = Cat("dj", 460, 350)
speaker_cat = Cat("speaker", 500, 65)

# Team 1 Cats
piano_cat = Cat("piano", 1000, 300)
guitar_cat = Cat("guitar", 700, 350)
drum_cat = Cat("drum", 850, 225)

# Team 2 Cats
piano_cat_2 = Cat("piano", -50, 300, True)
guitar_cat_2 = Cat("guitar", 205, 350, True)
drum_cat_2 = Cat("drum", 77, 225, True)


# lists to keep track of arrows on screen

up_arrows = []
left_arrows = []
right_arrows = []
down_arrows = []

song_information = [1, 1, 1, 1, 4,
                    1, 1, 1, 1, 4.2,
                    1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 0.5, 0.5,
                    0.5,
                    1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 0.5, 0.5,
                    0.5,    
                    0.5, 0.5, 0.5, 0.5, 1, 2, 0.5, 0.5, 1, 0.85,
                    0.5, 0.5, 0.5, 0.5, 1, 2, 0.5, 0.5, 1, 0.85,
                    0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25,
                    0.25, 0.25, 0.5, 0.5, 1, 1, 1, 1,
                    0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25,
                    0.25, 0.25, 0.5, 0.5, 1, 1, 1, 1,
                                    ]
num_notes = [5, 5, 13, 12,9,9,17 ,17]
arrows_on_screen = []
computer_arrows = []
player_arrows = [[], [], [], []]
total_score = 0


add_arrow = pg.USEREVENT + 0
add_arrow_event = pg.event.Event(add_arrow)


deletion = 0
note_counter = 0
melody_counter = 0
saved_time = 0
next_notes = melody_arrow_generator(BPM, song_information)
# print(next_notes)
next_note = next_notes[0]
melody = 0


    
while True:
    # if scene == scenes["game"]:
        

    # if game_timer % length == True:
    #     pg.time.set_timer(add_arrow, length)
    game_timer = game_timer + dt
    # print (f"game timer {GAME_TIMER}")

    if scene == scenes["game"]:
 
        if deletion == 1:
            # print(f"game timer before{game_timer}")
            game_timer -= 0.08
            # print(f"game timer after{game_timer}")
            deletion = 0

        # The intro before the game begins = DELAY
        if game_timer > DELAY:
            if game_timer > next_note + saved_time and note_counter < \
                len(next_notes):
                pg.event.post(add_arrow_event)
                # print(f"post time added {game_timer - saved_time}")
                next_note = next_notes[note_counter]
                saved_time = game_timer
                # print(f"counter {counter}")
                note_counter += 1
                melody_counter += 1

    events = pg.event.get()
    # print(type(events))
    # print(game_timer)
    # Switch scenes if there is a new scene.
    if scene != scenes['exit']:
        new_scene = scene.update(events, dt)
    else:
        new_scene = scene.update(events, round(total_score,2))
    # print (i)

    if new_scene is not scene:
        # print("new scene")
        # If there is a new scene, make sure to allow the old
        # scene to exit and the new scene to start.
        scene.exit()
        print("In here")
        scene = new_scene
        game_timer = 0
        scene.start()

    # pygame.display.update()

    for event in events:
        if event.type == pg.QUIT:
            pg.quit()
            exit()

        if event.type == add_arrow and game_timer > DELAY:
            # print(f"melody: {melody}")
            # print(f"melody_counter: {melody_counter}")

            # if the number of notes in this melody is greater than the
            # number of notes for this melody
            if melody_counter > num_notes[melody]:
                # go onto the next melody
                melody += 1
                # reset the counter
                melody_counter = 0

            # If the melody number is divisible by 2, that means it's the
            # computer's turn
            if melody % 2 == 0:
                print("computer")
                computer_produce_arrow(computer_arrows,arrows_on_screen)
            else:
                print("player")
                try:
                    player_produce_arrow(player_arrows,arrows_on_screen)
                    arrows_on_screen.pop(0)
                except IndexError:
                    print("back to the computer")

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
    if scene == scenes["game"]:
        dj_cat.display(screen)
        drum_cat.display(screen)
        piano_cat.display(screen)
        speaker_cat.display(screen)
        guitar_cat.display(screen)
        drum_cat_2.display(screen)
        piano_cat_2.display(screen)
        guitar_cat_2.display(screen)
        
        # new_computer_arrows = [[], [], [], []]
        # new_player_arrows = [[], [], [], []]
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
