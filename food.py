from config import *
from random import randint,choice
import pygame as pg

class Food:
    def __init__(self,x_cells,y_cells):
        self.x_cells = x_cells
        self.y_cells = y_cells
        self.food_location = (randint(0,int(self.x_cells)-1),randint(0,int(self.y_cells)-1))
    
    def Respawn_food(self,snake):
        cells = [(i,j) for i in range(int(self.x_cells)) for j in range(int(self.y_cells))]
        # cells.remove(tuple(self.food_location))
        for body_part in snake.body:
            cells.remove((int(body_part[0]),int(body_part[1])))
        self.food_location = choice(cells)
