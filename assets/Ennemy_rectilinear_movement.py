
import pygame as pg

from assets.Entity import Entity


class Ennemy_rectilinear_movement(Entity):
    def __init__(self, x:int, y:int, deltaX:int, deltaY:int):
        super().__init__(x,y,30,30,pg.Color(255,0,0),deltaX,deltaY)
    
    def move(self, board_width:int, board_height:int):
        super().move(board_width,board_height)
        if self.get_x() < 0:
            self._rect.x = 0
            self._deltaX *= -1
        if self.get_y() < 0:
            self._rect.y = 0
            self._deltaY *= -1
        if self.get_x() > board_width - self.get_width():
            self._rect.x = board_width - self.get_width()
            self._deltaX *= -1
        if self.get_y() > board_height - self.get_height():
            self._rect.y = board_height - self.get_height()
            self._deltaY *= -1