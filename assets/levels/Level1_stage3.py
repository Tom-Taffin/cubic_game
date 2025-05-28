from assets.Area import Area
from assets.Coin import Coin
from assets.levels.Level import Level
from assets.ennemies.Ennemy_laser_pulsation import Ennemy_laser_pulsation

class Level1_stage3(Level):

    def __init__(self, width:int, height:int):
    
        coins = [Coin(width//4,height//2), Coin(3*width//4,height//2), Coin(width//2,height//4), Coin(width//2,3*height//4)]
        ennemies = []
        for i in range(100,width,100):
            ennemies.append(Ennemy_laser_pulsation(i,0,i,height,3,40,40))
            ennemies.append(Ennemy_laser_pulsation(0,i,width,i,3,40,40,40))

        super().__init__(coins, ennemies, Area(0,0,False), Area(width-40, height-40,True), width, height)