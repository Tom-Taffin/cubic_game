from assets.Coin import Coin
from assets.Ennemy_circular_movement import Ennemy_circular_movement
from assets.Area import Area
from assets.levels.Level import Level
from assets.Timer import Timer

class Level8(Level):

    def __init__(self, width:int, height:int):
    
        coins = [Coin(width//4,height//2), Coin(3*width//4,height//2), Coin(width//2,height//4), Coin(width//2,3*height//4)]
        ennemies = []
        for i in range(30,width, 150):
            ennemies.append(Ennemy_circular_movement(i,height//4,80,0.04))
            ennemies.append(Ennemy_circular_movement(i,height//2,80,0.04))
            ennemies.append(Ennemy_circular_movement(i,3*height//4,80,0.04))

        super().__init__(coins, ennemies, Area(0,0,False), Area(width-40, height-40,True), width, height, Timer(11))