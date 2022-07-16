import pygame

import Screen

FONT_SIZE = 32
FONT = pygame.font.Font('assets/font.ttf', FONT_SIZE)

class Counter:#ammo originally
    def __init__(self, text, counter, x = 0, y = Screen.HEIGHT - FONT_SIZE):
        self.text = FONT.render(text, True, Screen.BLACK, Screen.LIGHT_BLUE)
        self.rect = self.text.get_rect()
        self.rect = pygame.Rect(0,Screen.HEIGHT - self.rect.height, self.rect.width, self.rect.height)
        self.counter = counter
        self.counter_text = FONT.render(str(self.counter), True, Screen.BLACK, Screen.LIGHT_BLUE)
        self.counter_rect = self.counter_text.get_rect()
        self.counter_rect = pygame.Rect(self.rect.x + self.rect.width,
                                        self.rect.y, self.counter_rect.width,
                                        self.counter_rect.height)


    def update(self):
        self.counter_text = FONT.render(str(self.counter), True, Screen.BLACK, Screen.LIGHT_BLUE)
        self.counter_rect = self.counter_text.get_rect()
        self.counter_rect = pygame.Rect(self.rect.x + self.rect.width,
                                        self.rect.y, self.counter_rect.width,
                                        self.counter_rect.height)
    def draw(self, WINDOW):
        WINDOW.blit(self.text, self.rect)
        WINDOW.blit(self.counter_text, self.counter_rect)