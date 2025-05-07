import pygame as pg

from assets.Element import Element

class Game:

    def __init__(self):
        self.elem = Element(self, 10, 10, 10, 10)
    
    def affiche(self):
        print(self.elem)


if __name__ == '__main__':
    game = Game()
    game.affiche()