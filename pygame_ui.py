import pygame as pg
from game import level_length

pg.display.set_caption("Wörtre")

SCREEN_HEIGHT, SCREEN_WIDTH = 600, 400
SCREEN = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pg.font.Font("Grandstander-Bold.ttf", 20)


while run:        
    for event in pg.event.get():
        if event.type == pg.QUIT:                
            run = False
    pg.display.update()


pg.quit()