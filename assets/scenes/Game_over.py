from assets.scenes.Animate_scene import Animate_scene

class Game_over(Animate_scene):

    def __init__(self, screen):
        super().__init__(screen,screen.get_width()//2,screen.get_height()//4,"images/game_over.png","main3_background")
        super().add_button("images/play.jpg")
        super().add_button("images/menu.jpg")

