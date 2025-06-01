from assets.Area import Area
from assets.Coin import Coin
from assets.levels.Level import Level
from assets.ennemies.Ennemy_laser_pulsation import Ennemy_laser_pulsation
import pygame as pg

from assets.scenes.Ready import Ready

class Level1_stage3(Level):

    def __init__(self, width:int, height:int):
    
        coins = [Coin(width//4,height//2), Coin(3*width//4,height//2), Coin(width//2,height//4), Coin(width//2,3*height//4)]
        ennemies = []
        for i in range(100,width,100):
            ennemies.append(Ennemy_laser_pulsation(i,0,i,height,3,40,40))
            ennemies.append(Ennemy_laser_pulsation(0,i,width,i,3,40,40,40))

        super().__init__(coins, ennemies, Area(0,0,False), Area(width-40, height-40,True), width, height)
        self.intro_duration = 120
        self.init_intro_duration = 120
        self.intro_bg_image = pg.image.load("images/stage3_bg.jpg")
        self.intro_bg_image = pg.transform.scale(self.intro_bg_image,(width,height))
        self.intro_image = pg.image.load("images/stage3.png")
        self.intro_image = pg.transform.scale(self.intro_image,(width//2, height//8))

    def update(self, screen):
        # returns true if it is necessary to wait
        if self.intro_duration > 60:
            self.intro_duration -= 1
            screen.blit(self.intro_bg_image,(0,0))
            screen.blit(self.intro_image,(self._width//4,self._height//4))
            return True
        return super().update(screen)