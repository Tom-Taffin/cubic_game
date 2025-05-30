import pygame as pg

class Screen_manager:
    def __init__(self, width:int=800, height:int=600):
        self.width = width
        self.height = height
        self.screen = None
        self.clock = None
        self.background_color = pg.Color(0, 0, 0)
    
    def init_display(self):
        # Initializing the pygame screen
        pg.init()
        self.screen = pg.display.set_mode((self.width, self.height))
        pg.display.set_caption("The hardest game")
        icon = pg.image.load("images/icon.jpg")
        pg.display.set_icon(icon)
        self.clock = pg.time.Clock()
    
    def clear_screen(self):
        # clear the screen
        self.screen.fill(self.background_color)
    
    def update_display(self):
        # Update the display
        pg.display.flip()
        self.clock.tick(60)

    def get_screen(self):
        return self.screen
    
    def get_clock(self):
        return self.clock
    
    def draw_text(self, text:str, position:tuple[int], font_size:int=40, color:tuple[int]=(255, 255, 255), font_name:str=None):
        # display text on the screen
        font = pg.font.Font(font_name, font_size)
        text = font.render(text,1,color)
        self.screen.blit(text, position)

    def display_nb_deaths(self, nb_deaths):
        # display the number of death
        self.draw_text(f'number of deaths: {nb_deaths}',(20, 300))

    def display_time(self, time):
        # display the time
        self.draw_text(f'time: {time}',(20, 350))

    def display_best_time(self, best_time, has_new_record):
        # display the best time
        self.draw_text(f'best time : {best_time}',(20, 400))
        if has_new_record:
            self.draw_text('NEW RECORD !',(20, 425), color=(255, 215, 0))

    