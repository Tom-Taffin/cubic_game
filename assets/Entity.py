from assets import Element
import pygame as pg

import game


class Entity(Element):
    def __init__(self, x:int, y:int, length:int, width:int, color:pg.Color, deltaX:int, deltaY:int):
        self.super(x,y,length,width,color)
        self._deltaX = deltaX
        self._deltaY = deltaY

    def get_deltaX(self):
        return self._deltaX
    
    def get_deltaY(self):
        return self._deltaY
    
    def set_deltaX(self, v:int):
        self._deltaX = v
    
    def set_deltaY(self, v:int):
        self._deltaY = v
    
    def move(self, game:game):
        self._x += self._deltaX
        self._y += self._deltaY
        