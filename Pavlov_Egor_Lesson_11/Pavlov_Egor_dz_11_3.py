class MyCheck(Exception):
    @staticmethod
    def add_to_list(some_data):
        if some_data == 'stop':
            print(f'Программа завершена. Рузультат ниже:')
            return False
        else:
            if some_data[0] == '-' or some_data[0] == '+' or some_data.isdigit():
                for i in range(1, len(some_data)):
                    if some_data[i].isdigit():
                        pass
                    else:
                        print('Ошибка! Нужно вводить число.')
                        return False
            else:
                print('Ошибка! Нужно вводить число.')
                return False
        return int(some_data)


result_list = []
a = input('Вводите только целые числа. Для основки введите "stop":\n')
try:
    if not MyCheck.add_to_list(a):
        raise MyCheck
except MyCheck:
    pass
else:
    result_list.append(int(a))
while a != 'stop':
    a = input('еще\n')
    try:
        if not MyCheck.add_to_list(a):
            raise MyCheck
    except MyCheck:
        pass
    else:
        result_list.append(int(a))
print(result_list)
