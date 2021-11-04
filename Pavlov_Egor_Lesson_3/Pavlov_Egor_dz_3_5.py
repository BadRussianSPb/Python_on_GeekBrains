__author__ = 'Pavlov_Egor'
import random


def get_jokes(list_1, list_2, list_3, flag1=False):
    """
    Returns a list of jokes consisting of the elements of the lists.
    The number of jokes is equal to the minimum list.
    :param list_1:
    :param list_2:
    :param list_3:
    :param flag1: By default, words are repeated.
    :return: list
    """

    if flag1:
        for el in range(min(len(list_1), len(list_2), len(list_3))):  # кол-во шуток по самом короткому списку
            pop_el_1 = list_1.pop(list_1.index(random.choice(list_1)))  # выбрали случ элемент,получили индекс и попнули
            pop_el_2 = list_2.pop(list_2.index(random.choice(list_2)))
            pop_el_3 = list_3.pop(list_3.index(random.choice(list_3)))
            list_of_jokes.append([pop_el_1, pop_el_2, pop_el_3])
    else:
        for el_1, el_2, el_3 in zip(list_1, list_2, list_3):  # а как без el_*?
            list_of_jokes.append([random.choice(list_1), random.choice(list_2), random.choice(list_3)])
    return list_of_jokes


nouns = ['автомобиль', 'лес', 'огонь', 'город', 'дом', 'мяч']
adverbs = ['сегодня', 'вчера', 'завтра', 'позавчера', 'ночью', 'в среду']
adjectives = ['веселый', 'яркий', 'зеленый', 'утопичный', 'мягкий', 'огромный']

list_of_jokes = []
repetitions = bool(input('Избегать повторы в шутках? Любое значение дает True:'))
get_jokes(nouns, adverbs, adjectives, flag1=repetitions)
for joke in list_of_jokes:
    print(*joke)
