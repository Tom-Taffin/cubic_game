from assets.scenes.Scene import Scene

class Ready(Scene):

    def __init__(self, screen):
        super().__init__(screen,screen.get_width()//2,screen.get_height()//2,"images/ready.jpg")
