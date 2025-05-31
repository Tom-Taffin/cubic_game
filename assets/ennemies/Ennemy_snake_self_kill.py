from assets.Animation import Animation
from assets.Player import Player
from assets.ennemies.Ennemy_snake_can_die import Ennemy_snake_can_die


class Ennemy_snake_self_kill(Ennemy_snake_can_die):
    def __init__(self, x:int, y:int, speed:int, player:Player, length:int):
        super().__init__(x,y,speed,player,length)

    def self_kill(self):
        for i in range(2,len(self.ennemies)):
            if self.ennemies[0].is_collision(self.ennemies[i]):
                for ennemy in self.ennemies[i:]:
                    self.explosions.append(Animation("explosion",ennemy.get_x(),ennemy.get_y(),30,30))
                self.ennemies = self.ennemies[:i]
                break

    def move(self, board_width, board_height):
        super().move(board_width, board_height)
        self.self_kill()
    
    def draw(self, screen):
        super().draw(screen)
        if len(self.ennemies) <= 15:
            for ennemy in self.ennemies:
                self.explosions.append(Animation("explosion",ennemy.get_x(),ennemy.get_y(),30,30))
            self.ennemies = []

        
