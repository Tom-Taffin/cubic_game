import random as rd

from assets.Coin import Coin
from assets.Ennemy import Ennemy
from assets.Area import Area
from assets.Level import Level

class Level_random(Level):

    def __init__(self, width:int, height:int):
    
        coins = []
        for _ in range(3):
            coins.append(Coin(rd.randrange(max(0,width-20)), rd.randrange(max(0,height-20))))

        ennemies = []
        for _ in range(55):
            ennemies.append(Ennemy(rd.randrange(max(100, width-40)), rd.randrange(max(100, height-40)), rd.random()*3, rd.random()*3))

        super().__init__(coins, ennemies, Area(0,0,False), Area(width-40, height-40,True), width, height)