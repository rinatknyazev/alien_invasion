import sys
from zoneinfo import available_timezones

from random import randint
import pygame
from ship import Ship
from settings import Settings
from bullet import Bullet
from alien import Alien
from big_star import Star
from drop import Drop
from time import sleep
from game_stats import GameStats
from button import Button


class AlienInvasion:
    """Класс для управления ресурсами и поведением игры"""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.screen_rect = self.screen.get_rect()
        # Создание экземпляра для хранения игровой статистики
        self.stats = GameStats(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()
        self.drops = pygame.sprite.Group()
        self._create_fleet()
        self._create_star_sky()
        self._create_drops()
        self.play_button = Button(self, 'Play')

    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            self._check_events()
            if self.stats.game_active:
                self._update_ship()
                self._update_bullets()
                self.stars.update()
                self._update_aliens()
                self._update_drops()
            self._update_screen()

    def _check_play_button(self, mouse_pos):
        """Запускает новую игру при нажатии Play"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Сброс игровой статистики.
            self.stats.reset_stats()
            self.stats.game_active = True
            # Очистка списков пришельцев и снарядов.
            self._clean_objects()
            # Создание нового флотка и размещение корабля в центре левого края
            self._create_objects()
            # Указатель мыши скрыватся.
            pygame.mouse.set_visible(False)

    def _clean_objects(self):
        self.aliens.empty()
        self.bullets.empty()
        self.stars.empty()
        self.drops.empty()

    def _create_objects(self):
        self._create_fleet()
        self.ship.center_ship()
        self._create_star_sky()
        self._create_drops()

    def _check_events(self):
        # Отслеживание событий клавиатуры и мыши.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()  # Корректно закрывает программу
            elif event.type == pygame.KEYDOWN:  # Клавиша нажата
                print(event.key)
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                elif event.key == pygame.K_UP:
                    self.ship.moving_up = True
                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = True
                elif event.key == pygame.K_ESCAPE:
                    sys.exit()  # Корректно закрывает программу
                elif event.key == pygame.K_SPACE and self.stats.game_active:
                    self._fire_bullet()
            elif event.type == pygame.KEYUP:  # Клавиша не нажата
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
                elif event.key == pygame.K_UP:
                    self.ship.moving_up = False
                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _fire_bullet(self):
        """Создание нового снаряда и выключение в группу bullets"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_ship(self):
        self.ship.update()

    def _update_bullets(self):
        """Обновляет позиции снарядов и уничтожает старые снаряды"""
        # Обновление позиции снарядов.
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.right >= self.screen_rect.right:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Обработка коллизий снарядов с пришельцами"""
        # Удаление снарядов и пришельцев, участвующих в коллизиях.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        if not self.aliens:
            # Уничтожение существующих снарядов и создание нового флота
            self.bullets.empty()
            self._create_fleet()

    def _create_fleet(self):
        """рассчитывает ширину, свободное место и запускает цикл."""
        alien_test = Alien(self)  # Создание ТЕСТОВОГО экземпляра
        alien_width, alien_height = alien_test.rect.size  # Ширина пришельца
        available_space_x = self.screen_rect.width - self.ship.rect.width - 3 * alien_width  # Вычисление доступного расстояния
        number_aliens_x = available_space_x // (2 * alien_width)  # Кол-во пришельцев
        """Определяет количество рядов, помещающися на экране"""
        ship_width = self.ship.rect.width  # Ширина корабля
        # Свободное пространство (кол-во пикселей)
        availabe_space_y = self.screen_rect.height - alien_height
        # Количество рядов
        number_rows = availabe_space_y // (2 * alien_height)
        # Создание флота вторжения.
        for row_number in range(number_rows):  # Перебираем список пришельцев(кол-во)
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """только за создание одного пришельца и добавление его в группу"""
        alien = Alien(self)  # Создание боевого пришельца
        alien_width, alien_height = alien.rect.size  # узнаем его габариты
        # Расставляем пришельцев справа - налево с шагом в две ширины
        alien.rect.right = self.screen_rect.right - 2 * alien_width * alien_number
        alien.rect.y = alien_height + 2 * alien_height * row_number

        alien.y = float(alien.rect.y)
        self.aliens.add(alien)

    def _create_drops(self):
        """Запускает цикл"""
        drop = Drop(self)  # Создание тестовой капли чтобы узнать е размеры
        drop_width, drop_height = drop.rect.size
        next_drop_y = drop_height + (randint(1, 50))
        while next_drop_y + drop_height <= self.screen_rect.bottom:
            drop = Drop(self)
            drop.rect.y = next_drop_y
            self.drops.add(drop)
            next_drop_y += drop_height + (randint(1, 50))

    def _update_drops(self):
        self.drops.update()
        for drop in self.drops:
            if drop.rect.right <= self.screen_rect.left:
                drop.rect.left = self.screen_rect.right
                drop.x = float(drop.rect.x)
                drop.speed = randint(1, 2)

    def _update_aliens(self):
        """Обновляет позиции всех пришельцев во флоте"""
        self._check_fleet_edges()
        self.aliens.update()
        # Проверка коллизий "Пришелец – корабль".
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        # Проверка условия дорались ли пришельцы до левого края экрна
        self._check_aliens_left()

    def _check_fleet_edges(self):
        """Реагирует на достижение пришельцем края экрана"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Опускает весь флот и меняте направление флота."""
        for alien in self.aliens.sprites():
            alien.rect.x -= self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_aliens_left(self):
        """Проверяет добрались ли пришельцы до левого края экрана"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if screen_rect.left >= alien.rect.left:
                # Происходит то же, что при столкновении с кораблем.
                self._ship_hit()
                break

    def _ship_hit(self):
        """Обрабатывает столкновение корабля с пришельцем."""
        if self.stats.ships_left > 0:
            # Уменьшение ships_left.
            self.stats.ships_left -= 1

            # Очистка списков пришельцев и снарядов.
            self.aliens.empty()
            self.bullets.empty()

            # Создание нового флота и размещение корабля в центре.
            self._create_fleet()
            self.ship.center_ship()

            # Пауза
            sleep(1)
        else:
            self.stats.game_active = False

    def _create_star_sky(self):
        star_test = Star(self)  # Тестовая звезд, чтобы узнать размеры.
        star_width, star_height = star_test.rect.size  # Габариты звезды
        # X - это ширина, Y - высота
        available_space_x = self.settings.screen_width
        available_space_y = self.settings.screen_height
        # Считаем сколько звезд поместится
        number_star_x = available_space_x // (2 * star_width)
        row_number = available_space_y // (2 * star_height)
        # Запускаем вложенные циклы
        for row in range(row_number):
            for number in range(number_star_x):
                self._create_star(number, row)

    def _create_star(self, star_number, row_number):
        star = Star(self)  # Создаем боевую звезду
        star_width, star_height = star.rect.size  # Узнаем габариты
        random_number = randint(-10, 10)
        # Генерируем случайное смещение для эффекта хаотичности
        random_x = randint(-10, 10)
        random_y = randint(-10, 10)
        star.rect.x = star_width + (2 * star_width * star_number) + random_x
        star.rect.y = star_height + 2 * star_height * row_number + random_y
        self.stars.add(star)

    def _update_screen(self):
        # При каждом проходе цикла перерисовывается экран.
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)
        for drop in self.drops:
            drop.draw_trasser()
        self.drops.draw(self.screen)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        # Кнопка Play отображается в том случае, если игра неактивна
        if not self.stats.game_active:
            self.play_button.draw_button()
        # Отображение последнего прорисованного экрана.
        pygame.display.flip()


if __name__ == '__main__':
    # Создание экземпляра и запуск игры.
    ai = AlienInvasion()
    ai.run_game()
