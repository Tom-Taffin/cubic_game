import pygame as pg

from assets.Labyrinth import Labyrinth
from assets.Player import Player

class Moving_labyrinth(Labyrinth):
    """
    The screen is divided into 400 tiles (20x20).
    A tile is 40 px wide and 30 px long.
    """

    def __init__(self, map : list[int], player : Player):
        """
        The labyrinth is represented by a map which is a list 
        that indicates for each tile whether there is an obstacle 1 or not 0.
        The tiles with a 2 or a 3 are the walls that appear and then disappear.
        The 2 start by being a wall and the 3 start by being free.
        """
        super().__init__(map,player)
        self.first_plan = False
        self.init_tick = 300
        self.tick = self.init_tick
        self.walls_plan2 = self.walls + self._get_moving_walls()
        self.first_plan = True
        self.walls_plan1 = self.walls + self._get_moving_walls()
        self.walls = self.walls_plan1


    def _get_moving_walls(self) -> list[pg.Rect]:
        """Return the list of rectangles associated with the moving walls"""
        walls = []
        for i in range(len(self.map)):
            if self.map[i] == 2 and self.first_plan or self.map[i] == 3 and not self.first_plan:
                walls.append(pg.Rect(i % 20 * 40, i // 20 * 30, 40, 30))
        return walls
    
    def draw(self, screen : pg.display):
        """Display the labyrinth and prevent the player from going through walls."""
        self.tick -= 1
        if self.tick == 0:
            self.tick = self.init_tick
            if self.first_plan:
                self.first_plan = False
                self.walls = self.walls_plan2
            else:
                self.first_plan = True
                self.walls = self.walls_plan1
        super().draw(screen)
    
        