
import pygame as pg

from assets.Entity import Entity


class Ennemy_static(Entity):
    def __init__(self, x:int, y:int, width:int, height:int):
        super().__init__(x,y,width,height,pg.Color(255,0,0),0,0)