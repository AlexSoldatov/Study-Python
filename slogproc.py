import math
p = int(input())
x = int(input())
y = int(input())
k = int(input())
i = 1
sumKop = x * 100 + y
while i <= k:
    sumKop = (sumKop * p // 100) + sumKop
    i += 1
itogRub = sumKop // 100
itogKop = sumKop % 100
print(itogRub, itogKop)
