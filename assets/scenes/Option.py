from assets.scenes.Animate_scene import Animate_scene
import pygame as pg

class Option(Animate_scene):

    def __init__(self, screen, sound):
        super().__init__(screen,screen.get_width()//2,screen.get_height()//6,"images/game_name.png", "main_background")
        super().add_button("images/on.jpg")
        super().add_button("images/reset.jpg")
        super().add_button("images/menu.jpg")
        self.on_button = pg.image.load("images/on.jpg")
        self.on_button = pg.transform.scale(self.on_button,(self.banner_rect.width//3,self.banner_rect.height//2))
        self.off_button = pg.image.load("images/off.jpg")
        self.off_button = pg.transform.scale(self.off_button,(self.banner_rect.width//3,self.banner_rect.height//2))
        self.on_button_selected = pg.image.load("images/on_selected.jpg")
        self.on_button_selected = pg.transform.scale(self.on_button_selected,(self.banner_rect.width//3,self.banner_rect.height//2))
        self.off_button_selected = pg.image.load("images/off_selected.jpg")
        self.off_button_selected = pg.transform.scale(self.off_button_selected,(self.banner_rect.width//3,self.banner_rect.height//2))
        
        self.reset_button_clicked = pg.image.load("images/reset_clicked.jpg")
        self.reset_button_clicked = pg.transform.scale(self.reset_button_clicked,(self.banner_rect.width//3,self.banner_rect.height//2))
        self.reset_button_selected_clicked = pg.image.load("images/reset_selected_clicked.jpg")
        self.reset_button_selected_clicked = pg.transform.scale(self.reset_button_selected_clicked,(self.banner_rect.width//3,self.banner_rect.height//2))

        self.sounds = sound
        self.update_sound_button()
        
    def update(self, selected_button):
        super().update(selected_button)
        font = pg.font.Font(None, 50)
        text_time = font.render(f'sounds:',1,(255,255,255))
        self.screen.blit(text_time, (190, 216))
        font = pg.font.Font(None, 50)
        text_time = font.render(f'records:',1,(255,255,255))
        self.screen.blit(text_time, (187, 278))
    

    def update_sound_button(self):
        self.buttons[0] = self.on_button if self.sounds else self.off_button
        self.selected_buttons[0] = self.on_button_selected if self.sounds else self.off_button_selected

    def click_reset_button(self):
        self.buttons[1] = self.reset_button_clicked
        self.selected_buttons[1] = self.reset_button_selected_clicked