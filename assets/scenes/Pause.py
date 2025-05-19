from assets.scenes.Scene import Scene

class Pause(Scene):

    def __init__(self, screen):
        super().__init__(screen,screen.get_width()//2,screen.get_height()//4,"images/pause.png")
        super().add_button("images/play.jpg")
        super().add_button("images/menu.jpg")
