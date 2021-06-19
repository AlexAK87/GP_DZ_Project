class MyExceptions(Exception):
    def __init__(self, text):
        self.text = text


def computation(num_1, num_2):
    try:
        if num_2 > 0:
            result = num_1 / num_2
        else:
            raise MyExceptions('Операция деления на 0 запрещена')
    except ValueError:
        return "Error type of value!"
    except MyExceptions as mr:
        return mr
    else:
        return f'Результат: {result}'


print('Операция деления')
number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))

print(computation(number_1, number_2))
