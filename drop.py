import pygame
from pygame.sprite import Sprite
from random import randint



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
        self.color = self.settings.drop_trasser_color
        self.rect_trasser = pygame.Rect(0,0,self.settings.drop_trasser_width,
                                        self.settings.drop_trasser_height)
        self.rect_trasser.midbottom = self.rect.midtop
        # Появление капли на расстоянии ширины капли от края экрана∆
        self.rect.x = 0
        self.rect.bottom = self.screen_rect.top - randint(0,1000)

        # Сохранение точной вертикальной позиции капли
        self.y = float(self.rect.y)
        self.speed = self.settings.drop_speed
    def update(self):
        self.y += self.speed
        self.rect.y = self.y
    def draw_trasser(self):
        self.rect_trasser.midbottom = self.rect.midtop
        pygame.draw.rect(self.screen,self.color,self.rect_trasser)
