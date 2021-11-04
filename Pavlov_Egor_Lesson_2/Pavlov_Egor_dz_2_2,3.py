__author__ = 'Pavlov_Egor'

given_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(f'Заданный список {given_list}\n')

i = 0
while i < len(given_list):
    if given_list[i].isdigit() or not given_list[i].isalnum():  # проверили на "число"
        if len(given_list[i]) == 1:  # проверили на развряды
            given_list[i] = '0' + given_list[i]  # добавили "0" если разряд 1
        elif len(given_list[i]) == 2 and given_list[i][0] == '+' or given_list[i][0] == '-':
            given_list[i] = given_list[i][0] + '0' + given_list[i][1:2:]
        given_list.insert(i, '"')  # вставили в список первую "
        given_list.insert(i + 2, '"')  # вставили в список вторую " со смещением на первую " и сам элемент
        print(f'{given_list[i]}{given_list[i + 1]}{given_list[i + 2]}', end=' ')  # вывели на экран конструкцию.
        i += 2  # прокрутили счетчик вперед из-за новых элементов
    else:
        print(given_list[i], end=' ')  # просто выводим элемент списка
    i += 1
