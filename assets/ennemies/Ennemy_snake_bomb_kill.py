from assets.Animation import Animation
from assets.Player import Player
from assets.ennemies.Ennemy_snake_can_die import Ennemy_snake_can_die
from assets.ennemies.Ennemy_static import Ennemy_static


class Ennemy_snake_bomb_kill(Ennemy_snake_can_die):
    def __init__(self, x:int, y:int, speed:int, player:Player, length:int, bombs:list[Ennemy_static]):
        super().__init__(x,y,speed,player,length)
        self.bombs = bombs

    def move(self, board_width, board_height):
        if not self.is_kill():
            super().move(board_width, board_height)
            for bombs in self.bombs:
                if bombs.is_collision(self.ennemies[0]):
                    self.bombs.remove(bombs)
                    for ennemy in self.ennemies:
                        self.explosions.append(Animation("explosion",ennemy.get_x(),ennemy.get_y(),30,30))
                    self.ennemies = []
                    break
    
    def draw(self, screen):
        super().draw(screen)
        for bomb in self.bombs:
            bomb.draw(screen)

    def is_collision(self, other):
        for bomb in self.bombs:
            if bomb.is_collision(other):
                return True
        return super().is_collision(other)
        
