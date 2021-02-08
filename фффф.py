import os
import sys

import pygame
import requests

shir, dolg = float(input('Введите широту: ')), float(input('Введите долготу: '))
spn = list(map(float, input('Введите масштаб карты: ').split()))
l = input('Введите формата карты (map, sat или sat,skl): ')
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
pygame.init()
screen = pygame.display.set_mode((600, 450))
# Рисуем картинку, загружаемую из только что созданного файла.
screen.blit(pygame.image.load(map_file), (0, 0))
# Переключаем экран и ждем закрытия окна.
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()

# Удаляем за собой файл с изображением.
os.remove(map_file)