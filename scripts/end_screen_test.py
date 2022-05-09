import pygame as pg
from cats import Cat
pg.init()
WIDTH, HEIGHT = 1280, 720
PINK = (255, 16, 240)

bg = pg.image.load("scripts/assets/imgs/end screen.png")
screen = pg.display.set_mode((WIDTH, HEIGHT))

total_score = 10

font = pg.font.Font('Eczar-SemiBold.ttf', 40)
text = font.render(str(total_score), True, PINK)
while True:
    screen.blit(bg, (0,0))
    screen.blit(text, (645,610))
    pg.display.update()