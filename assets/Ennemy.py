
import pygame as pg

from assets.Entity import Entity


class Enemy(Entity):
    def __init__(self, x:int, y:int, deltaX:int, deltaY:int):
        super().__init__(x,y,15,15,pg.Color(255,0,0),deltaX,deltaY)
    
    def move(self, board_length:int, board_width:int):
        super().move(board_length,board_width)
        if self._x > board_length:
            self._x = board_length
            self._deltaX *= -1
        if self._y > board_width:
            self._y = board_width
            self._deltaY *= -1