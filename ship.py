import pygame

class Ship():
    """Класс для управления Кораблем"""

    def __init__(self, ai_game):
        self.screen = ai_game.screen  # Определение экрана
        self.settings = ai_game.settings  # Определение настроек
        self.screen_rect = ai_game.screen.get_rect()  # Определение прямоугльника для экрана
        self.image = pygame.image.load('images/ship.bmp')  # Загрузка изображения
        self.rect = self.image.get_rect()  # Определение прямоугольника для изображения
        self.rect.midbottom = self.screen_rect.midbottom  # Определение центра нижней границы экрана
        # Сохраненение вещественной координаты центра корабля в формате float, чтобы перемещение происходило плавнее.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        # Флаги пермещения корабля
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Обновляет позицию корабля с учетом флага."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        self.rect.x = self.x  # Определение координаты границы прямоугольника
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)  # Наложение Картинки и прямоугльника на экран screen
