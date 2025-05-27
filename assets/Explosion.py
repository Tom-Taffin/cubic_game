import pygame as pg
class Explosion:
    def __init__(self,x,y,width,height):
        self.images = []
        self.current_image = 0
        self.tick = 0
        self.rect = (x,y,width,height)
        for image in images:
            self.images.append(pg.transform.scale(image,(width,height)))
        
    def update(self, screen):
        if self.tick == 0:
            self.tick = 4
            self.image = self.images[self.current_image]
            self.current_image +=1
        else:
            self.tick-=1
        screen.blit(self.image,self.rect)
    
    def is_finish(self):
        return self.tick == 1 and self.current_image == 5

images = []
for i in range(1,6):
    images.append(pg.image.load(f"images/explosion/exp{i}.png"))
