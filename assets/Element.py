import pygame as pg

class Element:

    def __init__(self, x : int, y : int, length : int, width : int, color : pg.Color):
        self._x = x
        self._y = y
        self._length = length
        self._width = width
        self._color = color
    
    def get_x(self) -> int:
        return self._x
    
    def get_y(self) -> int:
        return self._y
    
    def get_length(self) -> int:
        return self._length
    
    def get_width(self) -> int:
        return self._width
    
    def get_color(self) -> pg.Color:
        return self._color