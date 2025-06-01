from assets.Coin import Coin
from assets.ennemies.Ennemy_rectilinear_movement import Ennemy_rectilinear_movement
from assets.Area import Area
from assets.levels.Level import Level
import pygame as pg

from assets.scenes.Ready import Ready

class Level1_stage1(Level):

    def __init__(self, width:int, height:int):
    
        coins = [Coin(20, height-40), Coin(width-40, 20), Coin(width//2,height//2)]
        ennemies = []
        for i in range(60,width-30, 120):
            ennemies.append(Ennemy_rectilinear_movement(i,0,0,3))

        super().__init__(coins, ennemies, Area(0,0,False), Area(width-40, height-40,True), width, height)

        self.intro_duration = 120
        self.init_intro_duration = 120
        self.intro_bg_image = pg.image.load("images/stage1_bg.jpg")
        self.intro_bg_image = pg.transform.scale(self.intro_bg_image,(width,height))
        self.intro_image = pg.image.load("images/stage1.png")
        self.intro_image = pg.transform.scale(self.intro_image,(width//2, height//8))


    def update(self, screen):
        # returns true if it is necessary to wait
        if self.intro_duration > 60:
            self.intro_duration -= 1
            screen.blit(self.intro_bg_image,(0,0))
            screen.blit(self.intro_image,(self._width//4,self._height//2.5))
            return True
        return super().update(screen)