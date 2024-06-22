from snake_game.logic.game_object import GameObject
from snake_game.logic.constants import BLACK

class Obstacle(GameObject):
    def __init__(self, snake_positions):
        super().__init__(BLACK, snake_positions)