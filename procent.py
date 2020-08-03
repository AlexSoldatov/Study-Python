import math
p = int(input())
x = int(input())
y = int(input())
sumKop = x * 100 + y
itog = sumKop * p // 100 + sumKop
itogRub = itog // 100
itogKop = itog % 100
print(itogRub, itogKop)
