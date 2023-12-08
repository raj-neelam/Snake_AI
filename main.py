import pygame as pg
from time import time
from config import *
from Game import Snake_Game

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
            return (False,0)
        
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                pg.quit()
                return (False,0)
            if event.key == pg.K_UP:return (True,1)
            if event.key == pg.K_LEFT:return (True,2)
            if event.key == pg.K_DOWN:return (True,3)
            if event.key == pg.K_RIGHT:return (True,4)
    return (True,0)


snake_Game = Snake_Game(window)
loop_run = True
time_eclipsed=0
set_move=0

while loop_run:
    loop_run, move = run()
    if move!=0:set_move=move

    current_fps=clock.get_fps()
    dt = 1/current_fps if current_fps!=0  else 0.001
    time_eclipsed += dt

    # snake_Game.draw_grid()
    snake_Game.draw_game()
    
    if time_eclipsed>step_time:
        time_eclipsed = 0
        snake_Game.step(set_move)


    