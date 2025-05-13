from assets.Coin import Coin
from assets.Ennemy import Ennemy
from assets.Area import Area

class Level:

    def __init__(self, coins:list[Coin], ennemies:list[Ennemy], entry:Area, exit:Area, width:int, height:int):
        self.coins = coins
        self.ennemies = ennemies
        self.entry = entry
        self.exit = exit
        self._width = width
        self._height = height