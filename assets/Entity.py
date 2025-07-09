from assets.Element import Element
import pygame as pg


class Entity(Element):
    """Element that moves"""
    def __init__(self, x:int, y:int, width:int, height:int, color:pg.Color, deltaX:int, deltaY:int):
        super().__init__(x,y,width,height,color)
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
    
    def move(self, board_width:int, board_height:int):
        self._rect.move_ip(self._deltaX,self._deltaY)
        