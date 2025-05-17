from assets.Coin import Coin
from assets.Ennemy import Ennemy
from assets.Area import Area
from assets.Level import Level

class Level2(Level):

    def __init__(self, width:int, height:int):
    
        coins = []
        for i in range(60,width,100):
            for j in range(0,height,100):
                coins.append(Coin(i,j))
        ennemies = []
        for i in range(60,width-30, 100):
            ennemies.append(Ennemy(i,height,0,7))

        super().__init__(coins, ennemies, Area(0,0,False), Area(width-40, height-40,True), width, height)