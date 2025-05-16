import pygame as pg

class Timer:

    def __init__(self, time:float):
        self.percent = 0
        self.speed = 100/(time*60)

    def add_percent(self, screen):
        self.percent += self.speed

    def update_bar(self, screen):
        self.add_percent(screen)
        pg.draw.rect(screen,(3,92,3),[40, 1, screen.get_width()-80, 10])
        pg.draw.rect(screen,(9,232,9),[40, 1, ((screen.get_width()-80) / 100) * self.percent, 10])

    def is_finish(self):
        return self.percent >= 100
    
    def reset(self):
        self.percent = 0