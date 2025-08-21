from assets.scenes.Scene import Scene
import pygame as pg

class Information_scene(Scene):

    def __init__(self, screen, width:int, height:int, banner_name:str):
        super().__init__(screen,width,height,banner_name)
        self.banner_rect.y = screen.get_height()//10
        self.screen.fill(pg.Color(0,0,0))
        screen.blit(self.banner, self.banner_rect)
        self.display_info()
        

    def add_button(self, button_name:str):
        """create and display a new button"""
        button = pg.image.load(button_name)
        button = pg.transform.scale(button,(self.banner_rect.width//3,self.banner_rect.height//2))
        button_rect = pg.Rect(0,0,0,0)
        button_rect.x = self.banner_rect.x + self.banner_rect.width//3
        button_rect.width = self.banner_rect.width//3
        button_rect.height = self.banner_rect.height//2
        if len(self.buttons_rect) == 0:
            button_rect.y = self.screen.get_height() - 20 - button_rect.height
        else:
            button_rect.y = self.buttons_rect[-1].top - 10 - button_rect.height
        self.screen.blit(button, button_rect)
        self.buttons.append(button)
        self.buttons_rect.append(button_rect)

        selected_button = pg.image.load(button_name[:-4]+"_selected"+button_name[-4:])
        selected_button = pg.transform.scale(selected_button,(self.banner_rect.width//3,self.banner_rect.height//2))
        self.selected_buttons.append(selected_button)

    def display_info(self):
        pass

    def draw_text(self, text:str, position:tuple[int], font_size:int=40, color:tuple[int]=(255, 255, 255), font_name:str=None):
        """Display text on the screen"""
        font = pg.font.Font(font_name, font_size)
        text = font.render(text,1,color)
        self.screen.blit(text, position)