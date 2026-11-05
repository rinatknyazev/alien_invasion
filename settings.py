from random import randint


class Settings():
    """Класс для сохранения всех настроек игры Alies Invasion"""

    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 1000
        self.screen_height = 700
        self.bg_color = (0, 0, 0)
        # Настройки корабля
        self.ship_speed = 1
        # Настройки пришельцев
        self.alien_speed = 0.2 # Скорость пришельца
        self.fleet_drop_speed = 10 # Снижение флота при достижении им края
        self.fleet_direction = 1
        self.drop_speed = 0.5
        self.drop_trasser_width = 2
        self.drop_trasser_height= 5
        self.drop_trasser_color = (150,150,150)
        # Параметры снаряда
        self.bullets_allowed = 3
        self.bullet_speed = 1
        self.bullet_width = 15
        self.bullet_height = 300
        self.bullet_color = (255, 255, 255)
