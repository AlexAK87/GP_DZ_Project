import random


class Matix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        result = ''

        for x in self.matrix:
            result = result + ' '.join(map(str, x)) + '\n'

        result = result + f'------------'

        return result

    def __add__(self, other):
        matrix_sum = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix[0])):
                try:
                    matrix_el_1 = other.matrix[i][j]
                except IndexError:
                    matrix_el_1 = 0

                row.append(self.matrix[i][j] + matrix_el_1)
            matrix_sum.append(row)

        return matrix_sum


matrix_list_1 = []
matrix_list_2 = []

len_matrix = 3

while len_matrix != 0:
    matrix_list_1.append(random.sample(range(1, 100), 5))
    matrix_list_2.append(random.sample(range(1, 100), 4))

    len_matrix -= 1

matrix_1 = Matix(matrix_list_1)
matrix_2 = Matix(matrix_list_2)

print(matrix_1)
print(matrix_2)


print(f'Сумма матриц: \n{Matix(matrix_1 + matrix_2)}')
