from assets.Coin import Coin
from assets.Ennemy_static import Ennemy_static
from assets.Area import Area
from assets.levels.Level import Level

class DQNLevel1(Level):

    def __init__(self, width:int, height:int):
        
        coins = []
        ennemies = []
        ennemies.append(Ennemy_static(0, 200, 600, 5))
        ennemies.append(Ennemy_static(200, 400, 600, 5))

        super().__init__(coins, ennemies, Area(0,0,False), Area(width-40, height-40,True), width, height)