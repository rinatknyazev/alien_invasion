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
        self.rect = self.image.get_rect()

        # Каждый новый пришелец появляется в левом верхнем углу экрана.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Сохранение точной горизонтальной позиции пришельца.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Возвращает True, если пришелец гаходится у крев экрана"""
        screen_rect = self.screen.get_rect()
        if screen_rect.left >= self.rect.left or self.rect.right >= screen_rect.right:
            return True

    def update(self):
        """"Перемещает пришельца вправо"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
