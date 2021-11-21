import sys


def users_and_hobbys(users, hobbys, result):
    with open(users, 'r', encoding='utf-8') as f_users:
        with open(hobbys, 'a+', encoding='utf-8') as f_hobbys:
            count_for_user = 0
            count_for_hobby = 0
            for _ in enumerate(f_users):  # посчитал кол-во строк в пользователях
                count_for_user += 1
            f_hobbys.seek(0)
            for _ in enumerate(f_hobbys):  # посчитал кол-во строк в хобби
                count_for_hobby += 1
            if count_for_hobby < count_for_user:
                for i in range(count_for_user - count_for_hobby):
                    f_hobbys.write('None\n')  # добавил ноны в  хобби если их меньше
            f_hobbys.seek(0)  # вернул курсоры в начало
            f_users.seek(0)
            with open(result, 'w', encoding='utf_8') as f_result:  # записал в новый файл пары юзер-хобби
                for user, hobby, in zip(f_users, f_hobbys):
                    f_result.write(user[:len(user) - 1:])
                    f_result.write(': ')
                    f_result.write(hobby[:len(hobby) - 1:])
                    f_result.write('\n')


users_and_hobbys(*sys.argv[1:])
