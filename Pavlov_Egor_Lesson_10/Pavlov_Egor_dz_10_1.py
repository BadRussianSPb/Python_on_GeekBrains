import itertools


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        print(f'Матрица сформирована')
        for i in self.matrix:
            max_i = len(max(self.matrix, key=len))
            if len(i) < max_i:  # заполняем 0 пустые элементы в основном для новых матриц
                differ = max_i - len(i)
                while differ > 0:
                    i.append(0)
                    differ -= 1
            print('|', end='')
            for j in i:
                print(f'{j:4d} ', end='')
            print(str('|'))
        return str()

    def __add__(self, other):
        result_matrix = []
        for i_1, i_2 in itertools.zip_longest(self.matrix, other.matrix, fillvalue=[0]):
            temp_list = []
            for j in itertools.zip_longest(i_1, i_2, fillvalue=0):
                temp_list.append(sum(j))
            result_matrix.append(temp_list)
        return Matrix(result_matrix)


a = [[31, 22], [37, 43], [51, 68]]
b = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
c = [[3, 5, 8, 3], [8, 3, 7, 1]]
matrix_a = Matrix(a)
matrix_b = Matrix(b)
matrix_c = Matrix(c)
matrix_x = matrix_a + matrix_b + matrix_c
print(matrix_x)
