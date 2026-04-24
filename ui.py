import pygame
import sys
import game_logic
from settings import Settings
from settings import AttackDistance
from level import Level

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
            pygame.draw.rect(screen, Settings.COLOR_BLUE, rect, 1)


def draw_unit(unit,color):
    rect = pygame.Rect(
        unit.coords[0],  # this coord is the x coord
        unit.coords[1],  # this one is the y coord
        Settings.GRID_BLOCK_SIZE,  # this one is the width
        Settings.GRID_BLOCK_SIZE  # this one is the height
    )
    pygame.draw.rect(screen, color, rect, 1)


def draw_all_units():
    for unit in game.friendly_units_on_screen:
        draw_unit(unit, Settings.COLOR_PASO)
    for unit in game.enemy_units_on_screen:
        draw_unit(unit, Settings.COLOR_RED)


def assign_targets():
    for unit in game.enemy_units_on_screen:
        unit.calc_speed(unit.x_distance(game.friendly_units_on_screen[0]),unit.y_distance(game.friendly_units_on_screen[0]))
    

def move_all_enemies():
    for unit in game.enemy_units_on_screen:
        unit.move()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(Settings.COLOR_BLACK)
    draw_grid()
    assign_targets()
    move_all_enemies()
    # d = game.enemy_units_on_screen[1].check_distance(game.enemy_units_on_screen[1], game.friendly_units_on_screen[1])
    # print(game.enemy_units_on_screen[1].coords, game.enemy_units_on_screen[1].is_in_range(d, attack_distance_type=AttackDistance.SHORT))
    draw_all_units()
    pygame.display.flip()
    clock.tick(Settings.FPS)

pygame.quit()
sys.exit()