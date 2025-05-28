from assets.Area import Area
from assets.Coin import Coin
from assets.Player import Player
from assets.ennemies.Ennemy_rectilinear_movement import Ennemy_rectilinear_movement
from assets.levels.Level import Level
from assets.ennemies.Ennemy_laser_pulsation import Ennemy_laser_pulsation

class Level4_stage3(Level):

    def __init__(self, width:int, height:int):
    
        coins = [Coin(width//4,height//2), Coin(3*width//4,height//2), Coin(width//2,height//4), Coin(width//2,3*height//4)]
        ennemies = [Ennemy_laser_pulsation(0,0,width,height,3,60,60,60),
                    Ennemy_laser_pulsation(width,0,0,height,3,60,60,60),
                    Ennemy_laser_pulsation(width//2,0,width//2,height,3,60,60),
                    Ennemy_laser_pulsation(0,height//2,width,height//2,3,60,60)
                    ]
        
        for i in range(100,height-30, 100):
            if i%200==0:
                ennemies.append(Ennemy_rectilinear_movement(width,i,6,3))
            else:
                ennemies.append(Ennemy_rectilinear_movement(0,i,6,3))

        super().__init__(coins, ennemies, Area(0,0,False), Area(width-40, height-40,True), width, height)