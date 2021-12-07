class Clothe:
    def __init__(self, v=0, h=0):
        self.fabric = 0
        self.volume = v
        self.height = h

    def calc_fabric(self):
        raise NotImplementedError("Необходимо переопределить метод")

    def __add__(self, other):
        result = self.fabric + other
        print(f'Всего ткани нужно', end='')
        return result

    def __mul__(self, other):
        result = self.fabric * other
        return result


class Coat(Clothe):
    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume):
        if volume < 0:
            self.__volume = 0  # наверное есть какие-то стандарты объема, но мне не ведомы
        else:
            self.__volume = volume

    def calc_fabric(self):
        self.fabric = (self.volume/6.5 + 0.5)
        return self.fabric


class Suit(Clothe):
    @property
    def calc_fabric(self):
        self.fabric = (self.height * 2 + 0.3)
        return self.fabric


a = Coat(-10, 7)
b = Suit(5, 7)
print(f'Ткани на 1 пальто: {a.calc_fabric()}')
print(f'Ткини на 1 костюм: {b.calc_fabric}')  # пускай будет по разному реализован @property
print(f'Ткани на 10 костюмов/ма :', b * 5)
print(f'Ткани на 10 пальто: ', a * 10)
print(f'На весь гардероб нужно {(a * 10) + (b * 5)} ткани')
