n, x, = int(input()), float(input())
a = float(input())
result = 0
i = n
while i > 0:
    result += a
    result *= x
    i -= 1
    a = float(input())
result += a
print('{0:.2f}'.format(result))
