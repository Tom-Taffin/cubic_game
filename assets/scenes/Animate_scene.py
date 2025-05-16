import pygame as pg
from assets.scenes.Scene import Scene

class Animate_scene(Scene):

    def __init__(self, screen, width:int, height:int, banner_name:str, background_name:str):
        super().__init__(screen, width, height, banner_name)
        self.current_image = 0
        self.images = animations.get(background_name)
        self.tick = 7

    def update(self, selected_button):
        if self.tick == 0:
            self.tick = 7
            self.current_image = (self.current_image+1)%len(self.images)
            self.image = self.images[self.current_image]
            self.image = pg.transform.scale(self.image,(800,620))
            self.screen.blit(self.image,(0,0))
            self.screen.blit(self.banner, self.banner_rect)
            for i in range(len(self.buttons)):
                self.screen.blit(self.buttons[i], self.buttons_rect[i])
            self.select_button(selected_button)
        else:
            self.tick-=1



def load_animation_images(background_name, nb_images):
    images = []
    path = f"images/{background_name}/{background_name}"
    for i in range(1,nb_images+1):
        images.append(pg.image.load(path + str(i) + ".jpg"))
    return images

animations = {
    "background_congradulation":load_animation_images("background_congradulation",12),
    "background_menu":load_animation_images("background_menu",16)
}