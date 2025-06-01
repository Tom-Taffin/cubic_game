import pygame as pg
from assets.scenes.Menu import Menu
from assets.scenes.Game_over import Game_over
from assets.scenes.Win import Win
from assets.scenes.Final_win import Final_win
from assets.scenes.Ready import Ready
from assets.scenes.Pause import Pause
from assets.scenes.Option import Option


class Scene_manager:
    """Centralized manager for all game scenes"""
    
    def __init__(self, game):
        self.game = game
        self.current_scene = None
        self.scene_name = "menu"
        self.selected_button = 0
        
        # Mapping scene names to their classes
        self.scene_classes = {
            "menu": Menu,
            "game_over": Game_over,
            "win": Win,
            "final_win": Final_win,
            "pause": Pause,
            "option": Option
        }
        
        # Mapping button actions for each scene
        self.scene_button_handlers = {
            "menu": [
                self.game.handle_start_button,
                self.game.handle_levels_button,
                self.game.handle_option_button,
                self.game.handle_quit_button
            ],
            "levels": [],  # Will be dynamically populated by Levels_manager
            "game_over": [
                self.game.handle_play_button,
                self.game.handle_menu_button
            ],
            "win": [
                self.game.handle_next_level_button,
                self.game.handle_reset_button,
                self.game.handle_menu_button
            ],
            "pause": [
                self.game.handle_continue_button,
                self.game.handle_menu_button
            ],
            "final_win": [
                self.game.handle_menu_button
            ],
            "option": [
                lambda: self.game.handle_sounds_button(self.current_scene),
                lambda: self.game.handle_reset_records_button(self.current_scene),
                self.game.handle_menu_button
            ]
        }
    
    def change_scene(self, scene_name):
        """Change the current scene"""
        self.scene_name = scene_name
        self.selected_button = 0
        
        if scene_name == "play":
            self.current_scene = None
        elif scene_name == "levels":
            self.current_scene = self.game.levels_manager.update_scene(1)
        elif scene_name in self.scene_classes:
            scene_class = self.scene_classes[scene_name]
            if scene_name == "option":
                self.current_scene = scene_class(
                    self.game.screen_manager.get_screen(),
                    self.game.game_logic.sounds_enabled
                )
            else:
                self.current_scene = scene_class(self.game.screen_manager.get_screen())
            self.current_scene.select_button(self.selected_button)
    
    def handle_events(self, event):
        """Handles events for the current scene"""
        if self.scene_name == "play":
            self._handle_play_events(event)
        else:
            self._handle_menu_events(event)
    
    def _handle_play_events(self, event):
        """Manages events during the game"""
        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            self.game.handle_pause_button()
    
    def _handle_menu_events(self, event):
        """Manages events in menus"""

        button_index = -1
        
        # Mouse click management
        if event.type == pg.MOUSEBUTTONDOWN:
            button_index = self.current_scene.has_click_on_button(event.pos)
        
        # Keyboard management
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_DOWN:
                self._select_next_button()
            elif event.key == pg.K_UP:
                self._select_previous_button()
            elif event.key == pg.K_RETURN:
                button_index = self.selected_button
        
        # Executing the button action
        if button_index != -1:
            self._execute_button_action(button_index)
    
    def _select_next_button(self):
        """Select the next button"""
        if self.current_scene and hasattr(self.current_scene, 'buttons_rect'):
            self.current_scene.deselect_button(self.selected_button)
            self.selected_button = (self.selected_button + 1) % len(self.current_scene.buttons_rect)
            self.current_scene.select_button(self.selected_button)
    
    def _select_previous_button(self):
        """Select the previous button"""
        if self.current_scene and hasattr(self.current_scene, 'buttons_rect'):
            self.current_scene.deselect_button(self.selected_button)
            self.selected_button = (self.selected_button - 1) % len(self.current_scene.buttons_rect)
            self.current_scene.select_button(self.selected_button)
    
    def _execute_button_action(self, button_index):
        """Performs the action corresponding to the selected button"""
        handlers = self._get_current_button_handlers()
        
        if button_index < len(handlers):
            handlers[button_index]()
            self.game.sound_manager.play_sound("button_click", self.game.game_logic.sounds_enabled)
    
    def _get_current_button_handlers(self):
        """Returns the button handlers for the current scene"""
        if self.scene_name == "levels":
            return self.game.levels_manager.get_buttons_action()
        else:
            return self.scene_button_handlers.get(self.scene_name, [])
    
    def update(self):
        """Updates the current scene"""
        if self.scene_name == "play":
            self.game.play_one_image()
        elif self.current_scene and self.scene_name != "pause":
            self.current_scene.update(self.selected_button)
            
            # Displaying scene-specific information
            if self.scene_name in ["game_over", "win"]:
                self.game.screen_manager.display_nb_deaths(self.game.game_logic.nb_deaths)
                self.game.screen_manager.display_time(self.game.game_logic.time)
                
            if self.scene_name == "win":
                self.game.screen_manager.display_best_time(
                    self.game.game_logic.best_times.get_best_time(self.game.game_logic.current_level_index),
                    self.game.game_logic.has_new_record
                )