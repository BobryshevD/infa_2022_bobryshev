import pygame
from pygame.draw import *
import math
from random import randint
pygame.init()

FPS = 2
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
score = 0



def new_ball():
    '''рисует новый шарик '''
    global x, y, r
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(20, 80)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)

def check(a,b):
    global score
    '''check of getting and print score if match'''
    if (x-a)**2 + (y-b)**2 <= r**2:
        score = score + 1
        print("Match! Your score:", score)


new_ball()

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            check(event.pos[0], event.pos[1])

screen.fill(BLACK)
new_ball()
pygame.display.update()
pygame.quit()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
