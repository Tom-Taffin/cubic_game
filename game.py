import pygame as pg
import time
import random as rd

from assets.Player import Player
from assets.Level_random import Level_random
from assets.Level1 import Level1
from assets.Level0 import Level0
from assets.Level import Level

WIDTH = 800
HEIGHT = 600

class Game:

    def __init__(self, level:Level):
        self._width = WIDTH
        self._height = HEIGHT
        self.level = level
        self.player = Player(level.entry.get_x(),level.entry.get_y())
        
        # apprentissage supervisé
        self.score = 0
    
    # apprentissage supervisé


    def state(self):
        """return the state vector with the coordinates of the player, coins, enemies and exit"""
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
        res.append(self.level.exit.get_x())
        res.append(self.level.exit.get_y())
        return res
    
    def step(self, action:int, width:int, height:int):
        if self.score < -100:
            return -100, 1
        self.score -= 0.001
        reward = -0.001

        self.player.step(action, width, height)

        self.screen.fill(self._background_color)
        self.level.entry.draw(self.screen)
        self.level.exit.draw(self.screen)

        for coin in self.level.coins:
            if coin.is_active == 1 and coin.get_rect().colliderect(self.player.get_rect()):
                coin.is_active = 0
                self.score += 20
                reward += 20
            else:
                coin.draw(self.screen)
        
        for ennemy in self.level.ennemies:
            ennemy.move(self._width, self._height)
            if ennemy.get_rect().colliderect(self.player.get_rect()):
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
        
        if self.level.exit.get_rect().colliderect(self.player.get_rect()):
            if not has_coin_active :
                self.score += 100
                reward += 100
                return reward, 1
            else :
                self.score -= 0.01
                reward -= 0.01
        
        self.player.draw(self.screen)

        pg.display.flip()

        return reward, 0

    def play(self):
        for i in range(100):
            action = rd.randrange(5)
            print(action)
            done = self.step(action, self._width, self._height)
            print(self.state())
            print(self.score)
            print(done)

    def initScreen(self):
        pg.init()
        self.screen = pg.display.set_mode((self._width, self._height))
        self.clock = pg.time.Clock()
        self.running = True
        self._background_color = pg.Color(0, 0, 0)
    
    def initGame(self):
        self.level = Level0(WIDTH,HEIGHT)
        self.player = Player(self.level.entry.get_x(),self.level.entry.get_y())
        self.score = 0

    # jeu classique
    
    def playGUI(self):

        self._background_color = pg.Color(0, 0, 0)
        self.is_playing = False

        pg.init()
        self.screen = pg.display.set_mode((self._width, self._height))
        self.clock = pg.time.Clock()
        self.running = True

        while self.running:
            
            self.screen.fill(self._background_color)

            if game.is_playing:
                self.update_area()
                self.update_player()
                self.update_coins()
                self.update_ennemies_and_defeat()
                self.update_win()
            else:
                banner = pg.image.load("images/banner.jpg")
                banner = pg.transform.scale(banner,(self._width//2,self._height//6))
                banner_rect = banner.get_rect()
                banner_rect.x = self._width//4
                banner_rect.y = self._height//4
                self.screen.blit(banner, banner_rect)
                start_button = pg.image.load("images/start.jpg")
                start_button = pg.transform.scale(start_button,(banner_rect.width//3,banner_rect.height//2))
                start_button_rect = banner.get_rect()
                start_button_rect.x = banner_rect.x + banner_rect.width//3
                start_button_rect.y = banner_rect.bottom+10
                self.screen.blit(start_button, start_button_rect)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                
                elif not game.is_playing and event.type == pg.MOUSEBUTTONDOWN:
                    if start_button_rect.collidepoint(event.pos):
                        game.is_playing = True

            pg.display.flip()

            self.clock.tick(60)
        
        pg.quit()

    def update_coins(self):
        for coin in self.level.coins:
            if coin.is_active == 1:
                if coin.get_rect().colliderect(self.player.get_rect()):
                    coin.is_active = 0
                else:
                    coin.draw(self.screen)

    def update_ennemies_and_defeat(self):
        for ennemy in self.level.ennemies:
            if ennemy.get_rect().colliderect(self.player.get_rect()):
                image = pg.image.load("images/game_over.png")
                self.screen.blit(image, (300,200))
                pg.display.flip()
                time.sleep(2)
                self.restore_game()
                break

            else:
                ennemy.move(self._width, self._height)
                ennemy.draw(self.screen)

    def update_area(self):
        self.level.entry.draw(self.screen)
        self.level.exit.draw(self.screen)

    def update_player(self):
        self.player.update(self._width, self._height)
        self.player.draw(self.screen)
    
    def has_coin_active(self):
        for coin in self.level.coins:
            if coin.is_active == 1:
                return True
        return False
    
    def update_win(self):
        if not self.has_coin_active() and self.level.exit.get_rect().colliderect(self.player.get_rect()):
            image = pg.image.load("images/win.jpg")
            self.screen.blit(image, (300,200))
            self.is_playing = False
            pg.display.flip()
            time.sleep(2)
            self.restore_game()

    def restore_game(self):
        self.level.__init__(WIDTH,HEIGHT)
        self.player = Player(self.level.entry.get_x(),self.level.entry.get_y())

if __name__ == '__main__':
    game = Game(Level0(WIDTH,HEIGHT))
    game.playGUI()