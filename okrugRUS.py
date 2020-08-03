import math
n = float(input())
if int((n % 1) * 10) >= 5:
    print(math.ceil(n))
else:
    print(math.floor(n))
