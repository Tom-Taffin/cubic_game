from assets.Explosion import Explosion
from assets.Player import Player
from assets.Ennemy_snake import Ennemy_snake


class Ennemy_snake_self_kill(Ennemy_snake):
    def __init__(self, x:int, y:int, speed:int, player:Player, length:int):
        super().__init__(x,y,speed,player,length)
        self.explosions = []

    def self_kill(self):
        for i in range(2,len(self.ennemies)):
            if self.ennemies[0].is_collision(self.ennemies[i]):
                for ennemy in self.ennemies[i:]:
                    self.explosions.append(Explosion(ennemy.get_x(),ennemy.get_y(),30,30))
                self.ennemies = self.ennemies[:i]
                break

    def move(self, board_width, board_height):
        super().move(board_width, board_height)
        self.self_kill()
    
    def draw(self, screen):
        super().draw(screen)
        for explosion in self.explosions:
            explosion.update(screen)
            if explosion.is_finish():
                self.explosions.remove(explosion)
        if len(self.ennemies) <= 15:
            for ennemy in self.ennemies:
                self.explosions.append(Explosion(ennemy.get_x(),ennemy.get_y(),30,30))
                self.ennemies = []

    def is_kill(self):
        return len(self.ennemies)==0

        
