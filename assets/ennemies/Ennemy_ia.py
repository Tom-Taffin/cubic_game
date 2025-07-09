import pygame as pg

from assets.Entity import Entity
from assets.Player import Player


class Ennemy_ia(Entity):
    """
    Square that chases the player
    """
    def __init__(self, x:int, y:int, speed:int, player:Player):
        super().__init__(x,y,30,30,pg.Color(255,0,0),0,0)
        self._speed = speed/10
        self._player = player
        self.init_tick = 200//speed
        self.tick = self.init_tick
    
    def move(self, board_width:int, board_height:int):
        dx = comp(self._player.get_x(), self._rect.x) * self._speed
        dy = comp(self._player.get_y(), self._rect.y) * self._speed
        self._deltaX += dx
        self._deltaY += dy
        self.tick -= 1
        if self.tick <= 0:
            self.tick = self.init_tick
            super().move(board_width,board_height)
            self._deltaX = 0
            self._deltaY = 0
        
def comp(a:int, b:int):
    if a<b:
        return -1
    if a>b:
        return 1
    return 0