from assets.Animation import Animation
from assets.Coin import Coin
from assets.ennemies.Ennemy_circular_movement import Ennemy_circular_movement
from assets.Area import Area
from assets.levels.Level import Level
import pygame as pg

from assets.scenes.Ready import Ready

class Level1_stage2(Level):

    def __init__(self, width:int, height:int):
    
        coins = [Coin(width//4,height//2), Coin(3*width//4,height//2), Coin(width//2,height//4), Coin(width//2,3*height//4)]
        ennemies = []
        for i in range(0,width//2+100, 30):
            ennemies.append(Ennemy_circular_movement(width//2-15,height//2-15,i,0.045))

        super().__init__(coins, ennemies, Area(0,0,False), Area(width-40, height-40,True), width, height)

        self.intro_bg_animation = Animation("circle",0,0,width,height)
        self.intro_image = pg.image.load("images/stage2.png")
        self.intro_image = pg.transform.scale(self.intro_image,(width//2, height//8))
        self.intro_duration = 124
        self.init_intro_duration = 124

    def update(self, screen):
        # returns true if it is necessary to wait
        if self.intro_duration > 60:
            self.intro_duration -= 1
            self.intro_bg_animation.update(screen)
            screen.blit(self.intro_image,(self._width//4,self._height//2.5))
            return True
        return super().update(screen)