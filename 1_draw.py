import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 500))


#rect(screen, (255, 0, 255), (100, 100, 200, 200))
#rect(screen, (0, 0, 255), (100, 100, 200, 200), 5)
#polygon(screen, (255, 255, 0), [(100,100), (200,50),
#                                (300,100), (100,100)])
#polygon(screen, (0, 0, 255), [(100,100), (200,50),
#                              (300,100), (100,100)], 5)
#circle(screen, (0, 255, 0), (200, 175), 50)
#circle(screen, (255, 255, 255), (200, 175), 50, 5)

rect(screen, (127, 127, 127), (0, 0, 500, 500))


circle(screen, (255,255,0), (250, 250), 150)
circle(screen, (0,0,0), (250, 250), 150, 3)

circle(screen, (255,0,0), (180, 210), 30)
circle(screen, (0,0,0), (180, 210), 30, 3)
circle(screen, (0,0,0), (180,210), 15)


circle(screen, (255,0,0), (300, 200), 40)
circle(screen, (0,0,0), (300, 200), 40,3)
circle(screen, (0,0,0), (300,200), 15)
rect(screen, (0,0,0), (170, 320, 160, 25))

polygon(screen, (0,0,0), [(220, 210), (230,200), (130, 130), (120,140)])
polygon(screen, (0,0,0), [(250, 170), (260,180), (390, 130), (380,120)])


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
