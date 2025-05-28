from assets.Coin import Coin
from assets.Entity import Entity
from assets.Area import Area
from assets.Timer import Timer

class Level:

    def __init__(self, coins:list[Coin], ennemies:list[Entity], entry:Area, exit:Area, width:int, height:int, timer:Timer = None):
        self.coins = coins
        self.ennemies = ennemies
        self.entry = entry
        self.exit = exit
        self._width = width
        self._height = height
        self.timer = timer

    def restore(self):
        self.__init__(self._width,self._height)

    def update(self):
        pass