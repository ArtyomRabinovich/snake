import pygame
from snake_game.logic.constants import GREEN, SNAKE_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, BORDER_HEIGHT

class Snake:
    def __init__(self):
        self.size = SNAKE_SIZE
        self.color = GREEN
        self.positions = [((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2))]
        self.direction = pygame.K_RIGHT
        self.grow = False

    def get_head_position(self):
        return self.positions[0]

    def turn(self, direction):
        if (direction == pygame.K_UP and self.direction != pygame.K_DOWN) or \
           (direction == pygame.K_DOWN and self.direction != pygame.K_UP) or \
           (direction == pygame.K_LEFT and self.direction != pygame.K_RIGHT) or \
           (direction == pygame.K_RIGHT and self.direction != pygame.K_LEFT):
            self.direction = direction

    def move(self):
        head_x, head_y = self.get_head_position()
        if self.direction == pygame.K_UP:
            head_y -= self.size
        elif self.direction == pygame.K_DOWN:
            head_y += self.size
        elif self.direction == pygame.K_LEFT:
            head_x -= self.size
        elif self.direction == pygame.K_RIGHT:
            head_x += self.size

        # Ensure the snake wraps around the screen edges correctly
        if head_y < BORDER_HEIGHT:  # When the snake moves beyond the top border
            head_y = SCREEN_HEIGHT - self.size
        elif head_y >= SCREEN_HEIGHT:  # When the snake moves beyond the bottom border
            head_y = BORDER_HEIGHT +2  # Move to just inside the top border

        if head_x < 0:  # When the snake moves beyond the left border
            head_x = SCREEN_WIDTH - self.size
        elif head_x >= SCREEN_WIDTH:  # When the snake moves beyond the right border
            head_x = 0

        new_head = (head_x, head_y)

        if not self.grow:
            self.positions.pop()  # Remove the tail
        else:
            self.grow = False  # Reset grow flag after growing

        self.positions.insert(0, new_head)  # Add the new head position


    def grow_snake(self):
        self.grow = True

    def draw(self, surface):
        for pos in self.positions:
            rect = pygame.Rect(pos[0], pos[1], self.size, self.size)
            pygame.draw.rect(surface, self.color, rect)
