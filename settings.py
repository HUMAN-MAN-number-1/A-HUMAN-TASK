class Settings:
    GRID_BLOCK_SIZE = 100
    ROWS = 9
    COLS = 20
    FPS = 60
    BASE_SPEED = 1 * GRID_BLOCK_SIZE / FPS
    MELEE_DISTANCE = 1 * GRID_BLOCK_SIZE
    SHORT_RANGE_DISTANCE = 2 * GRID_BLOCK_SIZE
    LONG_RANGE_DISTANCE = 3 * GRID_BLOCK_SIZE
    WIDTH = COLS * GRID_BLOCK_SIZE
    HEIGHT = ROWS * GRID_BLOCK_SIZE
    TITLE = "CHADMAN SAVES THE UNITED STATES"
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    PASO = (124,213,8)
    RED = (255, 0, 0)


class AttackDistance:
    MELEE = 1 * Settings.GRID_BLOCK_SIZE
    SHORT = 2 * Settings.GRID_BLOCK_SIZE
    LONG = 3 * Settings.GRID_BLOCK_SIZE


class UnitType:
    TURRET = 1
    PROJECTILE = 2
    WALL = 3
    ENEMY = 4
    GRID = 5
    MINE = 6
    MINER = 7
    PORTAL = 8


class AttackType:
    PHYSICAL = 1
    FOOD = 2
    FIRE = 3
    ICE = 4
