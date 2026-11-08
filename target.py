import pygame

class Target():
    def __init__(self,ai_game):
        self.screen = ai_game.screen # Определение экрана
        self.settings = ai_game.settings # Определение настроек
        self.screen_rect = self.screen.get_rect() # Определение рамки экрана
        self.color = self.settings.target_color # Определение цвета
        # Определение размеров платформы
        self.rect = pygame.Rect(0,0,self.settings.target_width,
                                self.settings.target_height)

    def center_target(self):
        """Создает платформу"""
        x, y = self.screen_rect.midright  # (x:1000,y:700)
        self.rect.midright = (x - self.rect.width, y)  # Передаем конкретную координату
        # Сохранение начальной координаты для движения по оси y
        self.y = float(self.rect.y)

    def update(self):
        """Обновляет позицию корабля с учетов флага: target_direction"""
        self.y += self.settings.target_speed * self.settings.target_direction
        self.rect.y = int(self.y)

    def check_edges(self):
        """Возвращает True, если платформа находится у крев экрана"""
        screen_rect = self.screen.get_rect()
        if screen_rect.top >= self.rect.top or self.rect.bottom >= screen_rect.bottom:
            return True



