import pygame as pg
import time

from assets.Player import Player
from assets.Level_random import Level_random

LENGTH = 800
WITDH = 600

class Game:

    def __init__(self, level):
        self._length = LENGTH
        self._width = WITDH
        self._background_color = pg.Color(0, 0, 0)

        pg.init()
        self.screen = pg.display.set_mode((self._length, self._width))
        self.clock = pg.time.Clock()
        self.running = True
        self.level = level
        self.player = Player(level.entry.get_x(),level.entry.get_y())
    
    def play(self):

        while self.running:
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

            self.screen.fill(self._background_color)

            self.level.entry.draw(self.screen)
            self.level.exit.draw(self.screen)

            for coin in self.level.coins:
                if pg.Rect(coin.get_x(),coin.get_y(),coin.get_length(),coin.get_width()).colliderect(pg.Rect(self.player.get_x(),self.player.get_y(),self.player.get_length(),self.player.get_width())):
                    self.level.coins.remove(coin)
                else:
                    coin.draw(self.screen)
            
            for ennemy in self.level.ennemies:
                if pg.Rect(ennemy.get_x(),ennemy.get_y(),ennemy.get_length(),ennemy.get_width()).colliderect(pg.Rect(self.player.get_x(),self.player.get_y(),self.player.get_length(),self.player.get_width())):
                    image = pg.image.load("images/game_over.png")
                    self.screen.blit(image, pg.Rect(300,200,400,400))
                    pg.display.flip()
                    time.sleep(2)
                    self.level = Level_random(LENGTH,WITDH)
                    self.player = Player(self.level.entry.get_x(),self.level.entry.get_y())
                    pass

                else:
                    ennemy.move(self._length, self._width)
                    ennemy.draw(self.screen)
            if len(self.level.coins) == 0 and pg.Rect(self.level.exit.get_x(),self.level.exit.get_y(),self.level.exit.get_length(),self.level.exit.get_width()).colliderect(pg.Rect(self.player.get_x(),self.player.get_y(),self.player.get_length(),self.player.get_width())):
                image = pg.image.load("images/win.jpg")
                self.screen.blit(image, pg.Rect(300,200,400,400))
                self.running = False
                pg.display.flip()
                time.sleep(2)
                break

            self.player.update(self._length, self._width)
            self.player.draw(self.screen)

            pg.display.flip()

            self.clock.tick(60)
        
        pg.quit()


if __name__ == '__main__':
    game = Game(Level_random(LENGTH,WITDH))
    game.play()