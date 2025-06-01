from assets.ennemies.Ennemy_snake_bomb_kill import Ennemy_snake_bomb_kill
from assets.ennemies.Ennemy_static import Ennemy_static
from assets.levels.Level_Boss import Level_Boss
from assets.Player import Player

class Level6_stage1(Level_Boss):

    def __init__(self, width:int, height:int, player:Player):
    
        coins = []
        bombs = [Ennemy_static(width//4,height//2,30,30),Ennemy_static(width//2,height//2,30,30),Ennemy_static(3*width//4,height//2,30,30)]
        ennemies = [Ennemy_snake_bomb_kill(width,0,40,player,5,bombs),Ennemy_snake_bomb_kill(0,height,25,player,5,bombs),Ennemy_snake_bomb_kill(width,height,35,player,5,bombs)]

        super().__init__(coins, ennemies, width, height, player)

    def update(self, screen):
        wait = super().update(screen)
        if wait:
            return wait
        for ennemy in self.ennemies:
            if not ennemy.is_kill():
                self.exit._rect.x = -100
                self.exit._rect.y = -100
                return False
        self.exit._rect.x = self._width-40
        self.exit._rect.y = self._height-40
        return False