__author__ = 'Pavlov_Egor'

from time import perf_counter

result = []
count = 0

with open('nginx_logs.txt', 'r', encoding='utf-8') as f_1:
    for el in f_1:
        result.append((el.split(' ')[0], el.split(' ')[5][1::], el.split(' ')[6]))  # кортеж из нужных элементов
        # добавил в результирующий список

start = perf_counter()
ip_count_dict = {}

for el in result:
    ip_count_dict.setdefault(el[0], 0)
for el in result:
    ip_count_dict.update({el[0]: ip_count_dict.get(el[0]) + 1})
max_value = max(ip_count_dict.values())
final_result = ({key: value for key, value in ip_count_dict.items() if value == max_value})
print(final_result, perf_counter() - start)

# ---------------------------------------------------------------------------------------------------------------------

start = perf_counter()
ip_count_dict = {}

for el in result:
    if el[0] in ip_count_dict:
        ip_count_dict.update({el[0]: ip_count_dict.get(el[0]) + 1})
    else:
        ip_count_dict.setdefault(el[0], 1)
max_value = max(ip_count_dict.values())
final_result = ({key: value for key, value in ip_count_dict.items() if value == max_value})
print(final_result, perf_counter() - start)
