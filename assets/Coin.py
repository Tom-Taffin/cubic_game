from assets.Element import Element
import pygame as pg

class Coin(Element):
    def __init__(self, x:int, y:int):
        super().__init__(x, y, 10, 10, pg.Color(255,255,0))