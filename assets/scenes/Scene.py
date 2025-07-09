import pygame as pg

class Scene:

    def __init__(self, screen, width:int, height:int, banner_name:str):
        """create and display the scene on the screen"""
        self.banner = pg.image.load(banner_name)
        self.banner = pg.transform.scale(self.banner,(width,height))
        self.banner_rect = self.banner.get_rect()
        self.banner_rect.x = screen.get_width()//4
        self.banner_rect.y = screen.get_height()//6
        screen.blit(self.banner, self.banner_rect)
        self.buttons_rect = []
        self.buttons = []
        self.selected_buttons = []
        self.screen = screen

    def add_button(self, button_name:str):
        """create and display a new button"""
        button = pg.image.load(button_name)
        button = pg.transform.scale(button,(self.banner_rect.width//3,self.banner_rect.height//2))
        button_rect = pg.Rect(0,0,0,0)
        button_rect.x = self.banner_rect.x + self.banner_rect.width//3
        if len(self.buttons_rect) == 0:
            button_rect.y = self.banner_rect.bottom+10
        else:
            button_rect.y = self.buttons_rect[-1].bottom+10
        button_rect.width = self.banner_rect.width//3
        button_rect.height = self.banner_rect.height//2
        self.screen.blit(button, button_rect)
        self.buttons.append(button)
        self.buttons_rect.append(button_rect)

        selected_button = pg.image.load(button_name[:-4]+"_selected"+button_name[-4:])
        selected_button = pg.transform.scale(selected_button,(self.banner_rect.width//3,self.banner_rect.height//2))
        self.selected_buttons.append(selected_button)


    def has_click_on_button(self, pos):
        """return the index of the clicked button and -1 otherwise"""
        i = 0
        while i<len(self.buttons_rect):
            if (self.buttons_rect[i].collidepoint(pos)):
                return i
            i+=1
        return -1
    
    def select_button(self, i):
        """display the selected button"""
        self.screen.blit(self.selected_buttons[i], self.buttons_rect[i])

    def deselect_button(self, i):
        """display the button as unselected"""
        self.screen.blit(self.buttons[i], self.buttons_rect[i])