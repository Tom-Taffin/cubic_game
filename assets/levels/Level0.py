from assets.Coin import Coin
from assets.Ennemy_rectilinear_movement import Ennemy_rectilinear_movement
from assets.Area import Area
from assets.levels.Level import Level

class Level0(Level):

    def __init__(self, width:int, height:int):
    
        coins = [Coin(20, height-40), Coin(width-40, 20), Coin(width//2,height//2)]
        ennemies = []
        for i in range(60,width-30, 120):
            if i%240==0:
                ennemies.append(Ennemy_rectilinear_movement(i,height,0,3))
            else:
                ennemies.append(Ennemy_rectilinear_movement(i,0,0,3))

        super().__init__(coins, ennemies, Area(0,0,False), Area(width-40, height-40,True), width, height)