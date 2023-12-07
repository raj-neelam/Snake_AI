from config import *
from random import randint
import pygame as pg

class Snake:
    def __init__(self,x_cells,y_cells):
        self.x_cells = x_cells
        self.y_cells = y_cells
        self.vel=[0,0]
        self.snake_head_location = [randint(0,int(self.x_cells)-1),randint(0,int(self.y_cells)-1)]
    
    def move(self,move):
        # 0 => none
        # 1 => up
        # 2 => left
        # 3 => down
        # 4 => right

        # sets the vel
        if move==1:
            self.vel[1] = -1
            self.vel[0] = 0
        elif move==2:
            self.vel[0] = -1
            self.vel[1] = 0
        elif move==3:
            self.vel[1] = 1
            self.vel[0] = 0
        elif move==4:
            self.vel[0] = 1
            self.vel[1] = 0

        # sets the motion of head
        self.snake_head_location[0] += self.vel[0]
        self.snake_head_location[1] += self.vel[1]

        if self.snake_head_location[0]<0:self.snake_head_location[0]=self.x_cells-1
        if self.snake_head_location[0]>=self.x_cells:self.snake_head_location[0]=0

        if self.snake_head_location[1]<0:self.snake_head_location[1]=self.y_cells-1
        if self.snake_head_location[1]>=self.y_cells:self.snake_head_location[1]=0