__author__ = 'Pavlov_Egor'


def rand_nums(mux_num):
    for i in range(1, mux_num + 1, 2):
        yield i


odd_to_rand = rand_nums(int(input('Введите конечное значение генератора нечетных чисел: ')))
print(type(odd_to_rand))
print(*odd_to_rand, sep=' ')
