from assets.scenes.Animate_scene import Animate_scene

class Final_win(Animate_scene):

    def __init__(self, screen):
        super().__init__(screen,screen.get_width()//2,screen.get_height()//4,"images/congradulation.jpg","background_congradulation")
        super().add_button("images/menu.jpg")