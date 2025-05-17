from assets.scenes.Scene import Scene

class Levels(Scene):

    def __init__(self, screen):
        super().__init__(screen,screen.get_width()//2,screen.get_height()//8,"images/level_select.jpg")
        super().add_button("images/level0.jpg")
        super().add_button("images/level1.jpg")
        super().add_button("images/level2.jpg")
        super().add_button("images/level3.jpg")
        super().add_button("images/level4.jpg")
        super().add_button("images/level5.jpg")
        super().add_button("images/menu.jpg")