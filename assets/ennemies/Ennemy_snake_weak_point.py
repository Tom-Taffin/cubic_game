import pygame as pg
from assets.Explosion import Explosion
from assets.Player import Player
from assets.ennemies.Ennemy_snake_can_die import Ennemy_snake_can_die


class Ennemy_snake_weak_point(Ennemy_snake_can_die):
    def __init__(self, x:int, y:int, speed:int, player:Player, length:int):
        super().__init__(x,y,speed,player,length)
        self.explosions = []
        self.player = player
        self.ennemies[-1]._color = pg.Color(0,255,255)

    def move(self, board_width, board_height):
        if not self.is_kill():
            super().move(board_width, board_height)
            if self.ennemies[-1].is_collision(self.player):
                for ennemy in self.ennemies[-10:]:
                    self.explosions.append(Explosion(ennemy.get_x(),ennemy.get_y(),30,30))
                self.ennemies = self.ennemies[:-10]
                if not self.is_kill():
                    self.ennemies[-1]._color = pg.Color(0,255,255)

    def is_collision(self, other):
        for ennemy in self.ennemies[:-1]:
            if ennemy.is_collision(other):
                return True
        return False



        
