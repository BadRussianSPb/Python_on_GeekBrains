import os
from shutil import copy2

root = '.\\my_project'
#  files = str(input('Введите путь до папки сканирования: '))


templates_path = os.path.join(root, 'templates')
for roots, dirs, files in os.walk(root):
    for dir in dirs:
        if str(dir) == 'templates':
            #            if str(roots) != root:  # это если в 15 строке будет exist_ok = True без обработки исключений
            new_dir = os.path.join(templates_path, (roots.split('\\')[-1]))  # папка копий
            print(new_dir)
            try:
                os.makedirs(new_dir)
            except FileExistsError as e:
                print('Директория существует')
                exit()
            new_path = os.path.join(roots, dir, roots.split('\\')[-1])
            for roots2, dirs2, files2 in os.walk(new_path):
                for file in files2:
                    copy2(os.path.join(new_path, str(file)), new_dir)
