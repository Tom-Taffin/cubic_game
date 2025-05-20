from assets.scenes.Animate_scene import Animate_scene

class Levels(Animate_scene):

    def __init__(self, screen):
        super().__init__(screen,screen.get_width()//2,screen.get_height()//8,"images/level_select.jpg", "main_background")
        super().add_button("images/level0.jpg")
        super().add_button("images/level1.jpg")
        super().add_button("images/level2.jpg")
        super().add_button("images/level3.jpg")
        super().add_button("images/level4.jpg")
        super().add_button("images/next.jpg")
        super().add_button("images/menu.jpg")