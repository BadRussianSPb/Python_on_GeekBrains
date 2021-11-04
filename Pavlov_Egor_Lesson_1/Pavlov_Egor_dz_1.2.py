__author__ = 'Pavlov_Egor'

# задаем список кубов нечетных чисел от 1 до 1000
list_of_cubes = []
for i in range(1, 1000, 2):
    list_of_cubes.append(i ** 3)

# Решение задания №2 пункт a : Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7
result = 0
for i in range(len(list_of_cubes)):
    sum_of_cube_numb = 0
    list_of_cubes_temp = list_of_cubes[i]
    while list_of_cubes_temp > 0:
        sum_of_cube_numb += list_of_cubes_temp % 10
        list_of_cubes_temp = list_of_cubes_temp // 10
    if sum_of_cube_numb % 7 == 0:
        result += (list_of_cubes[i])
print(f'Сумма чисел из списка, сумма цифр которых делится нацело на 7 составляет: {result}')

# Решение задания №2 пункт b и c: К каждому элементу списка добавить 17 и заново вычислить
# сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7, без нового списка

result = 0
for i in range(len(list_of_cubes)):
    list_of_cubes[i] += 17
    sum_of_cube_numb = 0
    list_of_cubes_temp = list_of_cubes[i]
    while list_of_cubes_temp > 0:
        sum_of_cube_numb += list_of_cubes_temp % 10
        list_of_cubes_temp = list_of_cubes_temp // 10
    if sum_of_cube_numb % 7 == 0:
        result += (list_of_cubes[i])
print(f'Сумма чисел, увеличенных на 17, сумма цифр которых делится нацело на 7 составляет: {result}')
