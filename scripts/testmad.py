import pygame as pg
from sys import exit 
import arrow as ar
import random

from score import score_calc

pg.init()

#screen size
size = (1280, 720)
screen = pg.display.set_mode(size)


#window title
pg.display.set_caption("catJAM")

#initialized stationary arrows at top of screen
# up = Arrow("up", 10, 20)
# left = Arrow("left", 100, 20)
# down = Arrow("down", 180, 20)
# right = Arrow("right", 255, 10)

measure = 0
notelength = (1200, 1200, 600)
length = 1200
#produce arrow event 
add_arrow = pg.USEREVENT + 0
pg.time.set_timer(add_arrow, length)

arrow_melody_1 = pg.USEREVENT + 1
pg.time.set_timer(arrow_melody_1, 1200)

#lists to keep track of arrows on screen
arrows_on_screen = []
computer_arrows = []
player_arrows = [[], [], [], []]


pup_arrows = []
pleft_arrows = []
pright_arrows = []
pdown_arrows = []

total_score = 0

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

#game clock (fps)
clock = pg.time.Clock()

#game loop
while True:
  print(f"ticks: {pg.time.get_ticks()}")
  # if pg.time.get_ticks() % 1200 == 0:
  #   pg.time.set_timer(add_arrow, length)

#allows them to quit
  for event in pg.event.get():
    if event.type == pg.QUIT:
      pg.quit()
      exit() #a python built-in way to exit loop/code without errors popping up

    if event.type == add_arrow:
        #computer_produce_arrow() #creates an arrow every 833 milliseconds
      #if len(arrows_on_screen) < 4:
      if measure < 4:
        if measure == 2:
          length = 600
        computer_produce_arrow()
        measure += 1
        
        #has a brief pause where player side produces arrows 
      #elif len(arrows_on_screen) >= 4:
      elif measure >= 4:
        player_produce_arrow()
        measure += 1
        arrows_on_screen.pop(0)
        if measure == 8:
          measure = 0
  
  #keybinds
    if event.type == pg.KEYDOWN:

      if event.key == pg.K_UP:
      #if the number of up arrows in the player's side is not zero, then you can delete the first arrow when key is pressed
        if len(player_arrows[0]) != 0:
          total_score += score_calc(player_arrows[0][0]._y, "up")
          del player_arrows[0][0]
          

      elif event.key == pg.K_LEFT:
        if len(player_arrows[1]) != 0:
          total_score += score_calc(player_arrows[1][0]._y, "left")
          del player_arrows[1][0]
          

      elif event.key == pg.K_RIGHT:
        if len(player_arrows[2]) != 0:
          total_score += score_calc(player_arrows[2][0]._y, "right")
          del player_arrows[2][0]
          
          
      elif event.key == pg.K_DOWN:
        if len(player_arrows[3]) != 0:
          total_score += score_calc(player_arrows[3][0]._y, "down")
          del player_arrows[3][0]
          
  #print(total_score)
#TEMPORARY screen to view the arrows 
  screen.fill("Red")            
  
#shows and moves the arrow 
  new_computer_arrows = [[], [], [], []]
  new_player_arrows = [[], [], [], []]


  for arrow in computer_arrows:
    arrow.display_arrow(screen)
    arrow.update()

  for type in player_arrows:
    for arrow in type:
      arrow.display_arrow(screen)
      arrow.update()


#potential off screen delete solution
  for arrow in computer_arrows + player_arrows[0] + player_arrows[1] + player_arrows[2] + player_arrows[3]:

    if arrow.at_top_screen():
      if arrow.type() == "computer":
        computer_arrows.remove(arrow)
      
      elif arrow.type() == "player":

        if arrow.get_direction() == "up":
          #player_arrows[0].remove(arrow)
          player_arrows[0].remove(arrow)

        elif arrow.get_direction() == "left":

          player_arrows[1].remove(arrow)

        elif arrow.get_direction() == "right":

          player_arrows[2].remove(arrow)

        elif arrow.get_direction() == "down":
          player_arrows[3].remove(arrow)








  #pg.time.delay(1000)
#stationary arrows
  # left.display_arrow(screen)
  # down.display_arrow(screen)
  # up.display_arrow(screen)
  # right.display_arrow(screen)

  # updates whats on screen everytime loop runs through
  pg.display.update()
  #60 fps
  clock.tick(30)/1000

