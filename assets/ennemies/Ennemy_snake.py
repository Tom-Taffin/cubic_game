import pygame as pg
from assets.Player import Player
from assets.ennemies.Ennemy_ia import Ennemy_ia
from assets.ennemies.Ennemy_snake_tail import Ennemy_snake_tail
from assets.Entity import Entity

class Ennemy_snake(Entity):
    def __init__(self, x:int, y:int, speed:int, player:Player, length:int):
        head = Ennemy_ia(x,y,speed,player)
        self.ennemies = [head]
        tmp = head
        for _ in range(length-1):
            tmp = Ennemy_snake_tail(tmp,speed)
            self.ennemies.append(tmp)
        
    def is_collision(self, other):
        for ennemy in self.ennemies:
            if ennemy.is_collision(other):
                return True
        return False
    
    def move(self, board_width, board_height):
        for ennemy in self.ennemies:
            ennemy.move(board_width, board_height)

    def draw(self, screen : pg.display):
        for ennemy in self.ennemies:
            ennemy.draw(screen)