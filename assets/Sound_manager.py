import pygame as pg

class Sound_manager:

    def __init__(self):
        pg.mixer.init()
        self.sounds = {
            "game_over" : pg.mixer.Sound("sounds/game_over.mp3"),
            "win" : pg.mixer.Sound("sounds/win.mp3"),
            "final_win" : pg.mixer.Sound("sounds/final_win.mp3"),
            "coin" : pg.mixer.Sound("sounds/coin.mp3"),
            "button_click" : pg.mixer.Sound("sounds/button_click.mp3")
        }
    
    def play_sound(self, name, sound):
        if sound:
            self.sounds[name].play()

    def play_music(self, name, sound):
        if sound:
            pg.mixer.music.load(f"sounds/{name}.mp3")
            pg.mixer.music.play(-1)

    def stop_all_sounds(self):
        pg.mixer.stop()

    def stop_music(self):
        pg.mixer.music.stop()
    
    def is_playing_music(self):
        return pg.mixer.music.get_busy()
    
    def start_level_music(self, level, sounds_enabled):       
        if level.timer:
            self.play_music("timer_bg", sounds_enabled)
        else:
            self.play_music("play_bg", sounds_enabled)

    def play_menu_sound(self, sounds_enabled):
        self.stop_all_sounds()
        self.stop_music()
        self.play_music("menu_bg", sounds_enabled)