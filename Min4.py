def minAll(a, b, c, d):
    min12 = min(a, b)
    min34 = min(c, d)
    minAll = min(min12, min34)
    return minAll
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(minAll(a, b, c, d))
