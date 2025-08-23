from assets.Player import Player
from assets.ennemies.Ennemy_astar_blocker import Ennemy_astar_blocker
from assets.ennemies.Ennemy_astar import Ennemy_astar
from assets.ennemies.Ennemy_astar_patrol import Ennemy_astar_patrol
from assets.levels.Level_labyrinth import Level_labyrinth
from assets.Labyrinth import Labyrinth


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

        labyrinth = Labyrinth(map,player)
        enemy1 = Ennemy_astar(width//2, height//2,40,labyrinth)
        enemy2 = Ennemy_astar_blocker(width//2, height//2,40,labyrinth)
        enemies = [enemy1, enemy2]
        super().__init__(enemies, width, height, labyrinth)

