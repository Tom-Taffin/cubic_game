import pygame as pg
class Animation:
    """
    To create an animation: edit animations then while the animation is not finish, update the animation
    """

    def __init__(self,name,x,y,width,height):
        self.images = []
        self.current_image = 0
        self.tick = 0
        self.rect = (x,y,width,height)
        for image in animations[name]:
            self.images.append(pg.transform.scale(image,(width,height)))
        self.nb_images = len(self.images)
        
    def update(self, screen):
        if self.tick == 0:
            self.tick = 4
            self.image = self.images[self.current_image]
            self.current_image +=1
        else:
            self.tick-=1
        screen.blit(self.image,self.rect)
    
    def is_finish(self):
        return self.tick == 1 and self.current_image == self.nb_images


def load_animation_images(name, nb_images, type = "jpg"):
    images = []
    path = f"images/{name}/{name}"
    for i in range(1,nb_images+1):
        images.append(pg.image.load(path + str(i) + "." + type))
    return images

animations = {
    "explosion":load_animation_images("explosion",5,"png"),
    "boss":load_animation_images("boss",24),
    "circle":load_animation_images("circle",4)
}
animations["circle"]= animations["circle"]*4
