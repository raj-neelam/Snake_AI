import pygame as pg
from time import time
from config import *
from map import Snake_map

pg.init()

clock = pg.time.Clock()

if width==0 or height==0:
    window = pg.display.set_mode((0,0), pg.FULLSCREEN)
    width,height = window.get_width,window.get_height
else:
    window = pg.display.set_mode((width,height))

def run():
    pg.display.update()
    clock.tick(fps)
    current_fps = clock.get_fps()
    pg.display.set_caption(f"{name}  |  fps : {round(current_fps,2)}")
    
    window.fill(bg_col)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            return False
        
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                pg.quit()
                return False
    return True

dt = 1/(clock.get_fps()+0.0001)

snake_map = Snake_map(window)


while run():
    current_fps=clock.get_fps()
    dt = 1/current_fps if current_fps!=0  else 0.0001

    # snake_map.draw_grid()
    snake_map.draw_food()

    