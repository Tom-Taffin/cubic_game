from assets.scenes.Animate_scene import Animate_scene
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Stage_config:
    name: str
    banner_image: str
    background_animation: str
    levels: List[str]

class Stage_manager:
    
    def __init__(self):
        self.stages = self._initialize_stages()
    
    def _initialize_stages(self) -> Dict[int, Stage_config]:
        return {
            1: Stage_config(
                name="Stage 1",
                banner_image="images/stage1.png",
                background_animation="main_background",
                levels=["level1.jpg", "level2.jpg", "level3.jpg", "level4.jpg", "level5.jpg", "level6.jpg"]
            ),
            2: Stage_config(
                name="Stage 2", 
                banner_image="images/stage2.png",
                background_animation="main_background",
                levels=["level1.jpg", "level2.jpg", "level3.jpg", "level4.jpg", "level5.jpg"]
            ),
            3: Stage_config(
                name="Stage 3",
                banner_image="images/stage3.png", 
                background_animation="main_background",
                levels=["level1.jpg", "level2.jpg", "level3.jpg", "level4.jpg", "level5.jpg"]
            )
        }
    
    def add_stage(self, stage_number: int, config: Stage_config):
        self.stages[stage_number] = config
    
    def add_level_to_stage(self, stage_number: int, level_image: str):
        if stage_number in self.stages:
            self.stages[stage_number].levels.append(level_image)
    
    def get_stage_config(self, stage_number: int) -> Stage_config:
        return self.stages.get(stage_number)
    
    def get_total_stages(self) -> int:
        return len(self.stages)
    
    def get_levels_for_stage(self, stage_number: int) -> List[str]:
        """Récupère les niveaux d'une page spécifique d'un stage"""
        if stage_number not in self.stages:
            return []
        
        return self.stages[stage_number].levels
    


class Levels_scene(Animate_scene):
    
    def __init__(self, screen, stage_manager: Stage_manager, stage_number: int):
        self.stage_manager = stage_manager
        self.stage_number = stage_number
        
        stage_config = stage_manager.get_stage_config(stage_number)
        if not stage_config:
            raise ValueError(f"Stage {stage_number} not found")
        
        super().__init__(
            screen, 
            screen.get_width()//2, 
            screen.get_height()//8,
            stage_config.banner_image, 
            stage_config.background_animation
        )
        
        self._add_level_buttons()
        
        self._add_navigation_buttons()
    
    def _add_level_buttons(self):
        levels = self.stage_manager.get_levels_for_stage(self.stage_number)
        for level_image in levels:
            self.add_button(f"images/{level_image}")
    
    def _add_navigation_buttons(self):
        
        if self.stage_number > 1:
            self.add_button("images/back.jpg")
        
        if self.stage_number < self.stage_manager.get_total_stages():
            self.add_button("images/next.jpg")
        
        self.add_button("images/menu.jpg")
    
    def get_button_actions(self) -> List[str]:

        actions = []
        
        levels = self.stage_manager.get_levels_for_stage(self.stage_number)
        start_index = sum(len(self.stage_manager.get_levels_for_stage(i)) for i in range(1,self.stage_number))
        for i in range(len(levels)):

            actions.append(f"level_{start_index+i}")
        
        if self.stage_number > 1:
            actions.append("back")
        if self.stage_number < self.stage_manager.get_total_stages():
            actions.append("next")
        
        actions.append("menu")
        
        return actions


class Levels_manager:
    
    def __init__(self, game_instance):
        self.game = game_instance
        self.stage_manager = Stage_manager()
        self.current_scene = None
    
    def update_scene(self, stage_number: int):
        self.current_scene = Levels_scene(
            self.game.screen_manager.get_screen(), 
            self.stage_manager, 
            stage_number
        )
        self.game.scene_manager.selected_button = 0
        self.current_scene.select_button(self.game.scene_manager.selected_button)
        return self.current_scene
    
    def get_buttons_action(self):
        actions = self.current_scene.get_button_actions()
        res = []
        
        for action in actions:
            if action.startswith("level_"):
                level_index = int(action.split("_")[1])
                res.append(lambda level_index=level_index: self.game.handle_start_button(level_index))
            
            elif action == "back":
                res.append(lambda : self.game.handle_back_stage_button(self.current_scene.stage_number))
            
            elif action == "next":
                res.append(lambda : self.game.handle_next_stage_button(self.current_scene.stage_number))
            
            elif action == "menu":
                res.append(self.game.handle_menu_button)
        
        return res
    
    def add_new_stage(self, stage_number: int, name: str, banner: str, animation: str, levels: List[str]):
        config = Stage_config(
            name=name,
            banner_image=banner,
            background_animation=animation,
            levels=levels
        )
        self.stage_manager.add_stage(stage_number, config)
    
    def add_level_to_existing_stage(self, stage_number: int, level_image: str):
        self.stage_manager.add_level_to_stage(stage_number, level_image)