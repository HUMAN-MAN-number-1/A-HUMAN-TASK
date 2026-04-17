import pygame
import sys
import game_obj as game_logic
from game_obj import Settings

# Window size
WIDTH = Settings.COLS * Settings.GRID_BLOCK_SIZE
HEIGHT = Settings.ROWS * Settings.GRID_BLOCK_SIZE

# Colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("9x20 Blue Grid")

clock = pygame.time.Clock()


def draw_grid():
    screen.fill(BLACK)

    for row in range(Settings.ROWS):
        for col in range(Settings.COLS):
            rect = pygame.Rect(
                col * Settings.GRID_BLOCK_SIZE,
                row * Settings.GRID_BLOCK_SIZE,
                Settings.GRID_BLOCK_SIZE,
                Settings.GRID_BLOCK_SIZE
            )
            pygame.draw.rect(screen, BLUE, rect, 1)  # 1 = outline thickness


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_grid()
    pygame.display.flip()
    clock.tick(Settings.FPS)

pygame.quit()
sys.exit()