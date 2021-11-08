__author__ = 'Pavlov_Egor'

import Utils
import sys
import time

for arg in sys.argv[1:]:
    start_time = time.time()
    if Utils.cureency_rates_str(arg) is None:
        print(None)
    else:
        print(*Utils.cureency_rates_str(arg), ''.ljust(4), 'STR Функция'.ljust(15), (time.time() - start_time), "s")
    start_time = time.time()
    if Utils.cureency_rates_bs4(arg) is None:
        print(None)
    else:
        print(*Utils.cureency_rates_bs4(arg), ''.ljust(4), 'BS4 Функция'.ljust(15), (time.time() - start_time), "s")
