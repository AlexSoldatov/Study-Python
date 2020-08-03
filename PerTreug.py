import math


def dis(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
print(dis(x1, y1, x2, y2) + dis(x2, y2, x3, y3) + dis(x3, y3, x1, y1))
