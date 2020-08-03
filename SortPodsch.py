A = list(map(int, input().split()))
n = max(A)
B = [0] * (n + 1)


def CountSort(A):
    for i in A:
        B[i] = B[i] + 1
    for j in range(n + 1):
        print((str(j) + ' ') * B[j], end='')


CountSort(A)
