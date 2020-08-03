from sys import stdin
import copy


class MatrixError(BaseException):
    def __init__(self, matrix, other):
        self.matrix1 = matrix
        self.matrix2 = other


class Matrix():
    def __init__(self, matrix):
        self.matrix = copy.deepcopy(matrix)

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, list)) for list in self.matrix])

    def size(self):
        return (len(self.matrix), len(self.matrix[0]))

    def __add__(self, other):
        if len(self.matrix) == len(other.matrix):
            lenght = len(self.matrix[0])
            for row in self.matrix:
                if len(row) != lenght:
                    raise MatrixError(self, other)
            for row2 in other.matrix:
                if len(row2) != lenght:
                    raise MatrixError(self, other)
            result = []
            numbers = []
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    summ = other.matrix[i][j] + self.matrix[i][j]
                    numbers.append(summ)
                    if len(numbers) == len(self.matrix[0]):
                        result.append(numbers)
                        numbers = []
            return Matrix(result)
        else:
            raise MatrixError(self, other)

    def __mul__(self, other):
        return Matrix([[i * other for i in list] for list in self.matrix])

    __rmul__ = __mul__

    def transpose(self):
        transMatrix = list(zip(*self.matrix))
        self.matrix = transMatrix
        return Matrix(transMatrix)

    def transposed(self):
        transMatrix = list(zip(*self.matrix))
        return Matrix(transMatrix)


exec(stdin.read())
