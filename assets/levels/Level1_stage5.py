import pygame as pg
from assets.Moving_labyrinth import Moving_labyrinth
from assets.Player import Player
from assets.ennemies.Ennemy_astar import Ennemy_astar
from assets.ennemies.Ennemy_astar_patrol import Ennemy_astar_patrol
from assets.levels.Level_labyrinth import Level_labyrinth


class Level1_stage5(Level_labyrinth):

    def __init__(self, width:int, height:int, player:Player):
        
        map = [
            1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
            1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,
            1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,0,
            1,0,1,0,0,0,0,0,0,1,0,0,2,0,0,0,1,0,0,0,
            1,0,1,0,1,1,1,1,0,1,0,1,1,1,1,0,1,1,0,1,
            1,0,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,0,1,
            1,0,1,3,1,1,0,1,1,1,1,1,0,1,1,1,1,3,1,1,
            1,0,1,0,1,1,0,3,0,0,1,1,0,0,0,1,1,0,0,1,
            1,0,1,0,1,1,1,1,1,0,1,1,1,1,0,1,1,1,0,1,
            1,0,2,0,1,0,0,0,1,0,0,0,0,0,0,0,0,2,0,1,
            1,1,1,0,1,0,1,0,1,0,0,0,1,0,1,1,0,1,0,1,
            1,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,1,0,1,
            1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1,0,1,
            1,0,0,0,1,0,0,0,0,1,0,0,0,0,2,0,0,3,0,1,
            1,1,1,3,1,1,1,1,0,1,0,1,1,1,1,0,1,1,1,1,
            1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,
            1,0,1,1,1,1,0,1,1,1,1,1,0,1,2,1,1,1,3,1,
            1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,
            1,1,1,1,0,1,2,1,1,1,1,1,0,1,0,1,0,0,1,1,
            1,1,1,1,0,0,0,1,1,1,1,1,0,0,0,1,1,0,0,0
        ]

        labyrinth = Moving_labyrinth(map,player)
        enemy1 = Ennemy_astar_patrol(width//2, height//2,30,labyrinth,(10,1),(12,19))
        enemy2 = Ennemy_astar_patrol(width//2, height//2,30,labyrinth,(1,1),(19,19))
        enemy3 = Ennemy_astar_patrol(width//2, height//2,30,labyrinth,(1,17),(19,1))
        enemies = [enemy1, enemy2, enemy3]
        super().__init__(enemies, width, height, labyrinth)

        # added stage 5 intro
        self.intro_duration = 120
        self.init_intro_duration = 120
        self.intro_bg_image = pg.image.load("images/stage4_bg.jpg")
        self.intro_bg_image = pg.transform.scale(self.intro_bg_image,(width,height))
        self.intro_image = pg.image.load("images/stage5.png")
        self.intro_image = pg.transform.scale(self.intro_image,(width//2, height//8))

    def update(self, screen):
        """
        Returns true if it is necessary to wait and displays the intro.
        Otherwise, returns false if the intro is complete.
        This level have a stage 4 intro and the ready intro
        """
        if self.intro_duration > 60:
            self.intro_duration -= 1
            screen.blit(self.intro_bg_image,(0,0))
            screen.blit(self.intro_image,(self._width//4,50))
            return True
        return super().update(screen)