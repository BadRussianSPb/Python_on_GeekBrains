__author__ = 'Pavlov_Egor'
#  Исключительно в учебных целях создаю список в 3 приема. 10 случайных чисел float, 10 - int и перемешиваю их.

import random

list_of_prices = []
for i in range(10):
    list_of_prices.append(round(random.random() * (90 - 50) + 50, 2))
for i in range(10):
    list_of_prices.append(random.randint(50, 90))
random.shuffle(list_of_prices)

print(f'Исходный список {list_of_prices}')
print('Решение под пунктом A:')
for i in range(len(list_of_prices)):
    if type(list_of_prices[i]) == float:
        whole = int(list_of_prices[i] // 1)
        hundred = int(round(list_of_prices[i] % 1 * 100, 2))  # "костыль" round из-за непонятного округления после "% 1"
        if hundred < 10:
            print(f'{whole} руб 0{hundred} коп', end=', ')
        else:
            print(f'{whole} руб {hundred} коп', end=', ')
    else:
        print(f'{list_of_prices[i]} руб 00 коп', end=', ')
print('\n')

print('Решение под пунктом B:')
first_id = (id(list_of_prices))
list_of_prices.sort()
second_id = (id(list_of_prices))
print(list_of_prices)

print(f'id {first_id} исходного и id {second_id} отсортированного списков равны?: {first_id == second_id}')
print('\nРешение под пунктом С:')
second_list_of_prices = list_of_prices
second_list_of_prices.sort(reverse=True)
print(list_of_prices)

print('\nРешение под пунктом D:')
list_of_prices.sort(reverse=True)  # можно взять готовый перевернутый список из решения C и обойтись одной строкой
print(list_of_prices[0:5:])
