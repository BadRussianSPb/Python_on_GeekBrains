class Cell:
    def __new__(cls, hexagon):
        if hexagon <= 0:
            print('Ошибка! Клетка не создана.')
            return None
        else:
            return super().__new__(cls)

    def __init__(self, hexagon):  # назвал hexagon чтобы не запутаться в клетках (cell) и ячейках (cells)
        self.hexagon = int(hexagon)
        print(f'Клетка с {self.hexagon} ячейками создана')

    def __add__(self, other):
        new_cell = self.hexagon + other.hexagon
        return new_cell

    def __sub__(self, other):
        print('__sub__ сработал. И...', end='')
        new_cell = self.hexagon - other.hexagon
        return new_cell

    def __mul__(self, other):
        new_cell = self.hexagon * other.hexagon
        return new_cell

    def __floordiv__(self, other):
        new_cell = self.hexagon // other.hexagon
        return new_cell

    def __truediv__(self, other):
        new_cell = round(self.hexagon / other.hexagon)
        return new_cell

    def make_order(self, number):
        rows = self.hexagon // number
        result_str = ''
        if rows != 0:
            for i in range(rows):
                if i == rows - 1:
                    result_str += ('*' * number)
                else:
                    result_str += ('*' * number) + '\\n'
            if self.hexagon % number > 0:
                result_str += '\\n' + ('*' * (self.hexagon % number))
        else:
            result_str += ('*' * self.hexagon)
        return result_str


a = Cell(12)
b = Cell(5)
c = Cell(a + b)
d = Cell(b - c)
print(type(d))  # экземпляр не создан, но метод __sub__ сработал :(. Часа 3 мучил без толку @property сделал __new__
e = Cell(a - b)
f = Cell(b * e)
j = Cell(f // c)
h = Cell(c / j)
print(f.make_order(4))
print(b.make_order(10))
