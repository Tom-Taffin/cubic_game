from assets.Coin import Coin
from assets.ennemies.Ennemy_circular_movement import Ennemy_circular_movement
from assets.ennemies.Ennemy_static import Ennemy_static
from assets.Area import Area
from assets.levels.Level import Level
import pygame as pg

class Level6(Level):

    def __init__(self, width:int, height:int):
    
        coins = [Coin(width//4,height//2), Coin(3*width//4,height//2), Coin(width//2,height//4), Coin(width//2,3*height//4)]
        ennemies = []
        for i in range(0,width//2+30, 30):
            ennemies.append(Ennemy_circular_movement(width//2-15,height//2-15,i,0.055))
        ennemies.append(Ennemy_static(width//2-80,height//2-80,160,160))

        super().__init__(coins, ennemies, Area(0,0,False), Area(width-40, height-40,True), width, height)