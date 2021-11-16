import sys
import json


def output(file_name, start_point, stop_point):
    with open(file_name, 'r', encoding='utf-8') as f:
        start_point, stop_point = int(start_point), int(stop_point)
        for i, el in enumerate(f, 1):
            if start_point <= i <= stop_point:
                tmp_dict = json.loads(el)
                print(tmp_dict)


if len(sys.argv) == 2:
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        count = 0
        for n, elem in enumerate(f, 1):
            count += 1
        sys.argv.append(str(count))
output('bakery.csv', *sys.argv[1:])
