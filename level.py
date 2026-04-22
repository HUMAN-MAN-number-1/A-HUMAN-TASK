from settings import Settings


class Level:
    def __init__(self, number, name):
        self.number = number
        self.name = name
        self.waves = 0
        self.enemies = dict()

    def initialize(self):
        with open(f'levels\\level_{self.number}_enemies', 'r') as f:
            all_rows = f.read().split('\n')
        for row in all_rows:
            row_length = len(row.rstrip())
            if row_length > self.waves:
                self.waves = row_length
        for wave_number in range(1, self.waves + 1):
            self.enemies[wave_number] = ''
        for wave_index in range(self.waves):
            wave_number = wave_index + 1
            for row_index in range(Settings.ROWS):  # HARD CODED FOR 9
                if wave_index < len(all_rows[row_index]):
                    self.enemies[wave_number] += all_rows[row_index][wave_index]
                else:
                    self.enemies[wave_number] += ' '


if __name__ == '__main__':
    level1 = Level(1, 'test')
    level1.initialize()
    print(level1.enemies)