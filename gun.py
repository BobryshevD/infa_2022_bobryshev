import math
from random import choice
from random import randint
import pygame

FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
score = 0

WIDTH = 800
HEIGHT = 600


class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if (self.x+self.r < 800) & (self.x - self.r > 0):
            self.x += self.vx
        else:
            self.vx = -self.vx
            self.x += self.vx
        if (self.y+self.r) < 500:
            self.vy -= 1
            self.y -= self.vy
        else:
            self.vy = -self.vy/1.1
            self.y -= self.vy
            self.vx = self.vx/1.1
        if self.vx**2 + self.vy**2 < 0.001:
            self.live -= 1


    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (obj.x-self.x)**2 + (obj.y-self.y)**2 <= (obj.r+self.r)**2:
            return True
        else:
            return False


def balls_live_test(balls):
    """Удаляет шарики, у которых self.live = 0"""
    global b
    for b in balls:
        b.draw()
        if b.live == 0:
            balls.remove(b)


class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            if event.pos[0] != 20:
                self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
            else:
                self.an = math.atan((event.pos[1]-450) / (event.pos[0]-21))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        pygame.draw.line(self.screen, self.color, (40,450), (40+5*self.f2_power*math.cos(self.an), 450+5*self.f2_power*math.sin(self.an)), 25)


    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target:
    def __init__(self):
        self.points = 0
        self.live = 1
        self.x = 0
        self.y = 0
        self.r = 0
        self.vx = 0
        self.vy = 0
        self.color = RED
        self.time = 0
        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = randint(550, 745)
        y = self.y = randint(200, 400)
        r = self.r = randint(5, 50)
        vx = self.vx = randint(-5, 5)
        vy = self.vy = randint(-5, 5)
        self.live = 1
        self.time = 0
        color = self.color = RED

    def hit(self):
        """Попадание шарика в цель."""
        global score
        score += 1
        print("Попадание! Очки:", score)

    def score_draw(self):
        """Выводит счёт на экран"""
        global bullet, b
        for b in balls:
            if b.hittest(self) and self.live:
                self.time += 1
                self.live = 0
                self.hit()
            if (self.time > 0) and (self.time < 120):
                text = font.render(f'Попадание за {bullet} попыток', True, BLACK)
                screen.blit(text, (200, 250))
                self.time += 1
            if self.time == 120:
                self.time = 0
                self.new_target()
                bullet = 0

    def draw(self):
        """Рисует цель"""
        if self.live != 0:
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)
            if (self.x+self.r > 800) or (self.x-self.r < 400):
                self.vx = -self.vx
            if (self.y+self.r > 550) or (self.y-self.r < 0):
                self.vy = -self.vy
            self.x += self.vx
            self.y += self.vy


def spawn_targets():
    """Создаёт цели"""
    target1 = Target()
    targets.append(target1)
    target2 = Target()
    targets.append(target2)


def draw_targets(targets):
    """"Рисует цели, проверяет на попадание"""
    for target in targets:
        target.draw()
    for target in targets:
        target.score_draw()


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont('arial', 50)
bullet = 0
balls = []
targets = []


clock = pygame.time.Clock()
gun = Gun(screen)
spawn_targets()
#target = Target()
finished = False

while not finished:
    screen.fill(WHITE)
    gun.draw()
    draw_targets(targets)
    balls_live_test(balls)
    pygame.display.update()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    for b in balls:
        b.move()
    gun.power_up()

pygame.quit()
