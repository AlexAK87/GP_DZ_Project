from functools import wraps


def type_logger(func):
    log = {}

    @wraps(func)
    def wrapper(*nums):
        nonlocal log
        result = []
        for i in nums:
            key = type(i)
            if key not in log:
                log[key] = func(i)
            result.append(log[key])

        return result

    return wrapper


@type_logger
def calc_cube(*nums):
    result = []

    for i in nums:
        result.append(i ** 3)

        print(f"{calc_cube.__name__}('{i}: {type(i)}')")

    return result


number_cub1 = calc_cube(5, 6, 2.3)
print(number_cub1)
