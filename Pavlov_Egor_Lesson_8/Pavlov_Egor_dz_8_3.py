from functools import wraps


def log_wrapper(callback):
    @wraps(callback)
    def type_wrapper(*args):
        for el in args:
            print(f'{callback.__name__}({el} {type(el)})', end=', ')
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
y = 10

print(degry_of_x(x, y))
help(degry_of_x)
