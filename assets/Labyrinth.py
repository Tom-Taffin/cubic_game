import pygame as pg

from assets.Player import Player

class Labyrinth:
    """
    The screen is divided into 400 tiles (20x20).
    A tile is 40 px wide and 30 px long.
    """

    def __init__(self, map : list[int], player : Player):
        """
        The labyrinth is represented by a map which is a list 
        that indicates for each tile whether there is an obstacle 1 or not 0.
        """
        self.map = map
        self.player = player
        self.walls = self._get_walls()

    def _get_walls(self) -> list[pg.Rect]:
        walls = []
        for i in range(len(self.map)):
            if self.map[i] == 1:
                walls.append(pg.Rect(i % 20 * 40, i // 20 * 30, 40, 30))
        return walls    
    
    def draw(self, screen : pg.display):
        for wall in self.walls:
            pg.draw.rect(screen,pg.Color(160,160,160),wall)

        self.player._rect.y -= self.player._deltaY
        for wall in self.walls:
            if self.player._rect.colliderect(wall):
                if self.player._deltaX > 0:
                    self.player._rect.right = wall.left
                else:
                    self.player._rect.left = wall.right
        
        self.player._rect.y += self.player._deltaY
        for wall in self.walls:
            if self.player._rect.colliderect(wall):
                if self.player._deltaY > 0:
                    self.player._rect.bottom = wall.top
                else:
                    self.player._rect.top = wall.bottom
    
        