import pygame

pygame.init()


screen = pygame.display.set_mode((300, 300))
screen.fill(pygame.Color('black'))

pygame.draw.rect(screen, pygame.Color('red'), [0, 0, 50, 50])


running = True
x1, y1 = 0, 0
contains = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if x >= x1 and x <= x1 + 50 and y >= y1 and y <= y1 + 50:
                contains = True
            else:
                contains = False

        if event.type == pygame.MOUSEMOTION and event.buttons == (1, 0, 0) and contains:
            screen.fill(pygame.Color('black'))
            pygame.draw.rect(screen, pygame.Color('red'), [event.pos[0], event.pos[1], 50, 50])
            x1, y1 = event.pos

    pygame.display.flip()

pygame.quit()
