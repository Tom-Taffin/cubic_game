import pygame as pg

from assets.Coin import Coin

class Game:

    def __init__(self):
        self._length = 800
        self._width = 600
        self._background_color = pg.Color(0, 0, 0)

        pg.init()
        self.screen = pg.display.set_mode((self._length, self._width))
        self.clock = pg.time.Clock()
        self.running = True

        self.coin = Coin(10, 10)
    
    def play(self):

        while self.running:
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

            self.screen.fill(self._background_color)

            self.coin.draw(self.screen)

            pg.display.flip()

            self.clock.tick(60)

        pg.quit()


if __name__ == '__main__':
    game = Game()
    game.play()