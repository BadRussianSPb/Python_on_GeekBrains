# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляро

class Woker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': float(wage), 'bonus': float(bonus)}


class Position(Woker):
    def get_full_name(self):
        return self.name, self.surname

    def get_total_incom(self):
        return sum(self._income.values())


a = Position('Egor', 'Pavlov', 'Buh', 110, 50)
print(*a.get_full_name())
print(a.get_total_incom())
