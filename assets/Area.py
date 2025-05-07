from assets.Element import Element
import pygame as pg


class Area(Element):
    def __init__(self, x:int, y:int, is_exit:bool):
        super().__init__(x,y,40,40, pg.Color(0,255,0) if is_exit else pg.Color(0,0,255))
        self._is_exit = is_exit
