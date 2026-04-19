import pygame
import sys
import game_logic
from game_logic import Settings

pygame.init()
screen = pygame.display.set_mode((Settings.WIDTH, Settings.HEIGHT))
pygame.display.set_caption(Settings.TITLE)

clock = pygame.time.Clock()

game = game_logic.Game()
game.initialize()

def draw_grid():
    for row in range(Settings.ROWS):
        for col in range(Settings.COLS):
            rect = pygame.Rect(
                col * Settings.GRID_BLOCK_SIZE,
                row * Settings.GRID_BLOCK_SIZE,
                Settings.GRID_BLOCK_SIZE,
                Settings.GRID_BLOCK_SIZE
            )
            pygame.draw.rect(screen, Settings.BLUE, rect, 1)


def draw_unit(unit,color):
    rect = pygame.Rect(
        unit.coords[0],  # this coord is the x coord
        unit.coords[1],  # this one is the y coord
        Settings.GRID_BLOCK_SIZE,  # this one is the width
        Settings.GRID_BLOCK_SIZE  # this one is the height
    )
    pygame.draw.rect(screen, color, rect, 1)


def draw_all_units():
    for unit in game.friendly_units.values():
        draw_unit(unit, Settings.PASO)
    for unit in game.enemy_units.values():
        draw_unit(unit, Settings.RED)


def assign_targets():
    for unit in game.enemy_units.values():
        unit.calc_speed(unit.x_distance(game.friendly_units[1]),unit.y_distance(game.friendly_units[1]))


def move_all_enemies():
    for unit in game.enemy_units.values():
        unit.move()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(Settings.BLACK)
    draw_grid()
    assign_targets()
    move_all_enemies()
    draw_all_units()
    pygame.display.flip()
    clock.tick(Settings.FPS)

pygame.quit()
sys.exit()