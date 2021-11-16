__author__ = 'Pavlov_Egor'

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Мрак', 'Егор', 'Борис']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

[klasses.append(None) for el in range(len(tutors) - len(klasses)) if len(tutors) - len(klasses) > 0]  # работает  8-О
tuple_in_gen = ((el1, el2) for el1, el2 in zip(tutors, klasses))  # без вторых () не работает, хотя c yield не нужны
print(type(tuple_in_gen))
for elem in tuple_in_gen:  # print(*tuple_in_gen) можно, но сделал вывод как в задании. в 1 строку врятли получится?
    print(elem)
