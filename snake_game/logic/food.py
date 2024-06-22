from snake_game.logic.game_object import GameObject
from snake_game.logic.constants import RED

class Food(GameObject):
    def __init__(self, snake_positions):
        super().__init__(RED, snake_positions)