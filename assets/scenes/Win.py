from assets.scenes.Animate_scene import Animate_scene

class Win(Animate_scene):

    def __init__(self, screen):
        super().__init__(screen,screen.get_width()//2,screen.get_height()//4,"images/win.png","main_background")
        super().add_button("images/next.jpg")
        super().add_button("images/reset.jpg")
        super().add_button("images/menu.jpg")