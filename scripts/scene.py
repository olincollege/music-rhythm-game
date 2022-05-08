"""
Scene classes 
"""
# Imports
import pygame
from cats import Cat
import os
os.chdir(os.path.dirname(os.path.abspath("/home/ideluis42/music-rhythm-game")))

WIDTH, HEIGHT = 1280, 720
pygame.init()
pygame.mixer.init()

class Background(pygame.sprite.Sprite):
    
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


class Scene:
    def start(self):
        pass

    def update(self, events, dt):
        pass

    def exit(self):
        pass


class Menu(Scene):
    def __init__(self, screen, scenes):
        self.scenes = scenes
        self.screen = screen
        self.font = pygame.font.SysFont('freesansbold.ttf', 32)
        self.music = pygame.mixer.Sound("/assets/soundtrack/base beat.wav")
        self.channel = pygame.mixer.Channel(0)
        self.background = Background('/assets/imgs/menu.png', [0, 0])

    def start(self):
        self.screen.blit(self.background.image, self.background.rect)
        self.channel.play(self.music, loops=-1, fade_ms=0)

    def update(self, events, dt):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return self.scenes['game']
        self.screen.blit(self.background.image, self.background.rect)
        #self.screen.blit(self.font.render("Menu", True, 'white'), (WIDTH/2 - 20, 100))
        return self

    def exit(self):
        self.channel.stop()


class Game(Scene):
    def __init__(self, screen, scenes):
        self.scenes = scenes
        self.screen = screen
        self.font = pygame.font.SysFont('freesansbold.ttf', 32)
        self.music = pygame.mixer.Sound(
            "/assets/soundtrack/melodies with intro.wav")
        self.channel = pygame.mixer.Channel(0)
        self.game_timer = 0
        self.background = Background('/assets/imgs/Background.png', [0, 0])
        # Background Cats
        self.dj_cat = Cat("dj", 460, 350)
        self.speaker_cat = Cat("speaker", 500, 65)

        # Team 1 Cats
        self.piano_cat = Cat("piano", 1000, 300)
        self.guitar_cat = Cat("guitar", 700, 350)
        self.drum_cat = Cat("drum", 850, 225)

        # Team 2 Cats
        self.piano_cat_2 = Cat("piano", -50, 300, True)
        self.guitar_cat_2 = Cat("guitar", 205, 350, True)
        self.drum_cat_2 = Cat("drum", 77, 225, True)

    def start(self):
        self.channel.play(self.music, loops=0, fade_ms=0)
        self.screen.blit(self.background.image, self.background.rect)

        # Cat display
        self.dj_cat.display(self.screen)
        self.drum_cat.display(self.screen)
        self.piano_cat.display(self.screen)
        self.speaker_cat.display(self.screen)
        self.guitar_cat.display(self.screen)
        self.drum_cat_2.display(self.screen)
        self.piano_cat_2.display(self.screen)
        #self.backgroundguitar_cat_2.display(self.screen)

        #print("playing" + str(game_timer))
        pass

    def update(self, events, dt):
        self.game_timer += dt
        if self.game_timer >= 42.3:
            return self.scenes['menu']
        self.screen.blit(self.background.image, self.background.rect)

        return self

    def exit(self):
        self.channel.stop()