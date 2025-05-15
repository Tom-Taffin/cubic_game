import pygame as pg

class Scene:

    def __init__(self, screen, width:int, height:int, banner_name:str):
        self.banner = pg.image.load(banner_name)
        self.banner = pg.transform.scale(self.banner,(width,height))
        self.banner_rect = self.banner.get_rect()
        self.banner_rect.x = screen.get_width()//4
        self.banner_rect.y = screen.get_height()//6
        screen.blit(self.banner, self.banner_rect)
        self.buttons_rect = []
        self.buttons = []
        self.screen = screen

    def add_button(self, button_name:str):
        button = pg.image.load(button_name)
        button = pg.transform.scale(button,(self.banner_rect.width//3,self.banner_rect.height//2))
        button_rect = pg.Rect(0,0,0,0)
        button_rect.x = self.banner_rect.x + self.banner_rect.width//3
        if len(self.buttons_rect) == 0:
            button_rect.y = self.banner_rect.bottom+10
        else:
            button_rect.y = self.buttons_rect[-1].bottom+10
        button_rect.x = self.banner_rect.x + self.banner_rect.width//3
        button_rect.width = self.banner_rect.width//3
        button_rect.height = self.banner_rect.height//2
        self.screen.blit(button, button_rect)
        self.buttons.append(button_name)
        self.buttons_rect.append(button_rect)


    def has_click_on_button(self, pos):
        i = 0
        while i<len(self.buttons_rect):
            if (self.buttons_rect[i].collidepoint(pos)):
                return i
            i+=1
        return -1
    
    def select_button(self, i):
        button = pg.image.load(self.buttons[i][:-4]+"_selected"+self.buttons[i][-4:])
        button = pg.transform.scale(button,(self.banner_rect.width//3,self.banner_rect.height//2))
        self.screen.blit(button, self.buttons_rect[i])

    def deselect_button(self, i):
        button = pg.image.load(self.buttons[i])
        button = pg.transform.scale(button,(self.banner_rect.width//3,self.banner_rect.height//2))
        self.screen.blit(button, self.buttons_rect[i])