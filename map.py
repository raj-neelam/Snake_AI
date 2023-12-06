from config import *
import pygame as pg
from random import randint

class Snake_map:
    def __init__(self,window):
        self.window = window
        self.width = window.get_width()
        self.height = window.get_height()
        self.x_cells = self.width/block_size
        self.y_cells = self.height/block_size
        self.extera_space_x = (self.x_cells-int(self.x_cells))*block_size
        self.extera_space_y = (self.y_cells-int(self.y_cells))*block_size

        self.food_location = (randint(0,int(self.x_cells)),randint(0,int(self.y_cells)))

    def Respawn_food(self):
        self.food_location = (randint(0,int(self.x_cells)-1),randint(0,int(self.y_cells)-1))
    
    def draw_food(self):
        pg.draw.rect(self.window,food_col,(self.food_location[0]*block_size,self.food_location[1]*block_size,block_size,block_size))
    
    def draw_grid(self):
        for x in range(int(self.x_cells)+1):
            pg.draw.line(self.window, grid_col, ((x*block_size)+self.extera_space_x/2,self.extera_space_y/2), ((x*block_size)+self.extera_space_x/2,self.height-self.extera_space_y/2))
        for y in range(int(self.y_cells)+1):
            pg.draw.line(self.window, grid_col, (self.extera_space_x/2,(y*block_size)+self.extera_space_y/2), (self.width-self.extera_space_x/2,(y*block_size)+self.extera_space_y/2))
