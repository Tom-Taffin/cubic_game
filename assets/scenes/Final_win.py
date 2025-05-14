from assets.scenes.Scene import Scene

class Final_win(Scene):

    def __init__(self, screen):
        super().__init__(screen,screen.get_width()//2,screen.get_height()//4,"images/congradulation.jpg")
        super().add_button("images/menu.jpg")