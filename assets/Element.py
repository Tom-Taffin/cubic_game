import pygame as pg

class Element:

    def __init__(self, x : int, y : int, width : int, height : int, color : pg.Color):
        self._rect = pg.Rect(x,y,width,height)
        self._color = color
    
    def get_x(self) -> int:
        return self._rect.x
    
    def get_y(self) -> int:
        return self._rect.y
    
    def get_height(self) -> int:
        return self._rect.height
    
    def get_width(self) -> int:
        return self._rect.width
    
    def get_rect(self) -> int:
        return self._rect
    
    def get_color(self) -> pg.Color:
        return self._color
    
    def draw(self, screen : pg.display):
        pg.draw.rect(screen, self._color, self._rect)

    def is_collision(self,other):
        return self.get_rect().colliderect(other.get_rect())