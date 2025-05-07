from assets import Element
import pygame as pg
import game


class Area(Element):
    def __init__(self, x:int, y:int, is_exit:bool):
        self.super(x,y,20,20, pg.Color(0,255,0) if is_exit else pg.Color(0,0,255))
        self._is_exit = is_exit
