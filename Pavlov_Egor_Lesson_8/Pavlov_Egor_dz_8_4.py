from functools import wraps


def log_wrapper(callback):
    @wraps(callback)
    def type_wrapper(*args):
        for el in args:
            print(f'{callback.__name__}({el} {type(el)})', end=', ')
            try:
                if type(el) != int or el < 0:
                    raise ValueError
            except ValueError:
                exit(ValueError(f'\n{callback.__name__} хочет работать с целыми положительными числами. Подано {el}'))
        print()
        result = callback(*args)
        return result

    return type_wrapper


@log_wrapper
def degry_of_x(x, y):
    """Проерка на маскировку"""
    result = x ** y
    return result


x = 2
y = 'ds'

print(degry_of_x(x, y))
help(degry_of_x)
