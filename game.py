import pygame as pg
import time
import random as rd

from assets.Player import Player
from assets.Level_random import Level_random
from assets.Level1 import Level1
from assets.Level0 import Level0

LENGTH = 800
WITDH = 600

class Game:

    def __init__(self, level):
        self._length = LENGTH
        self._width = WITDH
        
        self.level = level
        self.player = Player(level.entry.get_x(),level.entry.get_y())
        self.score = 0
    
    def state(self):
        res = []
        res.append(self.player.get_x())
        res.append(self.player.get_y())
        for coin in self.level.coins:
            res.append(coin.get_x())
            res.append(coin.get_y())
            res.append(coin.is_active)
        for ennemy in self.level.ennemies:
            res.append(ennemy.get_x())
            res.append(ennemy.get_y())
        return res
    
    def step(self, action, length, width):
        self.score -= 0.001
        reward = -0.001

        self.player.step(action, length, width)

        self.screen.fill(self._background_color)
        self.level.entry.draw(self.screen)
        self.level.exit.draw(self.screen)

        for coin in self.level.coins:
            if coin.is_active == 1 and pg.Rect(coin.get_x(),coin.get_y(),coin.get_length(),coin.get_width()).colliderect(pg.Rect(self.player.get_x(),self.player.get_y(),self.player.get_length(),self.player.get_width())):
                coin.is_active = 0
                self.score += 10
                reward += 10
            else:
                coin.draw(self.screen)
        
        for ennemy in self.level.ennemies:
            ennemy.move(self._length, self._width)
            if pg.Rect(ennemy.get_x(),ennemy.get_y(),ennemy.get_length(),ennemy.get_width()).colliderect(pg.Rect(self.player.get_x(),self.player.get_y(),self.player.get_length(),self.player.get_width())):
                self.score -= 10
                reward -= 10
                return reward, 1
            else:
                ennemy.draw(self.screen)
        
        has_coin_active = False
        for coin in self.level.coins:
            if coin.is_active == 1:
                has_coin_active = True
                break
        
        if not has_coin_active and pg.Rect(self.level.exit.get_x(),self.level.exit.get_y(),self.level.exit.get_length(),self.level.exit.get_width()).colliderect(pg.Rect(self.player.get_x(),self.player.get_y(),self.player.get_length(),self.player.get_width())):
            self.score += 100
            reward += 100
            return reward, 1
        
        self.player.draw(self.screen)

        pg.display.flip()

        return reward, 0

    def play(self):
        for i in range(100):
            action = rd.randrange(5)
            print(action)
            done = self.step(action, self._length, self._width)
            print(self.state())
            print(self.score)
            print(done)

    def initScreen(self):
        pg.init()
        self.screen = pg.display.set_mode((self._length, self._width))
        self.clock = pg.time.Clock()
        self.running = True
        self._background_color = pg.Color(0, 0, 0)
    
    def initGame(self):
        self.level = Level0(LENGTH,WITDH)
        self.player = Player(self.level.entry.get_x(),self.level.entry.get_y())
        self.score = 0
    
    def playGUI(self):

        self._background_color = pg.Color(0, 0, 0)

        pg.init()
        self.screen = pg.display.set_mode((self._length, self._width))
        self.clock = pg.time.Clock()
        self.running = True

        while self.running:
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

            self.screen.fill(self._background_color)

            self.level.entry.draw(self.screen)
            self.level.exit.draw(self.screen)

            for coin in self.level.coins:
                if coin.is_active == 1:
                    if pg.Rect(coin.get_x(),coin.get_y(),coin.get_length(),coin.get_width()).colliderect(pg.Rect(self.player.get_x(),self.player.get_y(),self.player.get_length(),self.player.get_width())):
                        coin.is_active = 0
                    else:
                        coin.draw(self.screen)
            
            for ennemy in self.level.ennemies:
                if pg.Rect(ennemy.get_x(),ennemy.get_y(),ennemy.get_length(),ennemy.get_width()).colliderect(pg.Rect(self.player.get_x(),self.player.get_y(),self.player.get_length(),self.player.get_width())):
                    image = pg.image.load("images/game_over.png")
                    self.screen.blit(image, pg.Rect(300,200,400,400))
                    pg.display.flip()
                    time.sleep(2)
                    self.level = Level0(LENGTH,WITDH)
                    self.player = Player(self.level.entry.get_x(),self.level.entry.get_y())
                    pass

                else:
                    ennemy.move(self._length, self._width)
                    ennemy.draw(self.screen)
            
            has_coin_active = False
            for coin in self.level.coins:
                if coin.is_active == 1:
                    has_coin_active = True
                    break
            
            if not has_coin_active and pg.Rect(self.level.exit.get_x(),self.level.exit.get_y(),self.level.exit.get_length(),self.level.exit.get_width()).colliderect(pg.Rect(self.player.get_x(),self.player.get_y(),self.player.get_length(),self.player.get_width())):
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
    game = Game(Level0(LENGTH,WITDH))
    game.playGUI()