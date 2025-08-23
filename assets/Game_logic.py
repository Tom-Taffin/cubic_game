from time import time
from assets.Best_times import Best_times
from assets.Player import Player


from assets.levels.Level import Level
from assets.levels.Level1_stage1 import Level1_stage1
from assets.levels.Level2_stage1 import Level2_stage1
from assets.levels.Level3_stage1 import Level3_stage1
from assets.levels.Level4_stage1 import Level4_stage1
from assets.levels.Level5_stage1 import Level5_stage1
from assets.levels.Level6_stage1 import Level6_stage1
from assets.levels.Level1_stage2 import Level1_stage2
from assets.levels.Level2_stage2 import Level2_stage2
from assets.levels.Level3_stage2 import Level3_stage2
from assets.levels.Level4_stage2 import Level4_stage2
from assets.levels.Level5_stage2 import Level5_stage2
from assets.levels.Level1_stage3 import Level1_stage3
from assets.levels.Level2_stage3 import Level2_stage3
from assets.levels.Level3_stage3 import Level3_stage3
from assets.levels.Level4_stage3 import Level4_stage3
from assets.levels.Level5_stage3 import Level5_stage3
from assets.levels.Level1_stage4 import Level1_stage4
from assets.levels.Level2_stage4 import Level2_stage4
from assets.levels.Level3_stage4 import Level3_stage4
from assets.levels.Level4_stage4 import Level4_stage4
from assets.levels.Level5_stage4 import Level5_stage4
from assets.levels.Level1_stage5 import Level1_stage5
from assets.levels.Level2_stage5 import Level2_stage5
from assets.levels.Level3_stage5 import Level3_stage5
from assets.levels.Level4_stage5 import Level4_stage5
from assets.levels.Level5_stage5 import Level5_stage5

