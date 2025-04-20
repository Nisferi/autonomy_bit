# ui.py

import pygame

CELL = 5
BAR = 50  # высота панели с кнопками

BUTTON_FONT_SIZE = 20
BUTTON_PADDING = 10
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 30

class Button:
    def __init__(self, rect, text, action):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.action = action
        self.font = pygame.font.SysFont(None, BUTTON_FONT_SIZE)
        self.text_surf = self.font.render(text, True, (255,255,255))
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)

    def draw(self, surface):
        pygame.draw.rect(surface, (50,50,50), self.rect)
        pygame.draw.rect(surface, (200,200,200), self.rect, 2)
        surface.blit(self.text_surf, self.text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

class UI:
    def __init__(self, grid):
        pygame.init()
        self.grid = grid
        size = grid.size * CELL
        self.screen = pygame.display.set_mode((size, size + BAR))
        pygame.display.set_caption("Autonomy Bit")
        self.clock = pygame.time.Clock()
        self.running = True

        # Define buttons
        self.buttons = []
        labels_actions = [
            ("Старт", "start"),
            ("Медленнее", "slower"),
            ("Быстрее", "faster"),
            ("Пауза", "pause"),
            ("Сохранить", "save"),
            ("Выход", "exit")
        ]
        for i, (label, action) in enumerate(labels_actions):
            x = i * (BUTTON_WIDTH + BUTTON_PADDING) + BUTTON_PADDING
            y = grid.size * CELL + (BAR - BUTTON_HEIGHT) // 2
            self.buttons.append(Button((x, y, BUTTON_WIDTH, BUTTON_HEIGHT), label, action))

    def poll(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.running = False
                return 'exit'
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                for btn in self.buttons:
                    if btn.is_clicked(e.pos):
                        if btn.action == 'start':
                            self.grid.paused = False
                        elif btn.action == 'pause':
                            self.grid.paused = True
                        return btn.action
        return None

    def render(self):
        # рисуем частицы
        self.screen.fill((0,0,0))
        for p in self.grid.cells.values():
            x, y = map(int, p['pos'])
            color = (255,255,255)
            pygame.draw.circle(self.screen, color, (x*CELL, y*CELL), CELL//2)
        # рисуем панель
        panel_rect = pygame.Rect(0, self.grid.size*CELL, self.grid.size*CELL, BAR)
        pygame.draw.rect(self.screen, (30,30,30), panel_rect)
        # рисуем кнопки
        for btn in self.buttons:
            btn.draw(self.screen)
        pygame.display.flip()
        self.clock.tick(60)

    def cleanup(self):
        pygame.quit()
