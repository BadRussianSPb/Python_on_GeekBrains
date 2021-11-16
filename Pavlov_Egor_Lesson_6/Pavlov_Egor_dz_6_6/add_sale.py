import sys
import json


def add_sale(name_of_file, sales):
    with open(name_of_file, 'r', encoding='utf-8') as f:
        count_of_str = 0
        for _ in enumerate(f):
            count_of_str += 1
        tmp_dict = {count_of_str + 1: sales}
    with open(name_of_file, 'a', encoding='utf-8') as f:
        json.dump(tmp_dict, fp=f)
        f.write('\n')


add_sale('bakery.csv', *sys.argv[1:])
