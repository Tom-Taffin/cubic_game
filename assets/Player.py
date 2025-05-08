
import pygame as pg

from assets.Entity import Entity

PLAYER_SPEED = 5

class Player(Entity):
    def __init__(self, x:int, y:int):
        super().__init__(x,y,30,30,pg.Color(255,255,255), 0, 0)
    
    def move(self, board_length:int, board_width:int):
        super().move(board_length,board_width)
        if self._x < 0:
            self._x = 0
        if self._y < 0:
            self._y = 0
        if self._x > board_length - self._length:
            self._x = board_length - self._length
        if self._y > board_width - self._width:
            self._y = board_width - self._width
    
    def update(self, board_length:int, board_width:int):
        self._deltaX = 0
        self._deltaY = 0
        keys = pg.key.get_pressed()
        if keys[pg.K_w] or keys[pg.K_UP]:
            self._deltaY = -PLAYER_SPEED
        if keys[pg.K_s] or keys[pg.K_DOWN]:
            self._deltaY = PLAYER_SPEED
        if keys[pg.K_a] or keys[pg.K_LEFT] :
            self._deltaX = -PLAYER_SPEED
        if keys[pg.K_d] or keys[pg.K_RIGHT]:
            self._deltaX = PLAYER_SPEED
        self.move(board_length, board_width)