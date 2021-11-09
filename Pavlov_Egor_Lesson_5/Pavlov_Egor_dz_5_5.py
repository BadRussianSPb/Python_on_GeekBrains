__author__ = 'Pavlov_Egor'

from time import perf_counter

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]  # почему такое название у списков? source?

start1 = perf_counter()
result1 = []
for el in src:
    if src.count(el) == 1:
        result1.append(el)
print(result1, perf_counter() - start1, 'Способ №1 Обычный цикл с новым списком')

start2 = perf_counter()
result2 = [el for el in src if src.count(el) == 1]
print(result2, perf_counter() - start2, 'Способ №2 List Comprehensions с новым списком')

start3 = perf_counter()
print([el for el in src if src.count(el) == 1], perf_counter() - start3, 'Способ №3 List Comprehensions без списка')
