import pygame
from snake_game.main import Game
from snake_game.logic.constants import SCREEN_WIDTH, SCREEN_HEIGHT

if __name__ == "__main__":
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake Game")
    game = Game(window, SCREEN_WIDTH, SCREEN_HEIGHT, 15)
    game.run()
