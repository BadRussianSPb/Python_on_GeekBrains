class Stationery():
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Отрисовка {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Отрисовка {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Отрисовка {self.title}')


a = Pen('pen')
a.draw()
b = Pencil('pencil')
b.draw()
c = Handle('handle')
c.draw()
