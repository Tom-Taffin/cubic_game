import pygame as pg
from assets.Moving_labyrinth import Moving_labyrinth
from assets.Player import Player
from assets.ennemies.Ennemy_astar import Ennemy_astar
from assets.ennemies.Ennemy_astar_patrol import Ennemy_astar_patrol
from assets.levels.Level_labyrinth import Level_labyrinth


class Level3_stage5(Level_labyrinth):

    def __init__(self, width:int, height:int, player:Player):
        
        map = [
            1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
            1,0,0,0,0,0,1,0,0,2,0,0,1,0,0,2,0,0,0,0,
            1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,3,
            1,0,1,0,0,0,3,0,0,1,0,0,3,0,0,0,1,0,0,0,
            1,0,1,0,1,1,1,1,0,1,0,1,1,1,1,0,1,1,0,1,
            1,0,0,0,0,0,0,2,0,0,0,0,0,1,1,0,0,0,0,1,
            1,0,1,1,1,1,3,1,1,2,1,1,0,1,1,1,1,0,1,1,
            1,0,2,0,1,1,0,0,0,0,1,1,0,0,0,1,1,0,0,1,
            1,0,1,0,1,1,1,1,1,0,1,1,3,1,2,1,1,1,0,1,
            1,0,3,0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,1,
            1,1,1,0,1,0,1,0,1,0,0,0,1,3,1,1,0,1,0,1,
            1,0,0,0,0,0,1,0,0,0,1,0,2,0,0,0,0,1,0,1,
            1,0,1,3,1,0,1,1,1,1,1,0,1,1,1,1,0,1,0,1,
            1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,2,0,1,
            1,1,1,2,1,3,1,1,0,1,0,1,1,1,1,0,1,1,2,1,
            1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,
            1,0,1,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,3,1,
            1,0,0,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,1,
            1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,0,0,1,1,
            1,1,1,1,0,2,0,1,1,1,1,1,0,3,0,1,1,0,0,0
        ]

        labyrinth = Moving_labyrinth(map,player)
        enemy1 = Ennemy_astar(width//2, height//2,40,labyrinth)
        enemy2 = Ennemy_astar_patrol(width//2, height//2,30,labyrinth,(1,1),(19,19))
        enemy3 = Ennemy_astar_patrol(width//2, height//2,30,labyrinth,(1,17),(19,1))
        enemies = [enemy1, enemy2, enemy3]
        super().__init__(enemies, width, height, labyrinth)
    
