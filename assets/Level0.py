from assets.Coin import Coin
from assets.Ennemy import Ennemy
from assets.Area import Area
from assets.Level import Level

class Level0(Level):

    def __init__(self, length, width):
    
        coins = [Coin(20, width-40), Coin(length-40, 20), Coin(length//2,width//2)]
        ennemies = []
        for i in range(60,length-30, 120):
            if i%240==0:
                ennemies.append(Ennemy(i,width,0,7))
            else:
                ennemies.append(Ennemy(i,0,0,7))

        super().__init__(coins, ennemies, Area(0,0,False), Area(length-40, width-40,True), length, width)