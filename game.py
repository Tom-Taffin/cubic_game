import pygame as pg
from time import time
import random as rd

from assets.Game_logic import Game_logic
from assets.Screen_manager import Screen_manager
from assets.Sound_manager import Sound_manager
from assets.Player import Player


from assets.levels.Level1_stage1 import Level1_stage1


from assets.scenes.Levels_scene import Levels_manager
from assets.scenes.Menu import Menu
from assets.scenes.Game_over import Game_over
from assets.scenes.Win import Win
from assets.scenes.Final_win import Final_win
from assets.scenes.Ready import Ready
from assets.scenes.Pause import Pause
from assets.scenes.Option import Option

WIDTH = 800
HEIGHT = 600

class Game:

    def __init__(self):
        self.screen_manager = Screen_manager(WIDTH,HEIGHT)
        self.sound_manager = Sound_manager()
        self.levels_manager = Levels_manager(self)
        self.game_logic = Game_logic(self.screen_manager,self.sound_manager)
        
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
        scene = self.handle_menu_button()

        while self.running:

            if self.scene == "play":
                if self.ready_duration>0:
                    self.ready_duration-=1
                else:
                    scene = self.play_one_image()
            
            elif not self.scene == "pause":
                scene.update(self.selected_button)
                if self.scene in ["game_over","win"]:
                    self.screen_manager.display_nb_deaths(self.game_logic.nb_deaths)
                    self.screen_manager.display_time(self.game_logic.time)
                if self.scene == "win":
                    self.screen_manager.display_best_time(self.game_logic.best_times.get_best_time(self.game_logic.current_level_index),self.game_logic.has_new_record)


            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                
                elif self.scene == "play" and event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    scene = self.handle_pause_button()
                
                elif self.scene == "menu":
                    scene = self.handle_buttons(scene,event,[self.handle_start_button,self.handle_levels_button,self.handle_option_button,self.handle_quit_button])
                
                elif self.scene == "levels":
                    list_handle_button = self.levels_manager.get_buttons_action()
                    scene = self.handle_buttons(scene,event,list_handle_button)
                    
                elif self.scene == "game_over":
                    scene = self.handle_buttons(scene,event,[self.handle_play_button,self.handle_menu_button])
                
                elif self.scene == "win":
                    scene = self.handle_buttons(scene,event,[self.handle_next_level_button,self.handle_reset_button,self.handle_menu_button])
                
                elif self.scene == "pause":
                    scene = self.handle_buttons(scene,event,[self.handle_continue_button,self.handle_menu_button])

                elif self.scene == "final_win":
                    scene = self.handle_buttons(scene,event,[self.handle_menu_button])
                
                elif self.scene == "option":
                    scene = self.handle_buttons(scene,event,[lambda scene=scene: self.handle_sounds_button(scene),lambda scene=scene: self.handle_reset_records_button(scene),self.handle_menu_button])

            self.screen_manager.update_display()
        
        pg.quit()
    

    # ------------------------------------------ play methods ----------------------------------------------------

    def play_one_image(self):
        self.game_logic.update_level()
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
        self.scene = "game_over"
        self.selected_button = 0
        scene = Game_over(self.screen_manager.get_screen())
        scene.select_button(self.selected_button)
        return scene

    def update_win(self):
        if self.game_logic.is_win():
            self.game_logic.win()
            self.scene = "win"
            self.selected_button = 0
            scene = Win(self.screen_manager.get_screen())
            scene.select_button(self.selected_button)
            return scene

    # ------------------------------------------ event methods ----------------------------------------------------
        
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
        new_scene = list_handle_button[i]()
        self.sound_manager.play_sound("button_click", self.game_logic.sounds_enabled)
        if new_scene:
            return new_scene
        return scene
    
    # ------------------------------------------ button behavior ----------------------------------------------------

    def handle_menu_button(self):
        self.game_logic.handle_menu_button()
        self.scene = "menu"
        self.selected_button = 0
        scene = Menu(self.screen_manager.get_screen())
        scene.select_button(self.selected_button)
        return scene
    
    def handle_levels_button(self):
        self.game_logic.handle_levels_button()
        scene = self.levels_manager.update_scene(1)
        return scene
    
    def handle_play_button(self):
        self.game_logic.handle_play_button()
        self.scene = "play"
        self.ready_duration = 60
        Ready(self.screen_manager.get_screen())

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
            self.scene = "final_win"
            self.selected_button = 0
            scene = Final_win(self.screen_manager.get_screen())
            scene.select_button(self.selected_button)
            return scene
        
    def handle_pause_button(self):
        if self.ready_duration==0:
            self.game_logic.handle_pause_button()
            self.scene = "pause"
            self.selected_button = 0
            scene = Pause(self.screen_manager.get_screen())
            scene.select_button(self.selected_button)
            return scene
    
    def handle_continue_button(self):
        self.game_logic.handle_continue_button()
        self.scene = "play"
        self.ready_duration = 60
        self.screen_manager.clear_screen()
        Ready(self.screen_manager.get_screen())

    def handle_option_button(self):
        self.game_logic.handle_option_button()
        self.scene = "option"
        self.selected_button = 0
        scene = Option(self.screen_manager.get_screen(), self.game_logic.sounds_enabled)
        scene.select_button(self.selected_button)
        return scene
    
    def handle_sounds_button(self, scene):
        self.game_logic.handle_sounds_button()
        scene.sounds = self.game_logic.sounds_enabled
        scene.update_sound_button()

    def handle_reset_records_button(self, scene):
        self.game_logic.handle_reset_button()
        scene.click_reset_button()

    def handle_next_stage_button(self, current_stage_number):
        scene = self.levels_manager.update_scene(current_stage_number+1)
        return scene
    
    def handle_back_stage_button(self, current_stage_number):
        scene = self.levels_manager.update_scene(current_stage_number-1)
        return scene



if __name__ == '__main__':
    game = Game()
    game.playGUI()