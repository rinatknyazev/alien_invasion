import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """Класс представляющий одну звезду"""

    def __init__(self, ai_game):
        super().__init__() # Родительский класс
        self.screen = ai_game.screen # Окно
        self.settings = ai_game.settings # Настройки
        # Загрузка фото
        self.image = pygame.image.load('images/big_star.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
