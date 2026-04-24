from level import Level
from units import Wall, BasicEnemy # hard coded fix it so we can inherit the whole unit shabang


class Game:
    def __init__(self):
        # self.friendly_units = dict() # maybe not neccery
        # self.enemy_units = dict()
        self.enemy_units_on_screen = list()
        self.friendly_units_on_screen = list()

    def initialize(self): # i want to not hard coded the stuff below
        level = Level(1, 'test')
        level.initialize()  # hard coded
        self.friendly_units_on_screen.append(Wall(1, 'wall', 'glory hole', 5, [500, 600], 1, 1, 1))  # change this to read from settings
        # self.enemy_units_on_screen[1] = BasicEnemy(1, 'wall', 'glory hole', 5, 1, [100, 200], 1, 1,1)  # change this to coded

        for wave, alist in level.enemies.items():
            if wave == 1:
                for enemy in alist:
                    self.enemy_units_on_screen.append(enemy)

