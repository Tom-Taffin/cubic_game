from assets.Coin import Coin
from assets.ennemies.Ennemy_rectilinear_movement import Ennemy_rectilinear_movement
from assets.ennemies.Ennemy_static import Ennemy_static
from assets.Area import Area
from assets.levels.Level import Level

class Level2(Level):

    def __init__(self, width:int, height:int):
    
        coins = [Coin(width//4,height//2), Coin(3*width//4,height//2), Coin(width//2,height//2)]
        ennemies = []
        for i in range(60,width-30, 60):
            if i%120==0:
                ennemies.append(Ennemy_rectilinear_movement(i,height,0,7))
            else:
                ennemies.append(Ennemy_rectilinear_movement(i,0,0,7))
        ennemies.append(Ennemy_static(0,150,width,5))
        ennemies.append(Ennemy_static(0,height-150,width,5))

        super().__init__(coins, ennemies, Area(0,280,False), Area(width-40, 280,True), width, height)