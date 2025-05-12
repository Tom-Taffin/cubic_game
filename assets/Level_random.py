import random as rd

from assets.Coin import Coin
from assets.Ennemy import Ennemy
from assets.Area import Area
from assets.Level import Level

class Level_random(Level):

    def __init__(self, length, width):
    
        coins = []
        for _ in range(3):
            coins.append(Coin(rd.randrange(max(0,length-20)), rd.randrange(max(0,width-20))))

        ennemies = []
        for _ in range(25):
            ennemies.append(Ennemy(rd.randrange(max(100, length-40)), rd.randrange(max(100, width-40)), rd.random()*3, rd.random()*3))

        super().__init__(coins, ennemies, Area(0,0,False), Area(length-40, width-40,True), length, width)