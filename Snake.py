from config import *
from random import randint
import pygame as pg

class Snake:
    def __init__(self,x_cells,y_cells):
        self.x_cells = x_cells
        self.y_cells = y_cells
        self.vel=[0,0]
        self.length = 1
        self.body = [[randint(0,int(self.x_cells)-1),randint(0,int(self.y_cells)-1)]]

    def move(self,move,food):
        # 0 => none  1 => up  2 => left  3 => down  4 => right
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

        if self.body[0][0]==food.food_location[0] and self.body[0][1]==food.food_location[1]:
            food.Respawn_food()
            self.length += 1
            self.body.append(self.body[-1].copy())
        
        buffer = self.body[0].copy()
        for i , body_part in enumerate(self.body):
            if i!=0:
                sec_buff = body_part.copy()
                body_part[0]=buffer[0]
                body_part[1]=buffer[1]
                buffer = sec_buff

        # sets the motion of head
        self.body[0][0] += self.vel[0]
        self.body[0][1] += self.vel[1]

        # appear from another side
        if self.body[0][0]<0:self.body[0][0]=self.x_cells-1
        if self.body[0][0]>=self.x_cells:self.body[0][0]=0

        if self.body[0][1]<0:self.body[0][1]=self.y_cells-1
        if self.body[0][1]>=self.y_cells:self.body[0][1]=0


