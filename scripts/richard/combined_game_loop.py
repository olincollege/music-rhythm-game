import pygame as pg
from sys import exit 
from arrow import Arrow
import random
import pygame 

pg.init()
pygame.mixer.init()

timer = 0 
showarrows = True
WIDTH, HEIGHT = 1280, 720


class Scene:
    def start(self):
        pass

    def update(self, events, dt):
        pass

    def exit(self):
        pass

class Menu(Scene):
    def __init__(self, screen, scenes):
        self.scenes  = scenes
        self.screen  = screen
        self.font    = pygame.font.SysFont('freesansbold.ttf', 32)
        self.music   = pygame.mixer.Sound("assets/soundtrack/base beat.wav")
        self.channel = pygame.mixer.Channel(0)

    def start(self):
        self.channel.play(self.music, loops=-1, fade_ms=0)

    def update(self, events, dt):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                left_click, *_ = pygame.mouse.get_pressed()
                if left_click:
                    return self.scenes['tutorial']

        self.screen.blit(self.font.render("Menu", True, 'white'), (WIDTH/2 - 20, 100))
        return self

    def exit(self):
        self.channel.stop()

class Tutorial(Scene):
    def __init__(self, screen, scenes):
        self.scenes = scenes
        self.screen = screen
        self.font = pygame.font.SysFont('freesansbold.ttf', 32)
        self.music = pygame.mixer.Sound("../assets/soundtrack/tutorial.wav")
        self.channel = pygame.mixer.Channel(0)
        self.timer = 0

    def start(self):
        self.channel.play(self.music, loops=-1, fade_ms=0)

    def update(self, events, dt):
        # Go back to menu if there hasn't been any events for 5 seconds.

        self.timer += dt
        print(f"tutorial: {self.timer}")
        if self.timer >= 9.5:
            return self.scenes['transition']

        self.screen.blit(self.font.render("Tutorial HERE", True, 'white'), (WIDTH / 15, 190))
        return self

    def exit(self):
        self.channel.stop()

class Transition(Scene):
    def __init__(self, screen, scenes):
        self.scenes = scenes
        self.screen = screen
        self.font = pygame.font.SysFont('freesansbold.ttf', 32)
        self.music = pygame.mixer.Sound("../assets/soundtrack/transition music.wav")
        self.channel = pygame.mixer.Channel(0)
        self.timer = 0

    def start(self):
        self.channel.play(self.music, loops=-1, fade_ms=0)

    def update(self, events, dt):
        # Go to the game once the transition is done.

        self.timer += dt
        if self.timer >= 19:
            return self.scenes['game']

        self.screen.blit(self.font.render("Transition", True, 'white'), (WIDTH / 15, 240))
        return self

    def exit(self):
        self.channel.stop()

class Game(Scene):
    def __init__(self, screen, scenes):
        self.scenes = scenes
        self.screen = screen
        self.font = pygame.font.SysFont('freesansbold.ttf', 32)
        self.music = pygame.mixer.Sound("../assets/soundtrack/demo 4 melodies.wav")
        self.channel = pygame.mixer.Channel(0)
        self.timer = 0

    def start(self):
        self.channel.play(self.music, loops=-1, fade_ms=0)
        print("playing" + str(timer))
        pass

    def update(self, events, dt):
        self.timer += dt
        if self.timer >= 38:
            return self.scenes['menu']
        
        # self.screen.blit(self.font.render("Game", True, 'white'), (WIDTH / 15, 290))
        return self

    def exit(self):
        self.channel.stop()

#screen size
size = (WIDTH, HEIGHT)
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
pg.time.set_timer(add_arrow, 1200)

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
    
dt = clock.tick(60)/1000
# print("tick " + str(pygame.time.get_ticks()))

screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
clock  = pygame.time.Clock()

# All the scenes.
scenes = {}
scenes['menu'] = Menu(screen, scenes)
scenes['tutorial'] = Tutorial(screen, scenes)
scenes['transition'] = Transition(screen,scenes)
scenes['game'] = Game(screen, scenes)

# Start with the menu.
scene = scenes['game']
scene.start()
    


while True:
    events = pg.event.get()
    timer = timer + dt
    print(timer)
    # Switch scenes if there is a new scene.
    new_scene = scene.update(events, dt)

    if new_scene is not scene:
        # print("new scene")
        # If there is a new scene, make sure to allow the old
        # scene to exit and the new scene to start.
        scene.exit()
        scene = new_scene
        scene.start()

    #pygame.display.update()
    
    for event in events:
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
    
  
    screen.fill("Red")
    #moves the arrow 
    for arrow in up_arrows + down_arrows + right_arrows + left_arrows:
        arrow.display_arrow(screen)
        arrow.update()
        print("updating")
        
    #stationary arrows
    left.display_arrow(screen)
    down.display_arrow(screen)
    up.display_arrow(screen)
    right.display_arrow(screen)

    # updates whats on screen everytime loop runs through
    pg.display.update()
    #60 fps
    clock.tick(60)/1000