import pygame
from pygame.sprite import Sprite
from random import randint, choice


class Star(Sprite):
    """Класс представляющий одну звезду"""

    def __init__(self, ai_game):
        super().__init__()  # Родительский класс
        self.screen = ai_game.screen  # Окно
        self.settings = ai_game.settings  # Настройки
        # Загрузка фото
        self.image = pygame.image.load('images/big_star.bmp').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Настройки мерцания
        # Задаем случайную начальную скорость,
        # чтобы все звезды не мигали одновременно
        self.brithness = randint(100, 255)
        self.image.set_alpha(self.brithness)
        # Случайно выбираем, увеличивается яркость сейчас или уменьшается
        self.twinkle_direction = choice([-1, 1])
        # Скорость изменения скорости ( чем больше число, тем быстрее мигает)
        self.twinkle_speed = randint(1, 3)

    def update(self):
        # ИСПРАВЛЕНО: умножаем направление на скорость (twinkle_direction * twinkle_speed)
        self.brithness += self.twinkle_direction * self.twinkle_speed

        # Если звезда дошла до пика яркости, начинаем тушить ее
        if self.brithness >= 255:
            self.brithness = 255
            self.twinkle_direction = -1
        # Если звезда стала слишком тусклой, начинаем разжигать ее
        elif self.brithness <= 80:  # Чтобы звезда не исчезла полностью
            self.brithness = 80
            self.twinkle_direction = 1

        # Применяем новую яркость к картинке звезды
        self.image.set_alpha(self.brithness)
