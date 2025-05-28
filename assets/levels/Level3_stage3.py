from assets.ennemies.Ennemy_snake_weak_point import Ennemy_snake_weak_point
from assets.levels.Level_Boss import Level_Boss
from assets.Player import Player

class Level3_stage3(Level_Boss):

    def __init__(self, width:int, height:int, player:Player):
    
        coins = []
        ennemies = [Ennemy_snake_weak_point(600,600,28,player,50)]

        super().__init__(coins, ennemies, width, height, player)