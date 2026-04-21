from level import Level


class Game:
    def __init__(self):
        self.friendly_units = dict()
        self.enemy_units = dict()
        self.enemy_units_on_screen = dict()
        self.friendly_units_on_screen = dict()

    def initialize(self):
        level1 = Level(1, 'test')
        level1.initialize()
        self.friendly_units_on_screen[1] = Wall(1, 'wall', 'glory hole', 5, [500, 600], 1, 1, 1)
        self.enemy_units_on_screen[1] = BasicEnemy(1, 'wall', 'glory hole', 5, 1, [100, 200], 1, 1,1)


