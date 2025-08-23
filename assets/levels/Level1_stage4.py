import pygame as pg
from assets.Labyrinth import Labyrinth
from assets.Player import Player
from assets.ennemies.Ennemy_astar import Ennemy_astar
from assets.levels.Level_labyrinth import Level_labyrinth


class Level1_stage4(Level_labyrinth):

    def __init__(self, width:int, height:int, player:Player):
        map = [
            1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
            1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
            1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,0,1,
            1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,
            1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,
            1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,
            1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,
            1,0,0,0,0,1,0,0,0,0,0,0,0,1,1,1,1,1,0,1,
            1,1,1,1,0,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,
            1,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,1,
            1,0,1,1,1,1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,
            1,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,1,
            1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,0,1,
            1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,
            1,0,1,0,1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,
            1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,
            1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,
            1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,
            1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
            1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0
        ]
        
        labyrinth = Labyrinth(map,player)
        enemies = [Ennemy_astar(width//2, height//2,40,labyrinth)]
        super().__init__(enemies, width, height, labyrinth)

        # added stage 4 intro
        self.intro_duration = 120
        self.init_intro_duration = 120
        self.intro_bg_image = pg.image.load("images/stage4_bg.jpg")
        self.intro_bg_image = pg.transform.scale(self.intro_bg_image,(width,height))
        self.intro_image = pg.image.load("images/stage4.png")
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