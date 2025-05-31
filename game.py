import pygame as pg
import random as rd

from assets.Game_logic import Game_logic
from assets.Scene_manager import Scene_manager
from assets.Screen_manager import Screen_manager
from assets.Sound_manager import Sound_manager
from assets.Player import Player

from assets.levels.Level1_stage1 import Level1_stage1
from assets.scenes.Levels_scene import Levels_manager

WIDTH = 800
HEIGHT = 600

class Game:

    def __init__(self):
        self.screen_manager = Screen_manager(WIDTH,HEIGHT)
        self.sound_manager = Sound_manager()
        self.levels_manager = Levels_manager(self)
        self.game_logic = Game_logic(self.screen_manager,self.sound_manager)
        self.scene_manager = Scene_manager(self)
        
        # apprentissage supervisé
        self.score = 0
    
    # apprentissage supervisé


    def state(self):
        """return the state vector with the coordinates of the player, coins, enemies and exit"""
        res = []
        res.append(self.game_logic.player.get_x())
        res.append(self.game_logic.player.get_y())
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

        self.game_logic.player.step(action, width, height)

        self.screen.fill(self.screen_manager.background_color)
        self.level.entry.draw(self.screen)
        self.level.exit.draw(self.screen)

        for coin in self.level.coins:
            if coin.is_active == 1 and coin.get_rect().colliderect(self.game_logic.player.get_rect()):
                coin.is_active = 0
                self.score += 20
                reward += 20
            else:
                coin.draw(self.screen)
        
        for ennemy in self.level.ennemies:
            ennemy.move(self.screen_manager.width, self.screen_manager.height)
            if ennemy.get_rect().colliderect(self.game_logic.player.get_rect()):
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
        
        if self.level.exit.get_rect().colliderect(self.game_logic.player.get_rect()):
            if not has_coin_active :
                self.score += 100
                reward += 100
                return reward, 1
            else :
                self.score -= 0.01
                reward -= 0.01
        
        self.game_logic.player.draw(self.screen)

        pg.display.flip()

        return reward, 0

    def play(self):
        for i in range(100):
            action = rd.randrange(5)
            print(action)
            done = self.step(action, self.screen_manager.width, self.screen_manager.height)
            print(self.state())
            print(self.score)
            print(done)

    def initScreen(self):
        pg.init()
        self.screen = pg.display.set_mode((self.screen_manager.width, self.screen_manager.height))
        self.clock = pg.time.Clock()
        self.running = True
        self.screen_manager.background_color = pg.Color(0, 0, 0)
    
    def initGame(self):
        self.level = Level1_stage1(WIDTH,HEIGHT)
        self.game_logic.player = Player(self.level.entry.get_x(),self.level.entry.get_y())
        self.score = 0

    # jeu classique
    
    def playGUI(self):

        self.screen_manager.init_display()
        self.running = True
        self.handle_menu_button()

        while self.running:

            self.scene_manager.update()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                
                else:
                    self.scene_manager.handle_events(event)

            self.screen_manager.update_display()
        
        pg.quit()
    

    # ------------------------------------------ play methods ----------------------------------------------------

    def play_one_image(self):
        if not self.game_logic.update_level(): # update_level return True if it is necessary to wait
            self.screen_manager.clear_screen()
            self.game_logic.update_area()
            game_over = self.game_logic.update_timer()
            if game_over:
                return self.game_over()
            self.game_logic.update_player()
            self.game_logic.update_coins()
            game_over = self.game_logic.update_ennemies_and_defeat()
            if game_over:
                return self.game_over()
            return self.update_win()

    def game_over(self):
        self.game_logic.game_over()
        self.scene_manager.change_scene("game_over")

    def update_win(self):
        if self.game_logic.is_win():
            self.game_logic.win()
            self.scene_manager.change_scene("win")
    
    # ------------------------------------------ button behavior ----------------------------------------------------

    def handle_menu_button(self):
        self.game_logic.handle_menu_button()
        self.scene_manager.change_scene("menu")
    
    def handle_levels_button(self):
        self.game_logic.handle_levels_button()
        self.scene_manager.change_scene("levels")
    
    def handle_play_button(self):
        self.game_logic.handle_play_button()
        self.scene_manager.change_scene("play")

    def handle_start_button(self, i = 0):
        self.game_logic.handle_start_button(i)
        self.handle_play_button()

    def handle_reset_button(self):
        self.game_logic.handle_reset_button()
        self.handle_play_button()

    def handle_quit_button(self):
        self.running = False

    def handle_next_level_button(self):
        index = self.game_logic.current_level_index + 1
        if index < len(self.game_logic.levels):
            self.handle_start_button(index)
        else:
            self.game_logic.handle_final_win()
            self.scene_manager.change_scene("final_win")
        
    def handle_pause_button(self):
        if self.scene_manager.ready_duration==0:
            self.game_logic.handle_pause_button()
            self.scene_manager.change_scene("pause")
    
    def handle_continue_button(self):
        self.game_logic.handle_continue_button()
        self.scene_manager.change_scene("play")

    def handle_option_button(self):
        self.game_logic.handle_option_button()
        self.scene_manager.change_scene("option")
    
    def handle_sounds_button(self, scene):
        self.game_logic.handle_sounds_button()
        scene.sounds = self.game_logic.sounds_enabled
        scene.update_sound_button()

    def handle_reset_records_button(self, scene):
        self.game_logic.handle_reset_button()
        scene.click_reset_button()

    def handle_next_stage_button(self, current_stage_number):
        self.scene_manager.current_scene = self.levels_manager.update_scene(current_stage_number+1)
    
    def handle_back_stage_button(self, current_stage_number):
        self.scene_manager.current_scene = self.levels_manager.update_scene(current_stage_number-1)

if __name__ == '__main__':
    game = Game()
    game.playGUI()