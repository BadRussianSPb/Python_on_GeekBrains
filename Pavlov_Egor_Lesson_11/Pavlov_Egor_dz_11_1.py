class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Date:
    def __init__(self, some_data):
        self.date = str(some_data)

    @classmethod
    def str_to_date(cls, some_data):
        temp_list = str(some_data).split('-')  # извлекли
        try:
            if len(temp_list) != 3:
                raise MyError('Ошибка формата даты')
        except MyError as err:
            print(err)
            return None
        try:
            temp_dict = {'day': int(temp_list[0]),
                         'month': int(temp_list[1]),
                         'year': int(temp_list[2])}  # преобразовали
            return temp_dict  # в задании не ясно в каком виде возвращать
        except ValueError:
            print('Ошибка формата. Должно быть не пустое и число.')  # тут ловлю т.к. дальше код не сработает
            exit()

    @staticmethod
    def is_date(some_data):
        if Date.str_to_date(some_data) is None:
            return False
        temp_dict = Date.str_to_date(some_data)
        try:
            if len(str(temp_dict.get('year'))) != 4:
                raise MyError(f'Ошибка даты. Год = {temp_dict.get("year")}')
            elif 12 < temp_dict.get('month') or temp_dict.get('month') < 1:
                raise MyError(f'Ошибка даты. Месяц = {temp_dict.get("month")}')
            elif 31 < temp_dict.get('day') or temp_dict.get('day') < 1:
                raise MyError(f'Ошибка даты. День = {temp_dict.get("day")}')
        except MyError as err:
            print(err)
            return False
        return True


a = '27-16-1896-45'
# print(Date.str_to_date(a))
print(Date.is_date(a))
b = '27-01-1983'
print(Date.str_to_date(b))
print(Date.is_date(b))
c = '-2701-1983'
print(Date.str_to_date(c))
print(Date.is_date(c))
