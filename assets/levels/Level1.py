from assets.Coin import Coin
from assets.Ennemy_rectilinear_movement import Ennemy_rectilinear_movement
from assets.Area import Area
from assets.levels.Level import Level

class Level1(Level):

    def __init__(self, width:int, height:int):
    
        coins = [Coin(width//4,height//2), Coin(3*width//4,height//2), Coin(width//2,height//2)]
        ennemies = []
        for i in range(60,width-30, 60):
            if i%120==0:
                ennemies.append(Ennemy_rectilinear_movement(i,height,0,7))
            else:
                ennemies.append(Ennemy_rectilinear_movement(i,0,0,7))

        super().__init__(coins, ennemies, Area(0,0,False), Area(width-40, height-40,True), width, height)