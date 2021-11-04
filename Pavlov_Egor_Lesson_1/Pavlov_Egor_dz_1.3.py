__author__ = 'Pavlov_Egor'

for i in range(1, 101):
    if i != 11 and i % 10 == 1:
        print(f'{i} процент')
    elif (12 != i and i % 10 == 2) or (13 != i and i % 10 == 3) or (14 != i and i % 10 == 4):
        print(f'{i} процента')
    else:
        print(f'{i} процентов')
