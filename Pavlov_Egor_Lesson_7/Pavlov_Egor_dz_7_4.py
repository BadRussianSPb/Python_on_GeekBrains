import os

files = '.\some_data'
#files = str(input('Введите путь до папки сканирования: '))


def create_dict(file, value):
    if file.stat()[6] < value:
        result_dict.update({value: result_dict.setdefault(value, 0) + 1})
    else:
        create_dict(file, value * 10)  # моя первая работающия рекурсия !!!


result_dict = {}
temp_list = []

for roots, dirs, files in os.walk(files):
    for item in os.scandir(roots):
        if item.is_file():
            create_dict(item, 100)
temp_list = sorted(result_dict.items(), key=lambda x: x[0])  # можно и посортировать, а можно изначально задать
result_dict = dict(temp_list)
print(result_dict)
