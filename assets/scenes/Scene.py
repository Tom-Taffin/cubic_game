import pygame as pg

class Scene:

    def __init__(self, screen, width:int, height:int, banner:str, button:str):
        self.banner = pg.image.load(banner)
        self.banner = pg.transform.scale(self.banner,(width,height))
        self.banner_rect = self.banner.get_rect()
        self.banner_rect.x = screen.get_width()//4
        self.banner_rect.y = screen.get_height()//4
        screen.blit(self.banner, self.banner_rect)
        self.first_button = pg.image.load(button)
        self.first_button = pg.transform.scale(self.first_button,(self.banner_rect.width//3,self.banner_rect.height//2))
        self.first_button_rect = self.banner.get_rect()
        self.first_button_rect.x = self.banner_rect.x + self.banner_rect.width//3
        self.first_button_rect.y = self.banner_rect.bottom+10
        self.first_button_rect.x = self.banner_rect.x + self.banner_rect.width//3
        self.first_button_rect.width = self.banner_rect.width//3
        self.first_button_rect.height = self.banner_rect.height//2
        screen.blit(self.first_button, self.first_button_rect)

    def has_click_on_first_button(self, pos):
        return self.first_button_rect.collidepoint(pos)