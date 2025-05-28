from assets.Coin import Coin
from assets.ennemies.Ennemy_rectilinear_movement import Ennemy_rectilinear_movement
from assets.Area import Area
from assets.levels.Level import Level

class Level_coin(Level):

    def __init__(self, width:int, height:int):
    
        coins = []
        for i in range(60,width,100):
            for j in range(0,height,100):
                coins.append(Coin(i,j))
        ennemies = []
        for i in range(60,width-30, 100):
            ennemies.append(Ennemy_rectilinear_movement(i,height,0,7))

        super().__init__(coins, ennemies, Area(0,0,False), Area(width-40, height-40,True), width, height)