from assets.scenes.Scene import Scene

class Win(Scene):

    def __init__(self, screen):
        super().__init__(screen,screen.get_width()//2,screen.get_height()//4,"images/win.jpg")
        super().add_button("images/next.jpg")
        super().add_button("images/reset.jpg")
        super().add_button("images/menu.jpg")