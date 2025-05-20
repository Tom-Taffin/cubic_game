from assets.Coin import Coin
from assets.Ennemy_circular_movement import Ennemy_circular_movement
from assets.Ennemy_static import Ennemy_static
from assets.Area import Area
from assets.levels.Level import Level
from assets.Timer import Timer

class Level7(Level):

    def __init__(self, width:int, height:int):
    
        coins = [Coin(width//4,height//2+10), Coin(3*width//4,height//2+10), Coin(width//2,height//4-10), Coin(width//2,3*height//4)]
        ennemies = []
        for i in range(0,width+100, 130):
            ennemies.append(Ennemy_circular_movement(width//2-15,height//2-15,i,0.015))
            ennemies.append(Ennemy_circular_movement(width//2-15,height//2-15,i,0.015,3.14/2))
            ennemies.append(Ennemy_circular_movement(width//2-15,height//2-15,i,0.015,3.14))
            ennemies.append(Ennemy_circular_movement(width//2-15,height//2-15,i,0.015,3*3.14/2))
        for i in range(100,height,100):
            if i%200==0:
                ennemies.append(Ennemy_static(40,i,width,5))
            else:
                ennemies.append(Ennemy_static(0,i,width-40,5))

        super().__init__(coins, ennemies, Area(0,0,False), Area(width-40, height-40,True), width, height, Timer(20))