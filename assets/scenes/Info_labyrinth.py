from assets.scenes.Information_scene import Information_scene
import pygame as pg

class Info_labyrinth(Information_scene):

    def __init__(self, screen):
        super().__init__(screen,screen.get_width()//2,screen.get_height()//4,"images/info_banner.png")
        self.add_button("images/quit.jpg")

    def display_info(self):
        pg.draw.rect(self.screen, pg.Color(255,0,0), pg.Rect(120,200,30,30))
        super().draw_text("The hunter: he chases you, taking the shortest path to you.",(160,208), 25)
        
        pg.draw.rect(self.screen, pg.Color(227, 71, 11), pg.Rect(50,300,30,30))
        super().draw_text("The Blocker: He tries to predict where you're going and goes there to block you.",(90,308), 25)

        pg.draw.rect(self.screen, pg.Color(245, 39, 121), pg.Rect(40,400,30,30))
        super().draw_text("The patroller: it patrols between two points but if you get too close it chases you.",(80,408), 25)