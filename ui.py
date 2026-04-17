import pygame
import sys
import game_obj as game_logic

# Grid settings
ROWS = 9
COLS = 20
CELL_SIZE = 100
FPS = 60

# Window size
WIDTH = COLS * CELL_SIZE
HEIGHT = ROWS * CELL_SIZE

# Colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("9x20 Blue Grid")

clock = pygame.time.Clock()


def draw_grid():
    screen.fill(BLACK)

    for row in range(ROWS):
        for col in range(COLS):
            rect = pygame.Rect(
                col * CELL_SIZE,
                row * CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE
            )
            pygame.draw.rect(screen, BLUE, rect, 1)  # 1 = outline thickness


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_grid()
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()