import sys


class MyExceptions(Exception):
    def __init__(self, text):
        self.text = text

    def my_fun(self):
        return False
        pass