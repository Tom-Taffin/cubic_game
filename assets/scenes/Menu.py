from assets.scenes.Scene import Scene

class Menu(Scene):

    def __init__(self, screen):
        super().__init__(screen,screen.get_width()//2,screen.get_height()//6,"images/game_name.jpg")
        super().add_button("images/start.jpg")
        super().add_button("images/levels.jpg")
        super().add_button("images/quit.jpg")