class Game_logic:

    """
    To manually add a level: edit manually self.levels
    """
    
    def __init__(self, screen_manager, sound_manager):
        WIDTH = screen_manager.width
        HEIGHT = screen_manager.height
        self.player = Player(0,0)
        self.levels = [Level1_stage1(WIDTH,HEIGHT),Level2_stage1(WIDTH,HEIGHT),Level3_stage1(WIDTH,HEIGHT),Level4_stage1(WIDTH,HEIGHT),Level5_stage1(WIDTH,HEIGHT),Level6_stage1(WIDTH,HEIGHT,self.player),
                       Level1_stage2(WIDTH,HEIGHT),Level2_stage2(WIDTH,HEIGHT),Level3_stage2(WIDTH,HEIGHT),Level4_stage2(WIDTH,HEIGHT),Level5_stage2(WIDTH,HEIGHT,self.player),
                       Level1_stage3(WIDTH,HEIGHT),Level2_stage3(WIDTH,HEIGHT),Level3_stage3(WIDTH,HEIGHT,self.player),Level4_stage3(WIDTH,HEIGHT),Level5_stage3(WIDTH,HEIGHT,self.player),
                       Level1_stage4(WIDTH,HEIGHT,self.player),Level2_stage4(WIDTH,HEIGHT,self.player),Level3_stage4(WIDTH,HEIGHT,self.player),Level4_stage4(WIDTH,HEIGHT,self.player),Level5_stage4(WIDTH,HEIGHT,self.player),
                       Level1_stage5(WIDTH,HEIGHT,self.player),Level2_stage5(WIDTH,HEIGHT,self.player),Level3_stage5(WIDTH,HEIGHT,self.player),Level4_stage5(WIDTH,HEIGHT,self.player),Level5_stage5(WIDTH,HEIGHT,self.player)
                       ]
        self.screen_manager = screen_manager
        self.sound_manager = sound_manager
        self.best_times = Best_times(self.levels)
        
        # State of the game
        self.level = self.levels[0]
        self.current_level_index = 0
        self.nb_deaths = 0
        self.time_start = 0
        self.time = 0
        self.has_new_record = False
        self.sounds_enabled = True # You can change the startup sound permission here

    # ------------------------------------------ play methods ----------------------------------------------------

    def has_coin_active(self):
        """Return true if there is at least one uncollected piece."""
        for coin in self.level.coins:
            if coin.is_active == 1:
                return True
        return False
    
    def is_win(self):
        """Return true if the player won."""
        return not self.has_coin_active() and self.level.exit.is_collision(self.player)
    
    def win(self):
        """Setup during victory."""
        self.sound_manager.stop_music()
        self.sound_manager.play_sound("win",self.sounds_enabled)
        self.sound_manager.play_music("win_bg",self.sounds_enabled)
        self.time = round(time() - self.time_start - self.intro_duration/60, 1)
        self.has_new_record = self.best_times.update_score(self.current_level_index,self.time)
    
    def game_over(self):
        """Setup during defeat."""
        self.sound_manager.stop_music()
        self.sound_manager.play_sound("game_over", self.sounds_enabled)
        self.sound_manager.play_music("game_over_bg", self.sounds_enabled)
        self.nb_deaths += 1
        self.time = round(time() - self.time_start - self.intro_duration/60, 1)

    def update_coins(self):
        """Update of the coins display"""
        for coin in self.level.coins:
            if coin.is_active == 1:
                if coin.is_collision(self.player):
                    self.sound_manager.play_sound("coin", self.sounds_enabled)
                    coin.is_active = 0
                else:
                    coin.draw(self.screen_manager.get_screen())

    def update_ennemies_and_defeat(self):
        """Update of the ennemies display and return true if the player loses."""
        for ennemy in self.level.ennemies:
            if ennemy.is_collision(self.player):
                return True

            else:
                ennemy.move(self.screen_manager.width, self.screen_manager.height)
                ennemy.draw(self.screen_manager.get_screen())
        return False
    
    def update_area(self):
        """Update of the areas display"""
        self.level.entry.draw(self.screen_manager.get_screen())
        self.level.exit.draw(self.screen_manager.get_screen())

    def update_player(self):
        """Update of the player display"""
        self.player.update(self.screen_manager.width, self.screen_manager.height)
        self.player.draw(self.screen_manager.get_screen())

    def update_timer_and_defeat(self):
        """Update of the timer display and return true if it's finished"""
        if self.level.timer:
            self.level.timer.update_bar(self.screen_manager.get_screen())
            if self.level.timer.is_finish():
                return True
        return False

    def update_level(self):
        """
        Returns true if it is necessary to wait and displays the intro.
        Otherwise, returns false if the intro is complete.
        """
        return self.level.update(self.screen_manager.get_screen())
    
    def draw_level(self):
        """
        Draw the necessary elements at the level
        """
        return self.level.draw(self.screen_manager.get_screen())

    def restore_game(self):
        """Restore the level to start a new game."""
        self.level.restore()
        self.player.get_rect().x = self.level.entry.get_x()
        self.player.get_rect().y = self.level.entry.get_y()
    
    # ------------------------------------------ button behavior ----------------------------------------------------

    def handle_menu_button(self):
        self.sound_manager.play_menu_sound(self.sounds_enabled)

    def handle_levels_button(self):
        pass

    def handle_play_button(self):
        self.sound_manager.stop_all_sounds()
        self.sound_manager.stop_music()
        self.restore_game()
        self.sound_manager.start_level_music(self.level, self.sounds_enabled)
        self.time_start = time()
        self.screen_manager.clear_screen()
        self.level.restore_ready_intro()
        self.intro_duration = self.level.intro_duration
    
    def handle_start_button(self, i = 0):
        self.level = self.levels[i]
        self.current_level_index = i
        self.nb_deaths = 0
        self.handle_play_button()
        self.level.restore_intro_duration()
        self.intro_duration = self.level.init_intro_duration

    def handle_reset_button(self):
        self.nb_deaths = 0

    def handle_final_win(self):
        self.sound_manager.stop_all_sounds()
        self.sound_manager.stop_music()
        self.sound_manager.play_sound("final_win",self.sounds_enabled)

    def handle_pause_button(self):
        self.sound_manager.play_menu_sound(self.sounds_enabled)
        self.time_start = time() - self.time_start - 1
        self.screen_manager.display_background("pause_bg.jpg", (1200,600), (-203,0))
    
    def handle_continue_button(self):
        self.sound_manager.stop_all_sounds()
        self.sound_manager.stop_music()
        self.sound_manager.start_level_music(self.level, self.sounds_enabled)
        self.time_start = time() - self.time_start
        self.level.restore_ready_intro()

    def handle_option_button(self):
        self.sound_manager.play_menu_sound(self.sounds_enabled)

    def handle_sounds_button(self):
        self.sounds_enabled = not self.sounds_enabled
        if not self.sounds_enabled:
            self.sound_manager.stop_all_sounds()
            self.sound_manager.stop_music()
        elif not self.sound_manager.is_playing_music():
            self.sound_manager.play_music("menu_bg", self.sounds_enabled)
    
    def handle_reset_records_button(self):
        self.best_times.reset()

    def handle_info_labyrinth_button(self):
        self.screen_manager.clear_screen()


