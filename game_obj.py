class GameObj:
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
        return abs(self.coords[0] - other_point.coords[0])  # x is the 0 of chords

    def y_distance(self, other_point):
        return abs(self.coords[1] - other_point.coords[1])      # y is the 1 of chords


class Settings:
    grid_size = 100
    fps = 60
    base_speed = 1 * grid_size / fps
    melee_distance = 1 * grid_size
    short_range_distance = 2 * grid_size
    long_range_distance = 3 * grid_size



class AttackDistance:
    MELEE = 1
    SHORT = 2
    LONG = 3


class DangerousObj:
    def __init__(self, dmg, pulse):
        self.dmg = dmg
        self.pulse = pulse

    @staticmethod
    def attack(attacker, target, attack_distance_type = AttackDistance.MELEE): # unfinished class method
        target.hp -= attacker.dmg
        print(attacker.name, 'attacking', target.name, 'causing dmg:', attacker.dmg)

    @staticmethod
    def check_distance(attacker, target):
        xd = abs(attacker.coords[0] - target.coords[0]) # the coords 0 is the X axis
        yd = abs(attacker.coords[1] - target.coords[1]) # coords 1 is Y axis
        d = (xd **2 + yd **2)**0.5
        print("distance:", d)
        return d

    @staticmethod
    def is_in_range( distance, attack_distance_type):
        attack_distance = -1
        if attack_distance_type == AttackDistance.MELEE:
            attack_distance = Settings.melee_distance
        if attack_distance_type == AttackDistance.SHORT:
            attack_distance = Settings.short_range_distance
        if attack_distance_type == AttackDistance.LONG:
            attack_distance = Settings.long_range_distance
        print(distance <= attack_distance)
        return distance <= attack_distance


class MovableObj:
    def __init__(self, speed):
        self.speed = speed
        self.h_speed = 0
        self.v_speed = 0

    @staticmethod
    def move(starting_point, ending_point):
        x_distance = starting_point.x_distance(ending_point)
        y_distance = starting_point.y_distance(ending_point)
        ratio = x_distance / y_distance
        y = (starting_point.speed**2/(ratio+1))**0.5  # explain the formula again
        x = ratio * y
        return [x, y]



class EnvObj(GameObj):
    def __init__(self, unit_type, name, hp, coords, zaxis, modifiers):
        super().__init__(unit_type, name, hp, coords, zaxis, modifiers)


class ProjectileObj(GameObj, DangerousObj, MovableObj):  # set projectile to moving obj
    def __init__(self, unit_type, name, dmg, pulse, hp, coords, speed, zaxis, modifiers):
        GameObj.__init__(self,unit_type, name, hp, coords, zaxis, modifiers)
        DangerousObj.__init__(self, dmg, pulse)
        MovableObj.__init__(self, speed)


class FriendlyUnit(GameObj):
    def __init__(self, price, unit_type, name, hp, coords, zaxis, modifiers):
        super().__init__(unit_type, name, hp, coords, zaxis, modifiers)
        self.price = price


class EnemyUnit(GameObj, DangerousObj, MovableObj):
    def __init__(self, dmg, pulse, unit_type, name, hp, coords, speed, zaxis, modifiers):
        GameObj.__init__(self, unit_type, name, hp, coords, zaxis, modifiers)
        DangerousObj.__init__(self, dmg, pulse)
        MovableObj.__init__(self, speed)

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


class Mine(EnvObj):
    def __init__(self, capacity, ttm, name, hp, coords, zaxis, modifiers):  # ttm "time to mine"
        super().__init__('Mine', name, hp, coords, zaxis, modifiers)
        self.capacity = capacity
        self.ttm = ttm


class Tree(EnvObj):
    def __init__(self, name, hp, coords, zaxis, modifiers):
        super().__init__('Tree', name, hp, coords, zaxis, modifiers)


class Miner(FriendlyUnit, MovableObj):
    def __init__(self, price, name, hp, coords, speed, zaxis, modifiers):
        FriendlyUnit.__init__(self, price, 'Miner', name, hp, coords, zaxis, modifiers)
        MovableObj.__init__(self, speed)


class Wall(FriendlyUnit, MovableObj):
    def __init__(self, price, unit_type, name, hp, coords,speed, zaxis, modifiers):
        FriendlyUnit.__init__(self, price, unit_type, name, hp, coords, zaxis, modifiers)
        MovableObj.__init__(self, speed)


class Grid(FriendlyUnit):
    def __init__(self, price, unit_type, name, hp, coords, zaxis, modifiers):
        super().__init__(price, unit_type, name, hp, coords, zaxis, modifiers)


class Bullet(ProjectileObj):
    def __init__(self, unit_type, name, hp, coords, speed, zaxis, modifiers):
        super().__init__(unit_type, name, hp, coords, speed, zaxis, modifiers)


eu = EnemyUnit(1, 1, 'enemy', 'black punisher', 1, [1, 2], 1, 1, 1)
print(eu)

w = Wall(1, 'wall', 'glory hole', 5, [1, 3], 1, 1, 1)
print(w)
eu.attack(w)
print(w)
eu.attack(w)
print(w)

d = eu.check_distance(eu, w)
eu.is_in_range(d,attack_distance_type=AttackDistance.MELEE)


# TO DO keep changing the speed thing