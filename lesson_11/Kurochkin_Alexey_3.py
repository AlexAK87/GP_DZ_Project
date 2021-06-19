import sys


class MyExceptions(Exception):
    def __init__(self, text):
        self.text = text


number_list = []


def get_number(num):
    try:
        if type(num) == int():
            number_list.append(num)
        else:
            print(number_list)
            raise MyExceptions('Программа работает только с целыми цифрами')

    except ValueError:
        return "Error type of value!"
    except MyExceptions as mr:
        return mr
    else:
        return f'Результат: {result}'



