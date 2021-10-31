__author__ = 'Pavlov_Egor'

given_list = ['инженер-конструктор Игорь',
              'главный бухгалтер МАРИНА',
              'токарь высшего разряда нИКОЛАй',
              'директор аэлита']
print(f'Исходный список {given_list}')

print(f'\nСпособ первый пришедший в голову - "последовательный"')

for i in range(len(given_list)):
    name_from_list = given_list[i]
    numb_of_spaces = 0
    last_space = 0
    while numb_of_spaces < name_from_list.count(' '):
        last_space = name_from_list.find(' ', last_space + 1)
        numb_of_spaces += 1
    new_name_from_list = name_from_list[last_space + 1:]
    print(f'Привет, {new_name_from_list.capitalize()}!')

print(f'\nСпособ второй - "перевертыш". Осознан в процессе написания первого')
# можно не менять элементы списка и действовать через переменную, чтобы список остался неизмененным

for i in range(len(given_list)):
    given_list[i] = given_list[i][::-1]
    given_list[i] = given_list[i][:given_list[i].find(' '):]
    given_list[i] = given_list[i][::-1]
    print(f'Привет, {given_list[i].capitalize()}!')
