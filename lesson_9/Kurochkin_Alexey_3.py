
class Worker:

    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = _income


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}, должность {self.position}'

    def get_total_income(self):
        total_income = 0
        for value in self.income.values():
            total_income += value

        return total_income


worker1 = Position('Петр', 'Петров', 'Программист', {"wage": 100000, "bonus": 50000})
worker2 = Position('Иван', 'Иванов', 'Дворник', {"wage": 50000, "bonus": 10000})

print(f'ФИО: {worker1.get_full_name()}')
print(f'Зарплата: {worker1.get_total_income()}')

print(f'ФИО: {worker2.get_full_name()}')
print(f'Зарплата: {worker2.get_total_income()}')