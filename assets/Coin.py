from assets import Element
import pygame as pg
import game


class Coin(Element):
    def __init__(self, x:int, y:int):
        self.super(x,y,10,10,pg.Color(255,255,0))