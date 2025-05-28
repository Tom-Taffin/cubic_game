from assets.ennemies.Ennemy_laser import Ennemy_laser
import pygame as pg

class Ennemy_laser_pulsation(Ennemy_laser):

    def __init__(self, x1:int, y1:int, x2:int, y2:int, width:int = 3, on_duration: int = 60, off_duration: int = 60, launch_duration = 0):
        super().__init__(x1, y1, x2, y2, width)
        self.on_duration = on_duration
        self.off_duration = off_duration
        self.launch_duration = launch_duration
        self.tick = off_duration
        self.active = False
    
    def move(self, board_width: int, board_height: int):
        self.tick += 1

        if self.launch_duration>0:
            self.launch_duration-=1

        elif self.active and self.tick >= self.on_duration:
            self.active = False
            self.tick = 0
        elif not self.active and self.tick >= self.off_duration:
            self.active = True
            self.tick = 0

    def draw(self, screen):
        if self.active:
            super().draw(screen)
        else:
            pg.draw.line(screen, pg.Color(100, 0, 0), 
                        (self.x1, self.y1), 
                        (self.x2, self.y2), self.width)
            
    def is_collision(self, other):
        if not self.active:
            return False
        return super().is_collision(other)