import re
import json

remote_addr = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} ')
request_datetime = re.compile(r'\s[-]\s[-]\s.(.+)[]]\s')  # r'\d{1,2}.\w+.\d{4}.\d{2}.\d{2}.\d{2}..\d{4}' первый вариант
request_type = re.compile(r'.\s.(\w{3,4})\s.')
requested_resource = re.compile(r'\s([/].+[/].+)["]\s\d{3}')
response_code = re.compile(r'.\s(\d{3})\s')
response_size = re.compile(r'\d{3}\s(\d+)\s')


count = 0
count_errors = 0
with open('nginx_logs.txt', 'r', encoding='utf-8') as f_source:
    with open('result.json', 'w+', encoding='utf-8') as f_result:
        with open('errors.json', 'w+', encoding='utf-8') as f_error:
            for line in f_source:
                count += 1
                try:
                    addr = remote_addr.findall(line)[0]
                    datetime = request_datetime.findall(line)[0]
                    req = request_type.findall(line)[0]
                    src = requested_resource.findall(line)[0]
                    code = response_code.findall(line)[0]
                    size = response_size.findall(line)[0]
                except IndexError:
                    print(f'Строка {count} не стандартная. Записана в {f_error.name}')
                    json.dump(count, f_error)
                    json.dump(line, f_error)
                    f_error.write('\n')
                    count_errors += 1
                    continue
                parsed_raw = addr, datetime, req, src, code, size
                json.dump(count, f_result)
                json.dump(parsed_raw, f_result)
                f_result.write('\n')
            print(f'Всего обработано строк {count}')
            print(f'Из них с ошибками {count_errors}')
