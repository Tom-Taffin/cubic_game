from assets.Coin import Coin
from assets.ennemies.Ennemy_snake_self_kill import Ennemy_snake_self_kill
from assets.Area import Area
from assets.Entity import Entity
from assets.Timer import Timer
from assets.levels.Level import Level
from assets.Player import Player

class Level_Boss(Level):

    def __init__(self, coins:list[Coin], ennemies:list[Entity], width:int, height:int, player:Player, timer:Timer = None):

        super().__init__(coins, ennemies, Area(0,0,False), Area(-100, -100,True), width, height, timer)
        self.player = player

    def restore(self):
        self.__init__(self._width,self._height,self.player)

    def update(self):
        if self.ennemies[0].is_kill():
            self.exit._rect.x = self._width-40
            self.exit._rect.y = self._height-40