class Car:
    def __init__(self, color, name, is_police=False, speed=0):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self, speed=40):
        self.speed = speed
        print(f'{self.name} {self.color} стартанул со скоростью {self.speed}')

    def stop(self):
        self.speed = 0
        print(f'{self.name} {self.color} остановился')

    def turn(self, direction):
        if self.is_police:
            print(f'{self.name} {self.color} включил мигалки и повернул {direction}')
        else:
            print(f'{self.name} {self.color} повернул {direction}')

    def show_speed(self):
        if self.speed == 0:
            print(f'{self.name} {self.color} не двигается')
        else:
            print(f'{self.name} {self.color} скорость {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed == 0:
            print(f'{self.name} {self.color} не двигается')
        else:
            show_speeding(self.speed, 60, self.name, self.color)


class WorkCar(Car):
    def show_speed(self):
        if self.speed == 0:
            print(f'{self.name} {self.color} не двигается')
        else:
            show_speeding(self.speed, 40, self.name, self.color)


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


def show_speeding(speed, limit, name, color):
    if speed > limit:
        print(f'{name} {color} превышает на {speed - limit}')
    else:
        print(f'{name} {color} не превышает и едет со скоростью {speed}')


car1 = WorkCar('зеленый', 'трактор')
car2 = TownCar('красный', 'автобус')
car3 = SportCar('разноцветный', 'болид')
car4 = PoliceCar('синий', 'седан', True)

car1.show_speed()
car2.go(30)
car1.go(60)
car3.go(120)
car1.show_speed()
car2.show_speed()
car4.turn(f'за {car1.name}')
car1.stop()
car1.show_speed()
print(f'А нас не догонят! {car3.name} ушел на {car3.speed + 50}')
