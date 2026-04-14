class GameObj:
    def __init__(self, unit_type, name, hp, coords, speed, zaxis, modifiers):
        self.unit_type = unit_type
        self.name = name
        self.hp = hp
        self.coords = coords
        self.speed = speed
        self.zaxis = zaxis
        self.modifiers = modifiers

    def __str__(self):
        return f"unit type:{self.unit_type} name:{self.name} hp:{self.hp} coords:{self.coords} speed:{self.speed} zaxis:{self.zaxis} modifiers:{self.modifiers}"

class Settings:
    grid_size = 100
    melee_distance = 1 * grid_size
    short_range_distance = 2 * grid_size
    long_range_distance = 3 * grid_size

class AttackDistance:
    MELEE = 1
    SHORT = 2
    LONG = 3


class DangerousObj:
    def __init__(self,dmg,pulse):
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



class EnvObj(GameObj):
    def __init__(self, unit_type, name, hp, coords, zaxis, modifiers):
        super().__init__(unit_type, name, hp, coords,0, zaxis, modifiers)


class ProjectileObj(GameObj, DangerousObj):
    def __init__(self, unit_type, name, dmg, pulse, hp, coords, speed, zaxis, modifiers):
        GameObj.__init__(self,unit_type, name, hp, coords, speed, zaxis, modifiers)
        DangerousObj.__init__(self, dmg, pulse)


class FriendlyUnit(GameObj):
    def __init__(self, price, unit_type, name, hp, coords, speed, zaxis, modifiers):
        super().__init__(unit_type, name, hp, coords, speed, zaxis, modifiers)
        self.price = price


class EnemyUnit(GameObj, DangerousObj):
    def __init__(self, dmg, pulse, unit_type, name, hp, coords, speed, zaxis, modifiers):
        GameObj.__init__(self, unit_type, name, hp, coords, speed, zaxis, modifiers)
        DangerousObj.__init__(self, dmg, pulse)

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
    def __init__(self, capacity, ttm, name, hp, coords, zaxis, modifiers):
        super().__init__('Mine', name, hp, coords, 0, zaxis, modifiers)
        self.capacity = capacity
        self.ttm = ttm


class Tree(EnvObj):
    def __init__(self, name, hp, coords, zaxis, modifiers):
        super().__init__('Tree', name, hp, coords, zaxis, modifiers)


class Miner(FriendlyUnit):
    def __init__(self, price, name, hp, coords, speed, zaxis, modifiers):
        super().__init__(price,'Miner', name, hp, coords, speed, zaxis, modifiers)


class Wall(FriendlyUnit):
    def __init__(self, price,unit_type, name, hp, coords, speed, zaxis, modifiers):
        super().__init__(price, unit_type, name, hp, coords, speed, zaxis, modifiers)


class Grid(FriendlyUnit):
    def __init__(self, price, unit_type, name, hp, coords, speed, zaxis, modifiers):
        super().__init__(price, unit_type, name, hp, coords, speed, zaxis, modifiers)


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


# TO DO when attacking check if units coords are close enough to attack