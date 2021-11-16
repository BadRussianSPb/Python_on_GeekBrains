__author__ = 'Pavlov_Egor'

last_num = int(input('Введите конечное значение генератора нечетных чисел: '))
odd_to_rand = (i for i in range(1, last_num + 1, 2))

print(type(odd_to_rand))
print(*odd_to_rand, sep=' ')
