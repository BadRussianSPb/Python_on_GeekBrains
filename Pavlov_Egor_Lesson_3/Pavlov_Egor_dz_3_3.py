__author__ = 'Pavlov_Egor'


def thesaurus(some_tuple, key=False):
    if key:
        some_tuple = sorted(list(some_tuple))
    for name in some_tuple:
        dict_of_names.setdefault(name[0:1:], []).append(name)  # "setdefault" если нет ключа создается по первой букве,
        # в качестве элемента список, туда и складываем имена
    return dict_of_names


names = ('Петр', 'Илья', 'Мария', 'Иван')
#  names = input('Ввод с клавиатуры через ", ":').split(', ')  #  просто так. работает если выключить 13 строку
sort_key = bool(input('Сортировать список? Любое значение дает True: '))
dict_of_names = {}
thesaurus(names, sort_key)
print(f'Результат функции "thesaurus": {dict_of_names}')
print(f'Результат в виде оглавления:')
for keys in dict_of_names:
    print(keys)
    print(*dict_of_names[keys], sep=', ')  # об этой распаковке речь в задании?
#    print(*dict_of_names[keys], (print(*keys)), sep=', ')  # откуда "None"?
