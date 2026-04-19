class Game:
    def __init__(self):
        self.friendly_units = dict()
        self.enemy_units = dict()

    def initialize(self):
        self.friendly_units[1] = Wall(1, 'wall', 'glory hole', 5, [100, 0], 1, 1, 1)
        self.enemy_units[1] = BasicEnemy(1, 'wall', 'glory hole', 5, 1, [200, 500], 1, 1,1)


class Unit:
    def __init__(self, unit_type, name, hp, coords, zaxis, modifiers):
        self.unit_type = unit_type
        self.name = name
        self.hp = hp
        self.coords = coords
        self.zaxis = zaxis
        self.modifiers = modifiers

    def __str__(self):
        return f"unit type:{self.unit_type} name:{self.name} hp:{self.hp} coords:{self.coords} zaxis:{self.zaxis} modifiers:{self.modifiers}"

    def x_distance(self, other_point):
        return other_point.coords[0] - self.coords[0]  # x is the 0 of chords

    def y_distance(self, other_point):
        return other_point.coords[1] - self.coords[1]   # y is the 1 of chords

    def place(self, x, y):
        self.coords[0] = x
        self.coords[1] = y


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
    MELEE = 1
    SHORT = 2
    LONG = 3


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


class Dangerous:
    def __init__(self, dmg, pulse):
        self.dmg = dmg
        self.pulse = pulse

    @staticmethod
    def attack(attacker, target, attack_distance_type=AttackDistance.MELEE):  # unfinished class method
        target.hp -= attacker.dmg
        print(attacker.name, 'attacking', target.name, 'causing dmg:', attacker.dmg)

    @staticmethod
    def check_distance(attacker, target):
        xd = abs(attacker.coords[0] - target.coords[0])  # the coords 0 is the X axis
        yd = abs(attacker.coords[1] - target.coords[1])  # coords 1 is Y axis
        d = (xd **2 + yd **2)**0.5
        print("distance:", d)
        return d

    @staticmethod
    def is_in_range(distance, attack_distance_type):
        attack_distance = -1
        if attack_distance_type == AttackDistance.MELEE:
            attack_distance = Settings.MELEE_DISTANCE
        if attack_distance_type == AttackDistance.SHORT:
            attack_distance = Settings.SHORT_RANGE_DISTANCE
        if attack_distance_type == AttackDistance.LONG:
            attack_distance = Settings.LONG_RANGE_DISTANCE
        print(distance <= attack_distance)
        return distance <= attack_distance


class Movable:
    def __init__(self, speed):
        self.speed = speed
        self.h_speed = 0
        self.v_speed = 0

    def calc_speed(self, x_distance, y_distance):
        if y_distance == 0:
            abs_v_speed = 0
            abs_h_speed = self.speed

        elif x_distance == 0:
            abs_h_speed = 0
            abs_v_speed = self.speed
        else:
            ratio = abs(x_distance / y_distance)
            abs_v_speed = (self.speed**2/(ratio+1))**0.5
            abs_h_speed = ratio * y
        self.v_speed = abs_v_speed if y_distance > 0 else -abs_v_speed
        self.h_speed = abs_h_speed if x_distance > 0 else -abs_h_speed
        return [self.h_speed, self.v_speed]

    def move(self):
        self.place(self.coords[0] + self.h_speed, self.coords[1] + self.v_speed)


class Env(Unit):
    def __init__(self, unit_type, name, hp, coords, zaxis, modifiers):
        super().__init__(unit_type, name, hp, coords, zaxis, modifiers)


class Projectile(Unit, Dangerous, Movable):
    def __init__(self, unit_type, name, dmg, pulse, hp, coords, speed, zaxis, modifiers):
        Unit.__init__(self,unit_type, name, hp, coords, zaxis, modifiers)
        Dangerous.__init__(self, dmg, pulse)
        Movable.__init__(self, speed)


class FriendlyUnit(Unit):
    def __init__(self, price, unit_type, name, hp, coords, zaxis, modifiers):
        super().__init__(unit_type, name, hp, coords, zaxis, modifiers)
        self.price = price


class EnemyUnit(Unit, Dangerous, Movable):
    def __init__(self, dmg, pulse, unit_type, name, hp, coords, speed, zaxis, modifiers):
        Unit.__init__(self, unit_type, name, hp, coords, zaxis, modifiers)
        Dangerous.__init__(self, dmg, pulse)
        Movable.__init__(self, speed)

    def attack(self, target):
        super().attack(self, target)


class Modifier:
    pass


class BasicEnemy(EnemyUnit):
    def __init__(self, dmg, pulse, unit_type, name, hp, coords, speed, zaxis, modifiers):
        super().__init__(dmg, pulse, unit_type, name, hp, coords, speed, zaxis, modifiers)


class Boss(EnemyUnit):
    def __init__(self, dmg, pulse, unit_type, name, hp, coords, speed, zaxis, modifiers):
        super().__init__(dmg, pulse, unit_type, name, hp, coords, speed, zaxis, modifiers)


class Mine(Env):
    def __init__(self, capacity, ttm, name, hp, coords, zaxis, modifiers):  # ttm "time to mine"
        super().__init__('Mine', name, hp, coords, zaxis, modifiers)
        self.capacity = capacity
        self.ttm = ttm


class Tree(Env):
    def __init__(self, name, hp, coords, zaxis, modifiers):
        super().__init__('Tree', name, hp, coords, zaxis, modifiers)


class Miner(FriendlyUnit, Movable):
    def __init__(self, price, name, hp, coords, speed, zaxis, modifiers):
        FriendlyUnit.__init__(self, price, 'Miner', name, hp, coords, zaxis, modifiers)
        Movable.__init__(self, speed)


class Wall(FriendlyUnit, Movable):
    def __init__(self, price, unit_type, name, hp, coords,speed, zaxis, modifiers):
        FriendlyUnit.__init__(self, price, unit_type, name, hp, coords, zaxis, modifiers)
        Movable.__init__(self, speed)


class Grid(FriendlyUnit):
    def __init__(self, price, unit_type, name, hp, coords, zaxis, modifiers):
        super().__init__(price, unit_type, name, hp, coords, zaxis, modifiers)


class Bullet(Projectile):
    def __init__(self, unit_type, name, dmg, pulse, hp, coords, speed, zaxis, modifiers):

        super().__init__(unit_type, name, dmg, pulse, hp, coords, speed, zaxis, modifiers)


if __name__ == '__main__':
    eu = EnemyUnit(1, 1, 'enemy', 'black punisher', 1, [0, 0], 60, 1, 1)
    print(eu)

    w = Wall(1, 'wall', 'glory hole', 5, [100, 0], 1, 1, 1)
    print(w)
    eu.attack(w)
    print(w)
    eu.attack(w)
    print(w)

    d = eu.check_distance(eu, w)
    eu.is_in_range(d, attack_distance_type=AttackDistance.MELEE)
    x_distance = eu.x_distance(w)
    y_distance = eu.y_distance(w)
    print(w.coords)
    print(eu.coords)
    eu.calc_speed(x_distance, y_distance)
    eu.move()
    print(eu.coords)
    eu.is_in_range(d, attack_distance_type=AttackDistance.MELEE)
    print(w.coords)

# TO DO keep changing the speed thing
# y_distance = starting_point.y_distance(ending_point)
# x_distance = starting_point.x_distance(ending_point)
