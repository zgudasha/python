import pygame

pygame.init()


screen = pygame.display.set_mode((300, 300))
screen2 = pygame.Surface(screen.get_size())

x1, y1, w, h = 0, 0, 0, 0
coords = []
drawing = False  # режим рисования выключен
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True  # включаем режим рисования
            # запоминаем координаты одного угла
            x1, y1 = event.pos
        if event.type == pygame.MOUSEBUTTONUP:
            # сохраняем нарисованное (на втором холсте)
            screen2.blit(screen, (0, 0))
            drawing = False
            coords.append([x1, y1, w, h])
        if event.type == pygame.MOUSEMOTION:
            # запоминаем текущие размеры
            w, h = event.pos[0] - x1, event.pos[1] - y1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_z and event.mod == pygame.KMOD_LCTRL:
            if len(coords) > 0:
                coords.pop()
                screen2.fill(pygame.Color('black'))
                # print(coords)
                for t_x, t_y, t_w, t_h in coords:
                    pygame.draw.rect(screen2, (0, 0, 255), (t_x, t_y, t_w, t_h), 5)
                screen.blit(screen2, (0, 0))

    # рисуем на экране сохранённое на втором холсте
    # screen.fill(pygame.Color('black'))
    if drawing:  # и, если надо, текущий прямоугольник
        screen.blit(screen2, (0, 0))
        pygame.draw.rect(screen, (0, 0, 255), ((x1, y1), (w, h)), 5)
    pygame.display.flip()
