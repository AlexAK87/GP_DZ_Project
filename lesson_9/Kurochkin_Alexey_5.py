class Stationery:

    def __init__(self, title=''):
        self.title = title

    def draw(self):
        return 'Запуск отрисовки'


class Pen(Stationery):

    def draw(self):
        return f'Класс Pen. {self.title}'


class Pencil(Stationery):

    def draw(self):
        return f'Класс Pencil. {self.title}'


class Handle(Stationery):

    def draw(self):
        return f'Класс Handle. {self.title}'


s = Stationery()
p = Pen('Гелевая ручка')
p1 = Pencil('Цветной карандаш')
h = Handle('Черный маркер')

print(s.draw())
print(p.draw())
print(p1.draw())
print(h.draw())
