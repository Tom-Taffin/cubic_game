import pygame as pg
import random as rd

from assets.Coin import Coin
from assets.Player import Player

class Game:

    def __init__(self):
        self._length = 800
        self._width = 600
        self._background_color = pg.Color(0, 0, 0)

        pg.init()
        self.screen = pg.display.set_mode((self._length, self._width))
        self.clock = pg.time.Clock()
        self.running = True

        self.player = Player(10, 10)
        self.coins = []
        self.add_random_coins(3)
    
    def add_random_coins(self, n:int):
        for _ in range(n):
            self.coins.append(Coin(rd.randrange(self._length), rd.randrange(self._width)))
    
    def play(self):

        while self.running:
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

            self.screen.fill(self._background_color)

            for coin in self.coins:
                coin.draw(self.screen)
            
            self.player.update(self._length, self._width)
            self.player.draw(self.screen)

            pg.display.flip()

            self.clock.tick(60)

        pg.quit()


if __name__ == '__main__':
    game = Game()
    game.play()