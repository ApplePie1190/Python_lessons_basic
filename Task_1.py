class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        result = ''
        for line in self.matrix:
            i = 0
            while i < len(line):
                result += f'{line[i]} '
                i += 1
            result += f'\n'
        return result

    def __add__(self, other):
        result = self.matrix.copy()
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                result[i][j] += other.matrix[i][j]
        return Matrix(result)


matrix_1 = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
matrix_2 = Matrix([[2, 1, 1], [1, 1, 1], [1, 1, 1]])

print(matrix_1)
print(matrix_2)
matrix_3 = matrix_1 + matrix_2
print(matrix_3)
