class MyError(Exception):
    @staticmethod
    # def is_dev_zero(x, y):  # для первого варианта
    def is_div_zero():
        tmp_list = input('Введите 2 числа через пробел \n')  # убрать для первого варианта
        tmp_list = tmp_list.split(' ')  # убрать для первого варианта
        x, y = tmp_list[0], tmp_list[1]  # убрать для первого варианта
        try:
            if int(y) == 0:
                raise MyError('Ошибка деления на 0.\n')
        except MyError as err:
            print(err, 'Попробуйте еще раз.')
            return MyError.is_div_zero()  # убрать для первого варианта
        else:
            return print(int(x) / int(y))


MyError.is_div_zero()

# первый вариант был с вводом и последующим запуском метода класса, но этот вариант просто выходит без остановки
# MyError.is_dev_zero(*(input('Введите 2 числа через пробел \n').split(' ')))
# MyError.is_dev_zero(6, 0)
# MyError.is_dev_zero(6, 5)  # работает дальше и не завершается с ошибкой
