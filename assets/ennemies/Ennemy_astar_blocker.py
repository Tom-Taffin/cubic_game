from assets.ennemies.Ennemy_astar import Ennemy_astar
from assets.Player import Player
import pygame as pg

class Ennemy_astar_blocker(Ennemy_astar):
    """
    Ennemi style Pac-Man qui donne l'impression de bloquer sans calculs complexes.
    Il anticipe juste où va le joueur au lieu de calculer une position précise.
    """
    def __init__(self, x: int, y: int, speed: int, player: Player, map: list[int]):
        self.last_player_pos = (0, 0)
        super().__init__(x, y, speed, player, map)
        self._color = pg.Color(255, 165, 0)
        
    def calculate_path(self):
        """Calcule le chemin vers où le joueur semble aller"""
        start = (self.get_x()//40, self.get_y()//30)
        current_player_pos = (self.player.get_x()//40, self.player.get_y()//30)
        
        target = self.predict_player_movement(current_player_pos)
        
        self.last_player_pos = current_player_pos
        
        self.path = super().astar_search(start, target)
    
    def predict_player_movement(self, current_pos):
        """Prédit où va le joueur de manière simple"""
        px, py = current_pos
        last_px, last_py = self.last_player_pos
        
        move_x = px - last_px
        move_y = py - last_py
        
        if move_x == 0 and move_y == 0:
            return current_pos
        
        prediction_distance = 3
        
        predicted_x = px + move_x * prediction_distance
        predicted_y = py + move_y * prediction_distance
        
        predicted_x = max(0, min(19, predicted_x))
        predicted_y = max(0, min(19, predicted_y))
        
        if self.map[predicted_y * 20 + predicted_x] != 0:
            predicted_x = px + move_x
            predicted_y = py + move_y
            
            predicted_x = max(0, min(19, predicted_x))
            predicted_y = max(0, min(19, predicted_y))

            if self.map[predicted_y * 20 + predicted_x] != 0:
                return current_pos
        
        return (predicted_x, predicted_y)