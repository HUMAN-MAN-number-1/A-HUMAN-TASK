
class Level:
    def __init__(self, number, name):
        self.number = number
        self.name = name
        self.enemies = dict()

    def initialize(self):
        with open(f'levels\\level_{self.number}_enemies', 'r') as f:
            all_rows = f.readlines()
            for i in range(len(all_rows)):
                self.enemies[i+1] = all_rows[i][:-1]

        print(self.enemies)
if __name__ == '__main__':
    level1 = Level(1, 'test')
    level1.initialize()

