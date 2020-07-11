import pygame

width, count = (int(i) for i in input().split())

pygame.init()
screen = pygame.display.set_mode((width // count * count, width // count * count)) # чтобы не было "черных линий"

screen.fill(pygame.Color('black'))
cell_size = width // count

for i in range(count):
    for j in range(count):
        if (i + j) % 2 == 0:
            pygame.draw.rect(screen, pygame.Color('black'), [i * cell_size, j * cell_size, cell_size, cell_size])
        else:
            pygame.draw.rect(screen, pygame.Color('white'), [i * cell_size, j * cell_size, cell_size, cell_size])

pygame.display.flip()

while pygame.event.wait().type != pygame.QUIT:
    pass

pygame.quit()
