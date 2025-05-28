from assets.Coin import Coin
from assets.ennemies.Ennemy_rectilinear_movement import Ennemy_rectilinear_movement
from assets.Area import Area
from assets.levels.Level import Level
from assets.Timer import Timer

class Level4(Level):

    def __init__(self, width:int, height:int):
    
        coins = [Coin(width//4,height//2), Coin(3*width//4,height//2), Coin(width//2,height//2)]
        ennemies = []
        for i in range(60,width-30, 60):
            if i%120==0:
                ennemies.append(Ennemy_rectilinear_movement(i,height,0,5))
            else:
                ennemies.append(Ennemy_rectilinear_movement(i,0,0,6))
        
        for i in range(200,height-30, 200):
            if i%400==0:
                ennemies.append(Ennemy_rectilinear_movement(width,i,4,2))
            else:
                ennemies.append(Ennemy_rectilinear_movement(0,i,4,2))

        super().__init__(coins, ennemies, Area(0,0,False), Area(width-40, height-40,True), width, height, Timer(5))