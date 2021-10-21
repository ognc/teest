import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 800))
circle(screen, (255, 255, 0), (400,350), 204)
circle(screen, (0, 255, 0), (400,350), 200)
circle(screen, (255, 255, 255), (320, 270), 25)
circle(screen, (255, 255, 255), (475, 270), 25)
circle(screen, (0, 0, 0), (320, 270), 19)
circle(screen, (0, 0, 0), (475, 270), 19)
polygon(screen, (255, 255, 0), [(430,250), (560,160),
                               (565,165), (436,255),])
polygon(screen, (255, 255, 0), [(200,165), (350,250),
                               (353,245), (204,160),])
rect(screen, (255, 5, 44), (300, 460, 200, 20))
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()