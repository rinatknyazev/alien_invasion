import pygame

import sys

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Test Key")

# Главный цикл программы
while True:
    # Отслеживание событий клавиатуры и мыши
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            print(event.key)
    # Отображение последнего прорисованного экрана
    pygame.display.flip()
