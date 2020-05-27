class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_mass(self):
        mass = self._length * self._width * 25 * 5 / 1000
        print(mass, 'т')

my_road = Road(20, 5000)
my_road.calc_mass()