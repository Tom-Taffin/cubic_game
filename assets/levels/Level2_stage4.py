from assets.Player import Player
from assets.ennemies.Ennemy_astar_blocker import Ennemy_astar_blocker
from assets.ennemies.Ennemy_astar import Ennemy_astar
from assets.ennemies.Ennemy_astar_patrol import Ennemy_astar_patrol
from assets.levels.Level_labyrinth import Level_labyrinth


class Level2_stage4(Level_labyrinth):

    def __init__(self, width:int, height:int, player:Player):

        map = [
            1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
            1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,
            1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,0,
            1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,
            1,0,1,0,1,1,1,1,0,1,0,1,1,1,1,0,1,1,0,1,
            1,0,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,0,1,
            1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1,1,
            1,0,1,0,1,1,0,0,0,0,1,1,0,0,0,1,1,0,0,1,
            1,0,1,0,1,1,1,1,1,0,1,1,1,1,0,1,1,1,0,1,
            1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,1,
            1,1,1,0,1,0,1,0,1,0,0,0,1,0,1,1,0,1,0,1,
            1,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,1,0,1,
            1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1,0,1,
            1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,
            1,1,1,0,1,1,1,1,0,1,0,1,1,1,1,0,1,1,1,1,
            1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,
            1,0,1,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,0,1,
            1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,
            1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,0,0,1,1,
            1,1,1,1,0,0,0,1,1,1,1,1,0,0,0,1,1,0,0,0
        ]

        ennemie1 = Ennemy_astar(width//2, height//2,40,player,map)
        ennemie2 = Ennemy_astar_patrol(width//2, height//2,30,player,map,(1,1),(19,19))
        ennemie3 = Ennemy_astar_patrol(width//2, height//2,30,player,map,(1,17),(19,1))
        ennemies = [ennemie1, ennemie2, Ennemy_astar_blocker(width//2, height//2,40,player,map)]
        super().__init__(ennemies, width, height, player, map)

