class Road:

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def calculation_mass_asphalt(self):
        mass_asphalt = 25
        thickness = 1

        return (self._length * self._width * mass_asphalt * thickness) / 1000


calc = Road(5000, 20)

print(calc.calculation_mass_asphalt())
