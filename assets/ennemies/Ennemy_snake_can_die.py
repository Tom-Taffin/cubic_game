from assets.Player import Player
from assets.ennemies.Ennemy_snake import Ennemy_snake


class Ennemy_snake_can_die(Ennemy_snake):
    def __init__(self, x:int, y:int, speed:int, player:Player, length:int):
        super().__init__(x,y,speed,player,length)
        self.explosions = []
    
    def draw(self, screen):
        super().draw(screen)
        for explosion in self.explosions:
            explosion.update(screen)
            if explosion.is_finish():
                self.explosions.remove(explosion)

    def is_kill(self):
        return len(self.ennemies)==0

        
