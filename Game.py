from config import *
import pygame as pg
from food import *
from Snake import *
from random import randint

class Snake_Game:
    def __init__(self,window):
        self.window = window
        self.width=window.get_width()
        self.height=window.get_height()
        self.x_cells = window.get_width()/block_size
        self.y_cells = window.get_height()/block_size
        self.extera_space_x = (self.x_cells-int(self.x_cells))*block_size
        self.extera_space_y = (self.y_cells-int(self.y_cells))*block_size

        self.food = Food(self.x_cells,self.y_cells)
        self.snake = Snake(self.x_cells,self.y_cells)
    
    def draw_game(self):
        # drawing food 
        self.draw_rect(self.food.food_location, food_col)
        
        # drawing snake
        self.draw_snake()
        
    def draw_snake(self):
        for body_part in self.snake.body:
            self.draw_rect(body_part, snake_head_col)
            self.draw_rect(body_part, bg_col, snake_boder)
    
    def draw_rect(self, ind, col, scale_down=0):
        pg.draw.rect(self.window, col, 
                     ((ind[0]*block_size)+(self.extera_space_x/2)+((block_size*scale_down)),
                      (ind[1]*block_size)+(self.extera_space_y/2)+((block_size*scale_down)),
                      block_size*(1-scale_down*2),
                      block_size*(1-scale_down*2)))

    def step(self,move=0):
        self.snake.move(move,self.food)

    def draw_grid(self):
        for x in range(int(self.x_cells)+1):
            pg.draw.line(self.window, grid_col, ((x*block_size)+self.extera_space_x/2,self.extera_space_y/2), ((x*block_size)+self.extera_space_x/2,self.height-self.extera_space_y/2))
        for y in range(int(self.y_cells)+1):
            pg.draw.line(self.window, grid_col, (self.extera_space_x/2,(y*block_size)+self.extera_space_y/2), (self.width-self.extera_space_x/2,(y*block_size)+self.extera_space_y/2))
