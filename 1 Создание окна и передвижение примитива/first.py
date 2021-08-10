# Начало изучения PyGame:

# В данном проекте мы создали окно размером 500 на 500.
# В это окно мы поместили прямоугольник, и дали ему функцию передвижения
# по 4 осям (вверх, вниз, влево, вправо). Имеются границы раб. поля.

import pygame as pg
pg.init() 

win = pg.display.set_mode((500, 500))
win.fill((255,255,255)) # Устанавливаем цвет заднего фона по RGB
pg.display.set_caption("Hello World!") # Имя окна

clock = pg.time.Clock()

x, y = 225, 175 # Положение персонажа по двум координатам
speed = 5

while True:
    #Функция прерывания программы при нажатии на выход (крестик):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    # Отслеживание нажатия кнопок, и перемещение персонажа:
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and x > 10:
        x -= speed
    if keys[pg.K_RIGHT] and x < 440:
        x += speed
    if keys[pg.K_UP] and y > 10:
        y -= speed
    if keys[pg.K_DOWN] and y < 390:
        y += speed


    # Изменяем положение персонажа:
    win.fill((255,255,255))
    pg.draw.rect(win, (0, 0, 0), (x, y, 50, 100), 10)
    pg.display.update()

    clock.tick(60) # Фиксируем частоту обновления окна

pg.quit() 