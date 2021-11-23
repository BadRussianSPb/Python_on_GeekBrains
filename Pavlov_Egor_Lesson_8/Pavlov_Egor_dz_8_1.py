import re
import sys

RE_EMAIL_find = re.compile(r'(\w+\@\w+\.\w{2,3}){1}')  # проблема c разной длинной ru, com и т.п.


def email_parse(email_address):
    try:
        email = RE_EMAIL_find.findall(email_address)[0]
    except (IndexError, TypeError) as e:
        print(f'wrong email: {email_address}')
        exit(e)
    result_dict.setdefault('username', re.split(f'\@', email)[0])
    result_dict.setdefault('domain', re.split(f'\@', email)[1])
    return result_dict


email = 'e9118116464@gmail.com'
result_dict = {}
#print(email_parse(email))
print(email_parse(sys.argv[1]))
