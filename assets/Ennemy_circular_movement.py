import pygame as pg
import math

from assets.Entity import Entity


class Ennemy_circular_movement(Entity):
    def __init__(self, x:int, y:int, radius:int, speed:float, angle:float=0):
        super().__init__(x,y,30,30,pg.Color(255,0,0),0,0)
        self.radius = radius
        self.speed = speed
        self.center_x = x
        self.center_y = y
        self.angle = angle
    
    def move(self, board_width:int, board_height:int):
        self.angle += self.speed
        self._rect.x = self.center_x + self.radius * math.cos(self.angle)
        self._rect.y = self.center_y + self.radius * math.sin(self.angle)
        