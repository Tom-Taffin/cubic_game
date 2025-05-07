from assets.Element import Element
import pygame as pg


class Entity(Element):
    def __init__(self, x:int, y:int, length:int, width:int, color:pg.Color, deltaX:int, deltaY:int):
        super().__init__(x,y,length,width,color)
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
    
    def move(self, board_length:int, board_width:int):
        self._x += self._deltaX
        self._y += self._deltaY
        