from assets.Animation import Animation
from assets.Coin import Coin
from assets.Area import Area
from assets.Entity import Entity
from assets.Timer import Timer
from assets.levels.Level import Level
from assets.Player import Player

class Level_Boss(Level):

    def __init__(self, coins:list[Coin], ennemies:list[Entity], width:int, height:int, player:Player, timer:Timer = None):

        super().__init__(coins, ennemies, Area(0,0,False), Area(-100, -100,True), width, height, timer)
        self.player = player
        self.animation = Animation("boss",0,-300,800,1200)
        self.intro_duration = 156 # 24 images * 4 + 60
        self.init_intro_duration = 156

    def restore(self):
        """
        Restore the level to start a new game.
        All non-abstract levels that inherit from this class have an init of this form
        """
        self.__init__(self._width,self._height,self.player)

    def update(self, screen):
        """
        Makes the exit appear if the boss is dead.
        Returns true if it is necessary to wait and displays the intro.
        Otherwise, returns false if the intro is complete.
        All Boss levels have a basic boss intro and the ready intro but you can add intros before by increasing the intro duration.
        """
        if self.intro_duration > 60:
            self.intro_duration -= 1
            self.animation.update(screen)
            return True
        if self.intro_duration > 0:
            return super().update(screen)
        if self.ennemies[0].is_kill():
            self.exit._rect.x = self._width-40
            self.exit._rect.y = self._height-40
        return False
        