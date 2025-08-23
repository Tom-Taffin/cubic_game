from assets.Area import Area
from assets.Coin import Coin
from assets.Entity import Entity
from assets.Labyrinth import Labyrinth
from assets.Moving_labyrinth import Moving_labyrinth
from assets.Player import Player
from assets.Timer import Timer
from assets.levels.Level import Level


class Level_labyrinth(Level):

    def __init__(self, ennemies:list[Entity], width:int, height:int, labyrinth: Labyrinth, timer:Timer = None):
        coins = []
        for i in range(len(labyrinth.map)):
            if labyrinth.map[i] == 0:
                coins.append(Coin(i%20*40+10,i//20*30+5))
        super().__init__(coins, ennemies, Area(40,30,False), Area(width-40, height-40,True), width, height)
        self.player = labyrinth.player
        self.labyrinth = labyrinth

    def draw(self, screen):
        """
        Display the labyrinth
        """
        self.labyrinth.draw(screen)
    
    def restore(self):
        """
        Restore the level to start a new game.
        All non-abstract levels that inherit from this class have an init of this form
        """
        self.__init__(self._width,self._height,self.player)