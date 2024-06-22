import random
import pygame
from snake_game.logic.constants import SCREEN_WIDTH, SCREEN_HEIGHT, SNAKE_SIZE, BORDER_HEIGHT

class GameObject:
    def __init__(self, color, snake_positions):
        self.color = color
        self.position = self.random_position(snake_positions)

    def random_position(self, snake_positions):
        while True:
            pos = (random.randint(0, (SCREEN_WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE,
                   random.randint((BORDER_HEIGHT + SNAKE_SIZE) // SNAKE_SIZE, (SCREEN_HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE)
            if pos not in snake_positions:
                return pos

    def draw(self, surface):
        rect = pygame.Rect(self.position[0], self.position[1], SNAKE_SIZE, SNAKE_SIZE)
        pygame.draw.rect(surface, self.color, rect)
