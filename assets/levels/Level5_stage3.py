from assets.ennemies.Ennemy_snake_weak_point import Ennemy_snake_weak_point
from assets.levels.Level_Boss import Level_Boss
from assets.ennemies.Ennemy_laser_pulsation import Ennemy_laser_pulsation
from assets.Player import Player

class Level5_stage3(Level_Boss):

    def __init__(self, width:int, height:int, player:Player):
    
        coins = []
        ennemies = [Ennemy_snake_weak_point(600,600,20,player,50)]
        for i in range(150,width,150):
            ennemies.append(Ennemy_laser_pulsation(i,0,i,height,3,30,120))

        super().__init__(coins, ennemies, width, height, player)