import pygame as pg
from assets.scenes.Scene import Scene

class Game_over(Scene):

    def __init__(self, screen):
        super().__init__(screen,screen.get_width()//2,screen.get_height()//4,"images/game_over.png")
        super().add_button("images/play.jpg")
        super().add_button("images/menu.jpg")

