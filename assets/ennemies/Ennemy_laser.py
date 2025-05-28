import math
import pygame as pg

class Ennemy_laser:
    def __init__(self, x1:int, y1:int, x2:int, y2:int, width:int = 3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.width = width
        
    def draw(self, screen):
        pg.draw.line(screen, pg.Color(255,0,0), 
                    (self.x1, self.y1), 
                    (self.x2, self.y2), self.width)

    def is_collision(self,other):
        player_center_x = other.get_x() + other.get_width() // 2
        player_center_y = other.get_y() + other.get_height() // 2
        
        distance = self._point_to_line_distance(
            player_center_x, player_center_y,
            self.x1, self.y1,
            self.x2, self.y2
        )
        
        return distance <= (self.width // 2 + min(other.get_width(), other.get_height()) // 2)
    
    def _point_to_line_distance(self, px, py, x1, y1, x2, y2):
        """Calcule la distance d'un point à une ligne"""
        A = px - x1
        B = py - y1
        C = x2 - x1
        D = y2 - y1
        
        dot = A * C + B * D
        len_sq = C * C + D * D
        
        if len_sq == 0:
            return math.sqrt(A * A + B * B)
        
        param = dot / len_sq
        
        if param < 0:
            xx, yy = x1, y1
        elif param > 1:
            xx, yy = x2, y2
        else:
            xx = x1 + param * C
            yy = y1 + param * D
        
        dx = px - xx
        dy = py - yy
        return math.sqrt(dx * dx + dy * dy)
    
    def move(self, board_width:int, board_height:int):
        pass