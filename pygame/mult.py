import pygame
from math import sin, cos, radians

def get_coord(n, radius, width):
    x = int(cos(radians(n)) * radius) + width // 2
    y = int(sin(radians(n)) * radius) + width // 2
    return x, y

width = 500
radius = 200
pygame.init()
screen = pygame.display.set_mode((width, width))
screen.fill(pygame.Color('black'))

running = True
pause = False
coefficient = 2

while running:
    screen.fill(pygame.Color('black'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if pause:
                pause = False
            else:
                pause = True
    if not pause:
        for i in range(360):
            pygame.draw.line(screen, pygame.Color('pink'), get_coord(i, radius, width), get_coord(i * coefficient, radius, width), 1)
        coefficient += 0.01
        pygame.display.flip()
