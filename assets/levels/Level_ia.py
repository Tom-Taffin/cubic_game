from assets.Coin import Coin
from assets.Ennemy_snake_self_kill import Ennemy_snake_self_kill
from assets.Area import Area
from assets.levels.Level import Level
from assets.Player import Player

class Level_ia(Level):

    def __init__(self, width:int, height:int, player:Player):
    
        coins = []
        ennemies = [Ennemy_snake_self_kill(600,600,23,player,80)]

        super().__init__(coins, ennemies, Area(0,0,False), Area(-100, -100,True), width, height)
        self.player = player

    def restore(self):
        self.__init__(self._width,self._height,self.player)

    def update(self):
        if self.ennemies[0].is_kill():
            self.exit._rect.x = self._width-40
            self.exit._rect.y = self._height-40