class Settings():
    """Класс для сохранения всех настроек игры Alies Invasion"""

    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 1000
        self.screen_height = 500
        self.bg_color = (0, 0, 0)
        self.bullets_allowed = 10
        # Настройки корабля
        self.ship_speed = 1
        # Параметры снаряда
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
