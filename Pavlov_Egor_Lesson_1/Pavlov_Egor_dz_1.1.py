__author__ = 'Pavlov_Egor'

duration = int(input('Введите кол-во секунд (duration): '))
day_in_dur = duration // (24*60*60)
hr_in_dur = duration // (60 * 60) - day_in_dur * 24
min_in_dur = duration // 60 - hr_in_dur * 60 - day_in_dur * 24 * 60
sec_in_dur = duration % 60

print(f'\nВ {duration} секундах ', end='')
if day_in_dur == 0:
    if hr_in_dur == 0:
        if min_in_dur == 0:
            if sec_in_dur < 0:
                print('Duration не указано')
            else:
                print(f'{duration} сек')
        else:
            print(f'{min_in_dur} мин {sec_in_dur} сек')
    else:
        print(f'{hr_in_dur} час {min_in_dur} мин {sec_in_dur} сек')
else:
    print(f'{day_in_dur} дн {hr_in_dur} час {min_in_dur} мин {sec_in_dur} сек')
