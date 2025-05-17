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
    
    def playSound(self, name):
        self.sounds[name].play()

    def playMusic(self, name):
        pg.mixer.music.load(f"sounds/{name}.mp3")
        pg.mixer.music.play(-1)

    def stop_all_sounds(self):
        pg.mixer.stop()

    def stop_Music(self):
        pg.mixer.music.stop()