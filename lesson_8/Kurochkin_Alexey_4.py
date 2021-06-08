from functools import wraps


def val_checker(valide_number):
    def _val_checker(func):
        @wraps(func)
        def wrapper(*args):
            if valide_number(*args):
                result = func(*args)
                msg = result
            else:
                raise ValueError
            return msg

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    print(f"{calc_cube.__name__}('{x}: {type(x)}')")
    return x ** 3


input_number = int(input('Введит число для возведения в 3 степень: '))
print(calc_cube(input_number))
