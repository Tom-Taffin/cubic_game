
import pygame as pg

from assets.Entity import Entity


class Ennemy_snake_tail(Entity):
    def __init__(self,head,speed):
        super().__init__(-100,-100,30,30,pg.Color(255,0,0),0,0)
        self._head = head
        self.init_tick = 200//speed
        self.tick = self.init_tick
        self.futur_x = self._head._rect.x
        self.futur_y = self._head._rect.y
    
    def move(self, board_width:int, board_height:int):
        """takes the old position of his head"""
        self.tick -= 1
        if self.tick <= 0:
            self.tick = self.init_tick
            self._rect.x = self.futur_x
            self._rect.y = self.futur_y
            self.futur_x = self._head._rect.x
            self.futur_y = self._head._rect.y
    