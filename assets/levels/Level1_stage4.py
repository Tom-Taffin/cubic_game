from assets.Area import Area
from assets.Coin import Coin
from assets.Entity import Entity
from assets.Labyrinth import Labyrinth
from assets.Player import Player
from assets.Timer import Timer
from assets.ennemies.Ennemy_astar import Ennemy_astar
from assets.levels.Level_labyrinth import Level_labyrinth


class Level1_stage4(Level_labyrinth):

    def __init__(self, width:int, height:int, player:Player):
    
        map = generate_labyrinth(20,20)
        map = [
            1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
            1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
            1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,0,1,
            1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,
            1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,
            1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,
            1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,
            1,0,0,0,0,1,0,0,0,0,0,0,0,1,1,1,1,1,0,1,
            1,1,1,1,0,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,
            1,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,1,
            1,0,1,1,1,1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,
            1,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,1,
            1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,0,1,
            1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,
            1,0,1,0,1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,
            1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,
            1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,
            1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,
            1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
            1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0
        ]

        ennemies = [Ennemy_astar(width//2, height//2,40,player,map)]
        super().__init__(ennemies, width, height, player, map)
    




import random

def generate_labyrinth(width=20, height=20, extra_paths=30):
    """
    Génère un labyrinthe avec plusieurs chemins.
    - width, height : dimensions
    - extra_paths : nombre de murs à casser pour créer des chemins annexes
    Retourne une liste [0,1] linéaire :
    - 0 = vide
    - 1 = mur
    Entrée en (1,1)
    Sortie en (width-2, height-2)
    """

    # Initialisation en murs
    grid = [[1 for _ in range(width)] for _ in range(height)]
    directions = [(0,-1),(0,1),(1,0),(-1,0)]

    def in_bounds(x, y):
        return 0 <= x < width and 0 <= y < height

    def neighbors(x, y):
        for dx, dy in directions:
            nx, ny = x + dx*2, y + dy*2
            if in_bounds(nx, ny) and grid[ny][nx] == 1:
                yield (nx, ny, dx, dy)

    def carve(x, y):
        grid[y][x] = 0
        neighs = list(neighbors(x,y))
        random.shuffle(neighs)
        for nx, ny, dx, dy in neighs:
            if grid[ny][nx] == 1:
                grid[y+dy][x+dx] = 0
                carve(nx, ny)

    # Génération DFS principale
    carve(1,1)

    # Création de chemins annexes aléatoires
    for _ in range(extra_paths):
        x = random.randrange(1, width-1)
        y = random.randrange(1, height-1)
        if grid[y][x] == 1:
            # On ne touche pas l'entrée/sortie
            if (x, y) not in [(1,1),(width-2,height-2)]:
                grid[y][x] = 0

    # Fixe entrée et sortie
    grid[1][1] = 0
    grid[height-2][width-2] = 0

    # Conversion en liste linéaire
    flat_map = [grid[y][x] for y in range(height) for x in range(width)]
    return flat_map
