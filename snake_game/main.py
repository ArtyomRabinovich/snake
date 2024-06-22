import pygame
from snake_game.ui.menu import Menu
from snake_game.logic.game_logic import GameLogic
from snake_game.ui.end_game import EndGame
from snake_game.ui.pause_menu import PauseMenu
from snake_game.logic.constants import HIGH_SCORE_FILE, SCREEN_WIDTH, SCREEN_HEIGHT, BORDER_HEIGHT

class Game:
    def __init__(self, window, width, height, difficulty):
        self.WINDOW = window
        self.WIDTH = width
        self.HEIGHT = height
        self.difficulty = difficulty
        self.game_started = False

        pygame.init()
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.running = True

        self.menu = Menu(self)
        self.game_ui = GameLogic(self)
        self.end_game = EndGame(self)
        self.pause_menu = PauseMenu(self)

        self.high_score = self.load_high_score()
        self.snake_move_delay = 200
        self.last_snake_move_time = pygame.time.get_ticks()
        self.current_score = 0

    def run(self):
        while self.running:
            self.run_menu()
            if self.running:
                game_result = self.run_game()
                if game_result == "game_over":
                    self.run_end_game()
            self.clock.tick(60)

    def run_menu(self):
        while self.running:
            action = self.menu.run()
            if action == "start_game":
                self.game_started = True
                break
            elif action == "continue_game":
                break
            elif action == "quit":
                self.running = False

    def run_game(self):
        self.game_ui.reset()
        paused = False
        while self.running:
            if paused:
                action = self.pause_menu.run()
                if action == "resume":
                    paused = False
                elif action == "end_game":
                    return "game_over"
                elif action == "quit":
                    self.running = False
                    return
            else:
                current_time = pygame.time.get_ticks()
                if current_time - self.last_snake_move_time > self.snake_move_delay:
                    self.game_ui.update()
                    self.last_snake_move_time = current_time
                self.game_ui.draw(self.WINDOW)
                action = self.game_ui.handle_events()
                if action == "pause":
                    paused = True
                elif action == "quit":
                    self.running = False
                    return
                pygame.display.update()

                if self.game_ui.check_game_over():
                    if self.current_score > self.high_score:
                        self.high_score = self.current_score
                        self.save_high_score()
                    return "game_over"

            self.clock.tick(60)

    def run_end_game(self):
        while self.running:
            action = self.end_game.run(self.current_score)
            if action == "main_menu":
                self.reset_game_state()
                return
            elif action == "retry":
                self.reset_game_state()
                game_result = self.run_game()
                if game_result == "game_over":
                    self.run_end_game()
                return
            elif action == "quit":
                self.running = False

    def set_speed(self, speed):
        self.snake_move_delay = speed

    def load_high_score(self):
        try:
            with open(HIGH_SCORE_FILE, 'r') as file:
                return int(file.read().strip())
        except (FileNotFoundError, ValueError):
            return 0

    def save_high_score(self):
        with open(HIGH_SCORE_FILE, 'w') as file:
            file.write(str(self.high_score))

    def reset_game_state(self):
        self.current_score = 0
        self.game_ui.reset()
        self.last_snake_move_time = pygame.time.get_ticks()
        self.snake_move_delay = 200

    def quit(self):
        self.running = False
        pygame.quit()
