from assets.Coin import Coin
from assets.Ennemy import Ennemy
from assets.Area import Area
from assets.Level import Level

class Level1(Level):

    def __init__(self, width:int, height:int):
    
        coins = [Coin(20, height-40), Coin(width-40, 20), Coin(width//2,height//2)]
        ennemies = []
        for i in range(60,width-30, 60):
            if i%120==0:
                ennemies.append(Ennemy(i,height,0,7))
            else:
                ennemies.append(Ennemy(i,0,0,7))
        
        for i in range(100,height-30, 100):
            if i%200==0:
                ennemies.append(Ennemy(width,i,4,0))
            else:
                ennemies.append(Ennemy(0,i,4,0))

        super().__init__(coins, ennemies, Area(0,0,False), Area(width-40, height-40,True), width, height)