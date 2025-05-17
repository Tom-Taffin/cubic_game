import pygame as pg
from time import time
import random as rd

from assets.Sound_manager import Sound_manager
from assets.Player import Player
from assets.Level4 import Level4
from assets.Level3 import Level3
from assets.Level_random import Level_random
from assets.Level1 import Level1
from assets.Level0 import Level0
from assets.Level import Level
from assets.Level2 import Level2

from assets.scenes.Menu import Menu
from assets.scenes.Game_over import Game_over
from assets.scenes.Win import Win
from assets.scenes.Final_win import Final_win
from assets.scenes.Levels import Levels
from assets.scenes.Ready import Ready

WIDTH = 800
HEIGHT = 600
LEVELS = [Level0(WIDTH,HEIGHT), Level2(WIDTH,HEIGHT), Level1(WIDTH,HEIGHT),Level_random(WIDTH,HEIGHT),Level3(WIDTH,HEIGHT),Level4(WIDTH,HEIGHT)]

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
        self.levels = LEVELS
        self.sound_manager = Sound_manager()

        pg.init()
        self.screen = pg.display.set_mode((self._width, self._height))
        pg.display.set_caption("The hardest game")
        self.clock = pg.time.Clock()
        self.running = True
        scene = self.handle_menu_button()

        while self.running:

            if self.scene == "play":
                if self.ready_duration>0:
                    self.ready_duration-=1
                else:
                    scene = self.play_one_image()
            
            elif self.scene == "menu" or self.scene == "final_win":
                scene.update(self.selected_button)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                
                elif self.scene == "menu":
                    scene = self.handle_buttons(scene,event,[self.handle_start_button,self.handle_levels_button,self.handle_quit_button])

                elif self.scene == "levels":
                    list_handle_button = []
                    for i in range(len(self.levels)):
                        list_handle_button.append(lambda level_index=i: self.handle_start_button(level_index))
                    list_handle_button.append(self.handle_menu_button)
                    scene = self.handle_buttons(scene,event,list_handle_button)
                
                elif self.scene == "game_over":
                    scene = self.handle_buttons(scene,event,[self.handle_play_button,self.handle_menu_button])
                
                elif self.scene == "win":
                    scene = self.handle_buttons(scene,event,[self.handle_next_button,self.handle_reset_button,self.handle_menu_button])
                
                elif self.scene == "final_win":
                    scene = self.handle_buttons(scene,event,[self.handle_menu_button])

            pg.display.flip()

            self.clock.tick(60)
        
        pg.quit()
    

    # ------------------------------------------ play methods ----------------------------------------------------

    def play_one_image(self):
        self.screen.fill(self._background_color)
        self.update_area()
        scene = self.update_timer()
        if scene:
            return scene
        self.update_player()
        self.update_coins()
        scene = self.update_ennemies_and_defeat()
        if scene:
            return scene
        return self.update_win()


    def update_coins(self):
        for coin in self.level.coins:
            if coin.is_active == 1:
                if coin.get_rect().colliderect(self.player.get_rect()):
                    self.sound_manager.playSound("coin")
                    coin.is_active = 0
                else:
                    coin.draw(self.screen)

    def update_ennemies_and_defeat(self):
        for ennemy in self.level.ennemies:
            if ennemy.get_rect().colliderect(self.player.get_rect()):
                return self.game_over()

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
            self.sound_manager.stop_Music()
            self.sound_manager.playSound("win")
            self.scene = "win"
            self.screen.fill(self._background_color)
            self.selected_button = 0
            scene = Win(self.screen)
            scene.select_button(self.selected_button)
            self.display_nb_deaths()
            self.display_time()
            return scene
        
    def update_timer(self):
        if self.level.timer:
            self.level.timer.update_bar(self.screen)
            if self.level.timer.is_finish():
                return self.game_over()

    # ------------------------------------------ some methods ----------------------------------------------------


    def restore_game(self):
        self.level.__init__(WIDTH,HEIGHT)
        self.player = Player(self.level.entry.get_x(),self.level.entry.get_y())
        
    def handle_buttons(self, scene, event, list_handle_button):
        i=-1
        
        if event.type == pg.MOUSEBUTTONDOWN:
            i = scene.has_click_on_button(event.pos)
        
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_DOWN:
                scene.deselect_button(self.selected_button)
                self.selected_button = (self.selected_button + 1) % len(scene.buttons_rect)
                scene.select_button(self.selected_button)
            if event.key == pg.K_UP:
                scene.deselect_button(self.selected_button)
                self.selected_button = (self.selected_button - 1) % len(scene.buttons_rect)
                scene.select_button(self.selected_button)
            if event.key == pg.K_RETURN:
                i = self.selected_button
        
        if i == -1:
            return scene
        self.sound_manager.stop_all_sounds()
        self.sound_manager.stop_Music()
        self.sound_manager.playSound("button_click")
        return list_handle_button[i]()
    
    def game_over(self):
        self.sound_manager.stop_Music()
        self.sound_manager.playSound("game_over")
        self.sound_manager.playMusic("game_over_bg")
        self.scene = "game_over"
        self.screen.fill(self._background_color)
        self.selected_button = 0
        self.nb_dead += 1
        scene = Game_over(self.screen)
        scene.select_button(self.selected_button)
        self.display_nb_deaths()
        self.display_time()
        return scene
    
    def display_nb_deaths(self):
        font = pg.font.Font(None, 40)
        text_deaths = font.render(f'number of deaths: {self.nb_dead}',1,(255,255,255))
        self.screen.blit(text_deaths, (20, 300))

    def display_time(self):
        font = pg.font.Font(None, 40)
        text_time = font.render(f'time: {round(time() - self.time_start - 1, 2)}',1,(255,255,255))
        self.screen.blit(text_time, (20, 350))
    
    
    # ------------------------------------------ button behavior ----------------------------------------------------

    def handle_menu_button(self):
        self.sound_manager.playMusic("menu_bg")
        self.scene = "menu"
        self.selected_button = 0
        scene = Menu(self.screen)
        scene.select_button(self.selected_button)
        return scene
    
    def handle_levels_button(self):
        self.scene = "levels"
        self.screen.fill(self._background_color)
        self.selected_button = 0
        scene = Levels(self.screen)
        scene.select_button(self.selected_button)
        return scene
    
    def handle_play_button(self):
        self.restore_game()
        if self.level.timer:
            self.sound_manager.playMusic("timer_bg")
        else:
            self.sound_manager.playMusic("play_bg")
        self.scene = "play"
        self.ready_duration = 60
        self.screen.fill(self._background_color)
        Ready(self.screen)
        self.time_start = time()

    def handle_start_button(self, i = 0):
        self.level = self.levels[i]
        self.handle_play_button()
        self.nb_dead = 0

    def handle_reset_button(self):
        self.handle_play_button()
        self.nb_dead = 0

    def handle_quit_button(self):
        self.running = False

    def handle_next_button(self):
        indice = self.levels.index(self.level)+1
        if indice<len(self.levels):
            self.handle_start_button(indice)
        else:
            self.sound_manager.playSound("final_win")
            self.scene = "final_win"
            self.selected_button = 0
            scene = Final_win(self.screen)
            scene.select_button(self.selected_button)
            return scene


if __name__ == '__main__':
    game = Game(Level0(WIDTH,HEIGHT))
    game.playGUI()