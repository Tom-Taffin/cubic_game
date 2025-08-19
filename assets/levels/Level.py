from assets.Coin import Coin
from assets.Entity import Entity
from assets.Area import Area
from assets.Timer import Timer
from assets.scenes.Ready import Ready
import pygame as pg

class Level:

    def __init__(self, coins:list[Coin], ennemies:list[Entity], entry:Area, exit:Area, width:int, height:int, timer:Timer = None):
        self.coins = coins
        self.ennemies = ennemies
        self.entry = entry
        self.exit = exit
        self._width = width
        self._height = height
        self.timer = timer
        self.intro_duration = 60
        self.init_intro_duration = self.intro_duration

    def restore(self):
        """
        Restore the level to start a new game.
        All non-abstract levels that inherit from this class have an init of this form
        """
        self.__init__(self._width,self._height)

    def update(self, screen):
        """
        Returns true if it is necessary to wait and displays the intro.
        Otherwise, returns false if the intro is complete.
        All levels have a basic intro Ready but you can add intros before this one by increasing the intro duration.
        """
        wait = False
        if self.intro_duration == 60:
            screen.fill(pg.Color(0,0,0))
            Ready(screen)
        if self.intro_duration > 0:
            self.intro_duration -= 1
            wait = True
        return wait
    
    def restore_intro_duration(self):
        """Restore all intros."""
        self.intro_duration = self.init_intro_duration

    def restore_ready_intro(self):
        """restore only the "Ready" intro"""
        self.intro_duration = 60

    def draw(self, screen):
        """Draw the necessary elements at the level """
        pass