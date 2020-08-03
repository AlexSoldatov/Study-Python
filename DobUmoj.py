from sys import stdin
import copy


class Matrix():
    def __init__(self, matrix):
        self.matrix = copy.deepcopy(matrix)

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, list)) for list in self.matrix])

    def size(self):
        return (len(self.matrix), len(self.matrix[0]))

    def __add__(self, other):
        return Matrix(list(map(
            lambda x, y: list(map(lambda z, w: z + w, x, y)),
            self.matrix, other.matrix)))

    def __mul__(self, other):
        return Matrix([[i * other for i in list] for list in self.matrix])

    __rmul__ = __mul__

exec(stdin.read())
