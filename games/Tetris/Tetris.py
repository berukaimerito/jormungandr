import pygame

blocks = [
    [[1, 4, 7,], [3, 4, 5]],  # straight
    [[1, 3, 4, 5, 7]],  # cross
    [[0, 1, 4, 5], [1, 3, 4, 6]],  # two on two 1
    [[1, 2, 3, 4], [0, 3, 4, 7]],  # two on two 2
    [[0, 1, 3, 6], [0, 1, 2, 5], [2, 5, 7, 8], [3, 6, 7, 8]],
    [[1, 2, 5, 8], [5, 6, 7, 8], [0, 3, 6, 7], [0, 1, 2, 3]],
    [[4, 6, 7, 8], [0, 3, 4, 6], [0, 1, 2, 4], [2, 4, 5, 8]],
]


class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = 0
        self.rotation = 0

    def shape(self):
        return blocks[self.type][self.rotation]


def draw_block():
    for y in range(3):
        for x in range(3):
            if y * 3 + x in block.shape():
                pygame.draw.rect(screen, (255, 255, 255),
                                 [(x + block.x) * grid_size + x_gap + 1, (y + block.y) * grid_size + y_gap + 1,
                                 grid_size - 2, grid_size - 2])


def draw_grid(columns, rows, grid_size, x_gap, y_gap):
    for y in range(rows):
        for x in range(columns):
            pygame.draw.rect(screen, (100, 100, 100),
                             [x * grid_size + x_gap, y * grid_size + y_gap, grid_size, grid_size], 1)


grid_size = 30
pygame.init()
screen = pygame.display.set_mode((500,600))
pygame.display.set_caption("Tetris")
cols = screen.get_width() // grid_size
rows = screen.get_height() // grid_size
x_gap = (screen.get_width() - cols * grid_size) // 2
y_gap = (screen.get_height() - rows * grid_size) // 2
block = Block(5, 6)

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    screen.fill((0, 0, 0))
    draw_grid(cols, rows, grid_size, x_gap, y_gap)
    draw_block()
    pygame.display.update()
pygame.quit()
