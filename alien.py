import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Класс, предстваляющий одного пришельца."""

    def __init__(self, cosmogame):
        """Инициализирует пришельца и задает его начальную позицию."""
        super().__init__()
        self.screen = cosmogame.screen
        self.settings = cosmogame.settings

        # Загрузка изображения пришельца и назначения атрибута rect.
        self.image = pygame.image.load('images/alien.bmp')
        self.image = pygame.transform.rotate(self.image,-90)
        self.rect = self.image.get_rect()

        # Каждый новый пришелец появляется в левом верхнем углу экрана.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Сохранение точной горизонтальной позиции пришельца.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_edges(self):
        """Возвращает True, если пришелец находится у крев экрана"""
        screen_rect = self.screen.get_rect()
        if screen_rect.top >= self.rect.top or self.rect.bottom >= screen_rect.bottom:
            return True

    def update(self):
        """"Перемещает пришельца влево"""
        self.y += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.y = self.y
