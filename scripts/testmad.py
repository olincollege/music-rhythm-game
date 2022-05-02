from turtle import right
import pygame as pg
from sys import exit 
from arrow import Arrow
import random

pg.init()

#screen size
size = (1080, 720)
screen = pg.display.set_mode(size)


#window title
pg.display.set_caption("catJAM")

#initialized stationary arrows at top of screen
up = Arrow(90, 10, 20)
left = Arrow(180, 100, 20)
down = Arrow(270, 180, 20)
right = Arrow(0, 255, 10)

#produce arrow event 
add_arrow = pg.USEREVENT + 0
pg.time.set_timer(add_arrow, 833)

#lists to keep track of arrows on screen
arrows_on_screen = []
up_arrows = []
left_arrows = []
right_arrows = []
down_arrows = []

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



#game clock (fps)
clock = pg.time.Clock()

#game loop
while True:
#allows them to quit
  for event in pg.event.get():
    if event.type == pg.QUIT:
      pg.quit()
      exit() #a python built-in way to exit loop/code without errors popping up

    if event.type == add_arrow:
        produce_arrow() #creates an arrow every 833 milliseconds

    #keybinds
    if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP and up_arrows:
              # point_total += score_points(up_arrows[0]._y)
              del up_arrows[0]
            if event.key == pg.K_DOWN and down_arrows:
              del down_arrows[0]
            if event.key == pg.K_RIGHT and right_arrows:
              del right_arrows[0]
            if event.key == pg.K_LEFT and left_arrows:
              del left_arrows[0]

  #TEMPORARY screen to view the arrows 
  screen.fill("Red")            

#moves the arrow 
  for arrow in up_arrows + down_arrows + right_arrows + left_arrows:
    arrow.display_arrow(screen)
    arrow.update()

#stationary arrows
  left.display_arrow(screen)
  down.display_arrow(screen)
  up.display_arrow(screen)
  right.display_arrow(screen)

  # updates whats on screen everytime loop runs through
  pg.display.update()
  #60 fps
  clock.tick(30)/1000

