from sys import stdin
import copy


class Matrix():
    def __init__(self, matrix):
        self.matrix = copy.deepcopy(matrix)

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, list)) for list in self.matrix])

    def size(self):
        return (len(self.matrix), len(self.matrix[0]))

exec(stdin.read())
