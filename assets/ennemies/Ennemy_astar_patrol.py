from assets.ennemies.Ennemy_astar import Ennemy_astar
from assets.Player import Player
import pygame as pg

class Ennemy_astar_patrol(Ennemy_astar):
    """
    Enemy that patrols between two tiles and chases the player if he is close
    """
    def __init__(self, x:int, y:int, speed:int, player:Player, map:list[int], point_a:tuple[int], point_b:tuple[int]):
        self.goal_is_point_b = False
        self.point_a = point_a
        self.point_b = point_b
        super().__init__(x,y,speed,player,map)
        self._color = pg.Color(245, 39, 121)

    def calculate_path(self):
        """Calculate the path"""
        start =  (self.get_x()//40, self.get_y()//30)
        if start == self.point_a:
            self.goal_is_point_b = True
        if start == self.point_b:
            self.goal_is_point_b = False
        goal = self.point_b if self.goal_is_point_b else self.point_a
        player_tile = (self.player.get_x()//40,self.player.get_y()//30)
        if abs(player_tile[0]-start[0]) + abs(player_tile[1]-start[1]) <= 6:
            goal = player_tile
        self.path = super().astar_search(start, goal)
