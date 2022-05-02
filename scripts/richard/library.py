import pygame

WIDTH, HEIGHT = 1280, 720

"""
Below are the scene classes for musical and visual transitions in the game
"""
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
        self.music   = pygame.mixer.Sound("../assets/soundtrack/base beat.wav")
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

    def update(self, events, dt):
        # Go back to menu if there hasn't been any events for 5 seconds.
        self.timer += dt
        if self.timer >= 38:
            return self.scenes['menu']


        self.screen.blit(self.font.render("Game", True, 'white'), (WIDTH / 15, 290))
        return self

    def exit(self):
        self.channel.stop()


"""
Helper functions
"""

    # All the scenes.
def initialize_scenes():
    scenes = {}
    scenes['menu'] = Menu(screen, scenes)
    scenes['tutorial'] = Tutorial(screen, scenes)
    scenes['transition'] = Transition(screen,scenes)
    scenes['game'] = Game(screen, scenes)