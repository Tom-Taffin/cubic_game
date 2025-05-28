from assets.ennemies.Ennemy_snake_self_kill import Ennemy_snake_self_kill
from assets.levels.Level_Boss import Level_Boss
from assets.Player import Player

class Level9(Level_Boss):

    def __init__(self, width:int, height:int, player:Player):
    
        coins = []
        ennemies = [Ennemy_snake_self_kill(600,600,23,player,80)]

        super().__init__(coins, ennemies, width, height, player)

