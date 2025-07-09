import json
import os

class Best_times:
    """saves the best times of each level"""
    def __init__(self, levels):
        self.levels = levels
        self.best_times_file = "best_times.json"
        self.best_times = self.load_best_times()
    
    def load_best_times(self):
        if os.path.exists(self.best_times_file):
            try:
                with open(self.best_times_file, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                return self.create_default_highscores()
        else:
            return self.create_default_highscores()
    
    def create_default_highscores(self):
        default_scores = {}
        for i in range(len(self.levels)):
            default_scores[f"level_{i}"] = None
        
        with open(self.best_times_file, 'w') as f:
            json.dump(default_scores, f)
        
        return default_scores
    
    def save_best_times(self):
        with open(self.best_times_file, 'w') as f:
            json.dump(self.best_times, f)
    
    def update_score(self, level_index, time):
        level_key = f"level_{level_index}"
        
        if level_key not in self.best_times:
            self.best_times[level_key] = None
        
        score_updated = False
        
        if self.best_times[level_key] is None or time < self.best_times[level_key]:
            self.best_times[level_key] = time
            score_updated = True
        
        if score_updated:
            self.save_best_times()
        
        return score_updated
    
    def get_best_time(self, level_index):
        level_key = f"level_{level_index}"
        if level_key in self.best_times:
            return self.best_times[level_key]
        return None
    
    def reset(self):
        self.best_times = self.create_default_highscores()