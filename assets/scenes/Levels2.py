from assets.scenes.Animate_scene import Animate_scene

class Levels2(Animate_scene):

    def __init__(self, screen):
        super().__init__(screen,screen.get_width()//2,screen.get_height()//8,"images/level_select.jpg", "main_background")
        super().add_button("images/level5.jpg")
        super().add_button("images/level6.jpg")
        super().add_button("images/level7.jpg")
        super().add_button("images/level8.jpg")
        super().add_button("images/back.jpg")
        super().add_button("images/menu.jpg")