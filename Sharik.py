
import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 200
screen = pygame.display.set_mode((1200, 900))

Yellow = (255, 255, 255)
BLACK = (99, 88, 66)
x = randint(100, 700)
y = randint(100, 700)
r = randint(10, 70)
x1 = randint(100, 700)
y1 = randint(100, 700)
r1 = randint(10, 70)
x2 = randint(100, 700)
y2 = randint(100, 700)
r2 = randint(10, 70)
dx = randint(-3, 3)
dx1 = randint(-3, 3)
dx2 = randint(-3, 3)
dy = randint(-3, 3)
dy1 = randint(-3, 3)
dy2 = randint(-3, 3)

def click(event):
    print(x, y, r)

def dvig(event):
    global dx, dy
    circle(screen, Yellow, (x, y), r)
    if x >= 1150 or x < 50:
        dx *= -1
    if y >= 850 or y < 50:
        dy *= -1
    return circle(screen, Yellow, (x, y), r)

def dvig1(event):
    global dx1, dy1
    circle(screen, Yellow, (x1, y1), r1)
    if x1 >= 1150 or x1 < 50:
        dx1 *= -1
    if y1 >= 850 or y1 < 50:
        dy1 *= -1
    return circle(screen, Yellow, (x1, y1), r1)

def dvig2(event):
    global dx2, dy2
    circle(screen, Yellow, (x2, y2), r2)
    if x2 >= 1150 or x2 < 50:
        dx2 *= -1
    if y2 >= 850 or y2 < 50:
        dy2 *= -1
    return circle(screen, Yellow, (x2, y2), r2)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
A = []
n = 0

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            A = pygame.mouse.get_pos()
            xx = A[0]
            yy = A[1]
            if ((xx-x)**2 + (yy-y)**2)**0.5 <= r:
                n += 1
                print(n, 'попаданий')
            if ((xx-x1)**2 + (yy-y1)**2)**0.5 <= r1:
                n += 1
                print(n, 'попаданий')
            if ((xx-x2)**2 + (yy-y2)**2)**0.5 <= r2:
                n += 1
                print(n, 'попаданий')

    x += dx
    y += dy
    x1 += dx1
    y1 += dy1
    x2 += dx2
    y2 += dy2

    dvig(event)
    dvig1(event)
    dvig2(event)
    pygame.display.update()
    screen.fill(BLACK)
pygame.quit()