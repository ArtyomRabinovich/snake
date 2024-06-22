import pygame
from snake_game.logic.constants import WHITE, BLACK

class EndGame:
    def __init__(self, game):
        self.game = game
        button_width = 200
        button_height = 50
        self.buttons = [
            {'text': 'Main Menu', 'rect': pygame.Rect(self.game.WIDTH / 2 - button_width / 2, self.game.HEIGHT / 2, button_width, button_height), 'action': 'main_menu'},
            {'text': 'Retry', 'rect': pygame.Rect(self.game.WIDTH / 2 - button_width / 2, self.game.HEIGHT / 2 + 75, button_width, button_height), 'action': 'retry'},
            {'text': 'Quit', 'rect': pygame.Rect(self.game.WIDTH / 2 - button_width / 2, self.game.HEIGHT / 2 + 150, button_width, button_height), 'action': 'quit'}
        ]

    def run(self, score):
        while True:
            self.game.WINDOW.fill(WHITE)
            self.draw_text('Game Over', 64, BLACK, self.game.WIDTH / 2, self.game.HEIGHT / 4)
            self.draw_text(f'Your Score: {score}', 32, BLACK, self.game.WIDTH / 2, self.game.HEIGHT / 2 - 100)
            self.draw_text(f'High Score: {self.game.high_score}', 32, BLACK, self.game.WIDTH / 2, self.game.HEIGHT / 2 - 50)
            for button in self.buttons:
                pygame.draw.rect(self.game.WINDOW, BLACK, button['rect'])
                self.draw_text(button['text'], 32, WHITE, button['rect'].centerx, button['rect'].centery)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 'quit'
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return 'quit'
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for button in self.buttons:
                        if button['rect'].collidepoint(event.pos):
                            return button['action']

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(None, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.game.WINDOW.blit(text_surface, text_rect)
