
class Level:

    def __init__(self, coins, ennemies, entry, exit, length, width):
        self.coins = coins
        self.ennemies = ennemies
        self.entry = entry
        self.exit = exit
        self._length = length
        self._width = width