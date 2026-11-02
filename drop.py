import pygame
from pygame.sprite import Sprite



class Drop(Sprite):
    """Класс, представляющий одну каплю"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Загрузка капли с прозрачностью и назначения аттрибута rect
        self.image = pygame.image.load('images/drop.png').convert_alpha()
        self.image = pygame.transform.smoothscale(self.image,(20,50))
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        # Появление капли на расстоянии ширины капли от края экрана∆
        self.rect.x = 0
        self.rect.bottom = self.screen_rect.top

        # Сохранение точной вертикальной позиции капли
        self.y = float(self.rect.y)

    def update(self):
        self.y += self.settings.drop_speed
        self.rect.y = self.y
