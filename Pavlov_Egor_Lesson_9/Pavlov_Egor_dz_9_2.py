class Road:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def mass_of_asphalt(self, thickness=5, mass_of_sm=25):
        result = self._lenght * self._width * thickness * mass_of_sm / 1000
        return f'Масса асфальта дял заданных данных: {result} т'


a = Road(5000, 20)
print(type(a.mass_of_asphalt()))
print(a.mass_of_asphalt(25, 5))
