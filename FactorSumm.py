import math
n = int(input())
s = 0
for i in range(0, n + 1):
    s += math.factorial(i)
print(s - 1)
