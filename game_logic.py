from level import Level
from units import Wall, BasicEnemy # hard coded fix it so we can inherit the whole unit shabang


class Game:
    def __init__(self):
        # self.friendly_units = dict() # maybe not neccery
        # self.enemy_units = dict()
        self.enemy_units_on_screen = dict()
        self.friendly_units_on_screen = dict()

    def initialize(self): # i want to not hard coded the stuff below
        level1 = Level(1, 'test')
        level1.initialize()  # hard coded
        self.friendly_units_on_screen[1] = Wall(1, 'wall', 'glory hole', 5, [500, 600], 1, 1, 1)  # change this to read from settings
        self.enemy_units_on_screen[1] = BasicEnemy(1, 'wall', 'glory hole', 5, 1, [100, 200], 1, 1,1)  # change this to coded


