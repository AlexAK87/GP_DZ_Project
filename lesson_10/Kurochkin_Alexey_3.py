class Cell:
    def __init__(self, num_cells):
        self.num_cells = num_cells

    def __add__(self, other):
        return self.num_cells + other.num_cells

    def __sub__(self, other):
        result = self.num_cells - other.num_cells
        if result < 0:
            result = 'Результат меньше 0'

        return result

    def __mul__(self, other):
        return self.num_cells * other.num_cells

    def __truediv__(self, other):
        try:
            result = self.num_cells / other.num_cells
            if result % 2 != 0:
                result = 0

            return int(result)
        except ZeroDivisionError as e:
            return e

    def make_order(self, row):
        row_cell = ''
        while self.num_cells > row:
            row_cell = row_cell + '*' * row + '\n'
            self.num_cells -= row
        else:
            row_cell = row_cell + '*' * self.num_cells + '\n'

        return row_cell


cell_1 = Cell(12)
cell_2 = Cell(10)

print(f'Сложение: {cell_1 + cell_2}')
print(f'Вычитание: {cell_1 - cell_2}')
print(f'Умнажение: {cell_1 * cell_2}')
print(f'Деление: {cell_1 / cell_2}')

print(Cell.make_order(cell_2, 3))
