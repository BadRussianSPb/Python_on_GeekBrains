__author__ = 'Pavlov_Egor'


def num_translate(some_word, some_dict):  # немного усложнил, зато работает для любого словаря. Получилось универсально
    if some_word.istitle() and some_dict.get(some_word.lower()):  # если первая буква заглавная и слово есть в словаре
        return some_dict.get(some_word.lower()).capitalize()  # нашли "уменьшеный" вариант и вернули "увеличеный"
    return some_dict.get(some_word)  # делаем через ".get" чтобы вернуть None если ничего не нашли


dict_numbers = {'zero': 'ноль', 'one': 'один',  # хранить словари в отдельном месте (файле) все же лучше чем в функции
                'two': 'два', 'three': 'три',
                'four': 'четыре', 'five': 'пять',
                'six': 'шесть', 'seven': 'семь',
                'eight': 'восемь', 'nine': 'девять'}

user_numb = input(f'Введите слово на английском языке для перевода: ')
print(num_translate(user_numb, dict_numbers))
