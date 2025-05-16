import pygame as pg

class Sound_manager:

    def __init__(self):
        pg.mixer.init()
        self.sounds = {
            "game_over": pg.mixer.Sound("sounds/game_over.mp3")
        }
    
    def play(self, name):
        self.sounds[name].play()