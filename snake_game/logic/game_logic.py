import pygame
import random
from snake_game.logic.snake import Snake
from snake_game.logic.food import Food
from snake_game.logic.obstacle import Obstacle
from snake_game.logic.constants import WHITE, BLACK, SCREEN_WIDTH, SCREEN_HEIGHT, BORDER_HEIGHT

class GameLogic:
    def __init__(self, game):
        self.game = game
        self.snake = Snake()
        self.food = Food(self.snake.positions)
        self.obstacles = []
        self.score = 0
        self.generate_obstacle()

    def generate_obstacle(self):
        while True:
            new_obstacle = Obstacle(self.snake.positions + [self.food.position])
            if new_obstacle.position not in self.snake.positions and \
               new_obstacle.position != self.food.position and \
               all(ob.position != new_obstacle.position for ob in self.obstacles):
                self.obstacles.append(new_obstacle)
                break

    def update(self):
        self.snake.move()
        if self.snake.get_head_position() == self.food.position:
            self.snake.grow_snake()
            self.food = Food(self.snake.positions + [ob.position for ob in self.obstacles])
            self.score += 1
            self.game.current_score = self.score
            if self.score % 10 == 0:
                self.generate_obstacle()
        for obstacle in self.obstacles:
            if self.snake.get_head_position() == obstacle.position:
                return "game_over"

    def draw(self, surface):
        surface.fill(WHITE)
        self.draw_border(surface)
        self.snake.draw(surface)
        self.food.draw(surface)
        for obstacle in self.obstacles:
            obstacle.draw(surface)
        self.draw_score(surface)
        self.draw_pause_instruction(surface)

    def draw_border(self, surface):
        pygame.draw.line(surface, BLACK, (0, BORDER_HEIGHT), (SCREEN_WIDTH, BORDER_HEIGHT), 2)

    def draw_score(self, surface):
        font = pygame.font.Font(None, 36)
        text = font.render(f'Score: {self.score}', True, BLACK)
        surface.blit(text, (5, 5))

    def draw_pause_instruction(self, surface):
        font = pygame.font.Font(None, 24)
        text = font.render('Press P to Pause', True, BLACK)
        surface.blit(text, (self.game.WIDTH - 150, 10))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "quit"
                elif event.key == pygame.K_p:  # Press 'P' to pause
                    return "pause"
                elif event.key == pygame.K_UP:
                    self.snake.turn(pygame.K_UP)
                elif event.key == pygame.K_DOWN:
                    self.snake.turn(pygame.K_DOWN)
                elif event.key == pygame.K_LEFT:
                    self.snake.turn(pygame.K_LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.snake.turn(pygame.K_RIGHT)
        return None

    def reset(self):
        self.snake = Snake()
        self.food = Food(self.snake.positions)
        self.obstacles = []
        self.score = 0
        self.generate_obstacle()

    def check_game_over(self):
        if self.snake.get_head_position() in self.snake.positions[1:]:
            return True
        for obstacle in self.obstacles:
            if self.snake.get_head_position() == obstacle.position:
                return True
        return False
