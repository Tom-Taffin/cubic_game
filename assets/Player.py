
import pygame as pg

from assets.Entity import Entity

PLAYER_SPEED = 5

class Player(Entity):
    def __init__(self, x:int, y:int):
        super().__init__(x,y,30,30,pg.Color(255,255,255), 0, 0)
    
    def move(self, board_width:int, board_height:int):
        super().move(board_width,board_height)
        if self.get_x() < 0:
            self._rect.x = 0
        if self.get_y() < 0:
            self._rect.y = 0
        if self.get_x() > board_width - self.get_width():
            self._rect.x = board_width - self.get_width()
        if self.get_y() > board_height - self.get_height():
            self._rect.y = board_height - self.get_height()
    
    def update(self, board_width:int, board_height:int):
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
        self.move(board_width, board_height)
    
    def step(self, action:int, board_width:int, board_height:int):
        self._deltaX = 0
        self._deltaY = 0
        if action == 1:
            self._deltaY = -PLAYER_SPEED
        if action == 2:
            self._deltaX = PLAYER_SPEED
        if action == 3:
            self._deltaY = PLAYER_SPEED
        if action == 4:
            self._deltaX = -PLAYER_SPEED
        self.move(board_width, board_height)