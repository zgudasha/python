import pygame, random

# Начнем с описания класса поля
class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # заполняем случайное кол-во клеточек по случайным индексам - 1
        for i in range(random.randint(5, 10)):
            # print(random.randint(0, width - 1), random.randint(0, height - 1))
            self.board[random.randint(0, height - 1)][random.randint(0, width - 1)] = 1
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 50

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size
        
    def render(self, screen):
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == 1:
                    color = pygame.Color('red')
                    width = 0
                else:
                    color = pygame.Color('white')
                    width = 1
                pygame.draw.rect(screen, color, (self.left + i*self.cell_size, self.top + j*self.cell_size, self.cell_size, self.cell_size), width)

    def get_cell(self, mouse_pos):
        for i in range(self.height):
            if i * self.cell_size <= mouse_pos[0] and i * self.cell_size + self.cell_size >= mouse_pos[0]:
                for j in range(self.width):
                    if j * self.cell_size <= mouse_pos[1] and j * self.cell_size + self.cell_size >= mouse_pos[1]:
                        return i, j
        return None

    def get_click(self, mouse_pos, screen):
        cell_coords = self.get_cell(mouse_pos)
        if not cell_coords is None:
            self.on_click(cell_coords, screen)
    
    def on_click(self, cell_coords, screen):
        i, j = cell_coords
        if self.board[i][j] == 0:
            font = pygame.font.Font(None, 24)
            s = 0
            for i_ in range(i - 1, i + 2):
                for j_ in range(j - 1, j + 2):
                    if 0 <= i_ < self.height and 0 <= j_ < self.width:
                        s += self.board[i_][j_]
            text = font.render(str(s), 1, pygame.Color('white'))
            pos_x = i * self.cell_size + self.cell_size // 2
            pos_y = j * self.cell_size + self.cell_size // 2
            screen.blit(text, (pos_x, pos_y))
                
width = 500

pygame.init()
screen = pygame.display.set_mode((width, width))
board = Board(5, 7)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos, screen)
    board.render(screen)
    pygame.display.flip()

pygame.quit()