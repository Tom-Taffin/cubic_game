from assets.Player import Player
from assets.ennemies.Ennemy_astar_blocker import Ennemy_astar_blocker
from assets.ennemies.Ennemy_astar import Ennemy_astar
from assets.ennemies.Ennemy_astar_patrol import Ennemy_astar_patrol
from assets.levels.Level_labyrinth import Level_labyrinth


class Level5_stage4(Level_labyrinth):

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

        enemy1 = Ennemy_astar(width//2, height//2,30,player,map)
        enemy2 = Ennemy_astar_patrol(width//2, height//2,25,player,map,(1,1),(19,19))
        enemy3 = Ennemy_astar_patrol(width//2, height//2,25,player,map,(1,17),(19,1))
        enemy4 = Ennemy_astar_blocker(width//2, height//2,30,player,map)
        enemies = [enemy1, enemy2, enemy3, enemy4]
        super().__init__(enemies, width, height, player, map)

