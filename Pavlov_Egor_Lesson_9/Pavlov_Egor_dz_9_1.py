import time
import sys


class Trafficlight:
    __color = ['Red', 'Yellow', 'Green']

    def running(self, *args):
        print('Запуск светофора')
        for el, sec in zip(self.__color, args):
            print(el)
            time_left(sec)


def time_left(sec):
    for i in range(sec, -1, -1):
        sys.stdout.write(f'\r{i}')
        sys.stdout.flush()
        time.sleep(1)
    print('')


a = Trafficlight()
a.running(7, 2, 5)
