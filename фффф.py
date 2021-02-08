import os
import sys

import pygame
import requests


pygame.init()

coord = list(map(float, input('Введите значаения широты и долготы через пробел ').split()))
spn = list(map(float, input('Введите масштаб карты: ').split()))
l = input('Введите формата карты (map, sat или sat,skl): ')


def draw(coord, spn, l):
    shir, dolg = coord
    map_request = f"http://static-maps.yandex.ru/1.x/?ll={dolg},{shir}&spn={spn[0]}" \
         f",{spn[1]}&l={l}"
    response = requests.get(map_request)

    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    # Запишем полученное изображение в файл.
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)


# Инициализируем pygame
screen = pygame.display.set_mode((600, 450))
# Рисуем картинку, загружаемую из только что созданного файла.
running = True
# Переключаем экран и ждем закрытия окна.

pygame.display.flip()
while running:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.K_UP:
                spn[0], spn[1] = spn[0] + 1, spn[1] + 1
            if event.type == pygame.K_DOWN:
                spn[0], spn[1] = spn[0] - 1, spn[1] - 1
    draw(coord, spn, l)
    screen.blit(pygame.image.load('map.png'), (0, 0))
    pygame.display.flip()

# Удаляем за собой файл с изображением.
    os.remove("map.png")