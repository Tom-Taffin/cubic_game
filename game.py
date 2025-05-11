import pygame as pg
import random as rd
import time

from assets.Player import Player
from assets.Coin import Coin
from assets.Ennemy import Ennemy
from assets.Area import Area

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

        self.ennemies = []
        self.add_random_ennemies(25)

        self.entry = Area(0,0,False)
        self.exit = Area(self._length-40,self._width-40,True)
    
    def add_random_coins(self, n:int):
        for _ in range(n):
            self.coins.append(Coin(rd.randrange(max(0,self._length-20)), rd.randrange(max(0,self._width-20))))
    
    def add_random_ennemies(self, n:int):
        for _ in range(n):
            self.ennemies.append(Ennemy(rd.randrange(max(60,self._length-40)), rd.randrange(max(60,self._width-40)), rd.random()*3, rd.random()*3))
    
    def play(self):

        while self.running:
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

            self.screen.fill(self._background_color)

            self.entry.draw(self.screen)
            self.exit.draw(self.screen)

            for coin in self.coins:
                if pg.Rect(coin.get_x(),coin.get_y(),coin.get_length(),coin.get_width()).colliderect(pg.Rect(self.player.get_x(),self.player.get_y(),self.player.get_length(),self.player.get_width())):
                    self.coins.remove(coin)
                else:
                    coin.draw(self.screen)
            
            for ennemy in self.ennemies:
                if pg.Rect(ennemy.get_x(),ennemy.get_y(),ennemy.get_length(),ennemy.get_width()).colliderect(pg.Rect(self.player.get_x(),self.player.get_y(),self.player.get_length(),self.player.get_width())):
                    image = pg.image.load("images/game_over.png")
                    self.screen.blit(image, pg.Rect(300,200,400,400))
                    self.running = False
                    pg.display.flip()
                    time.sleep(2)
                    break

                else:
                    ennemy.move(self._length, self._width)
                    ennemy.draw(self.screen)
            if len(self.coins) == 0 and pg.Rect(self.exit.get_x(),self.exit.get_y(),self.exit.get_length(),self.exit.get_width()).colliderect(pg.Rect(self.player.get_x(),self.player.get_y(),self.player.get_length(),self.player.get_width())):
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
    game = Game()
    game.play()