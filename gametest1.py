import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 30
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
WHITE = (255, 255, 255)

COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, GRAY, WHITE]
score = 0 #счёт
kol = 6 #количество шариков


def new_balls():
    '''Создаёт kol шариков,рисует шарики в момент старта программы'''
    global x, y, r, v_x, v_y, color, time, type
    x = []
    y = []
    r = []
    v_x = []
    v_y = []
    color = []
    time = []  # время жизни шарика
    type = []  # тип шарика
    '''Генерируем шарики:'''
    for i in range(kol):
        x.append(randint(100, 1100))
        y.append(randint(100, 800))
        r.append(randint(20, 100))
        v_x.append(randint(-10, 10))
        v_y.append(randint(-10, 10))
        color.append(COLORS[randint(0, 7)])
        time.append(0)
        type.append(randint(0, 10))
    for j in range(kol):
        circle(screen, color[j], (x[j], y[j]), r[j])


def new_ball(j):
    '''Рисует новый шарик вместо старого, если в старый попали'''
    x[j] = randint(100, 1100)
    y[j] = randint(100, 800)
    r[j] = randint(20, 100)
    v_x[j] = randint(-10, 10)
    v_y[j] = randint(-10, 10)
    time[j] = 0
    color[j] = COLORS[randint(0, 7)]
    type[j] = randint(0, 10)
    circle(screen, color[j], (x[j], y[j]), r[j])


def click(xpos , ypos, j):
    '''Проверяет, попал ли клик на шарик с учётом позиции шарика в данный момент времени'''
    if (xpos-x[j])**2 + (ypos-y[j])**2 <= r[j]**2:
        return True


def update_position(time):
    '''Реализует движение шариков как функцию от времени, проверяет, легендарный ли шарик'''
    screen.fill(BLACK)
    for j in range(kol):
        if (x[j]-r[j] <= 0) | (x[j]+r[j] >= 1200):
            v_x[j] = -v_x[j]
        if (y[j]-r[j] <= 0) | (y[j]+r[j] >= 900):
            v_y[j] = -v_y[j]
        x[j] += v_x[j]
        y[j] += v_y[j]
        circle(screen, color[j], (x[j], y[j]), r[j])
        for j in range(kol):
            time[j] += 1
            if (type[j] > 8) & (time[j] % 2 == 0):
                color[j] = COLORS[randint(0, 7)]


def score_counter(j):
    '''Считает очки с учётом типа шарика'''
    global score
    if type[j] > 8:
        score += 2
        print("Вы поймали легендарный шарик! Счёт: ", score)
    else:
        score += 1
        print("Вы поймали шарик! Счёт: ", score)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

new_balls()

while not finished:
    clock.tick(FPS)
    update_position(time)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for j in range(kol):
                if(click(event.pos[0], event.pos[1], j)):
                    score_counter(j)
                    new_ball(j)
    pygame.display.update()


pygame.quit()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
