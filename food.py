from config import *
from random import randint
import pygame as pg

class Food:
    def __init__(self,x_cells,y_cells):
        self.x_cells = x_cells
        self.y_cells = y_cells
        self.food_location = (randint(0,int(self.x_cells)-1),randint(0,int(self.y_cells)-1))
    
    def Respawn_food(self):
        self.food_location = (randint(0,int(self.x_cells)-1),randint(0,int(self.y_cells)-1))
    
