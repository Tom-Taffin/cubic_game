import pygame as pg

from assets.Entity import Entity
from assets.Player import Player

import heapq


class Ennemy_astar(Entity):
    """
    Ennemy who hunts the player thanks to Astar
    """
    def __init__(self, x:int, y:int, speed:int, player:Player, map:list[int]):
        super().__init__(x,y,30,30,pg.Color(255,0,0),0,0)
        self.speed = speed/10
        self.player = player
        self.map = map
        self.tick = 60
        self.calculate_path()
    
    def move(self, board_width:int, board_height:int):
        if self.tick == 0:
            self.calculate_path()
            self.tick = 60
        self.tick-=1

        if self.path and len(self.path) > 1:
            next_cell = self.path[1]
            target_x = next_cell[0] * 40 + 20
            target_y = next_cell[1] * 30 + 15

            dx = target_x - self._rect.centerx
            dy = target_y - self._rect.centery

            if abs(dx) > self.speed:
                self._rect.x += self.speed if dx > 0 else -self.speed
            else:
                self._rect.centerx = target_x

            if abs(dy) > self.speed:
                self._rect.y += self.speed if dy > 0 else -self.speed
            else:
                self._rect.centery = target_y

            if self._rect.centerx == target_x and self._rect.centery == target_y:
                self.path.pop(0)

    def calculate_path(self):
        """Calculate the path"""
        start =  (self.get_x()//40, self.get_y()//30)
        goal = (self.player.get_x()//40, self.player.get_y()//30)
        self.path = self.astar_search(start, goal)

    def astar_search(self, start, goal, width=20, height=20):
        """
        A* pathfinding on a grid.
        start : (x, y)        -> start tile
        goal : (x, y)         -> gaol tile
        width, height : dimensions of the maze in number of tiles
        """
        # Heuristic = Manhattan distance
        def heuristic(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        # Return the neighbors
        def neighbors(node):
            x, y = node
            possible_moves = [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]
            results = []
            for nx, ny in possible_moves:
                if 0 <= nx < width and 0 <= ny < height:
                    if self.map[ny * width + nx] == 0:
                        results.append((nx, ny))
            return results

        open_set = []
        heapq.heappush(open_set, (0, start))
        came_from = {}
        g_score = {start: 0}
        f_score = {start: heuristic(start, goal)}

        while open_set:
            _, current = heapq.heappop(open_set)

            if current == goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                path.reverse()
                return path

            for neighbor in neighbors(current):
                tentative_g = g_score[current] + 1
                if tentative_g < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score[neighbor] = tentative_g + heuristic(neighbor, goal)
                    if neighbor not in [n for _, n in open_set]:
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))

        return None
