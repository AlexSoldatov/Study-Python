a, b, c = float(input()), float(input()), float(input())
p = float((a + b + c) / 2)
s = (((p * (p - a)*(p - b)*(p - c)) ** 0.5))
print(s)
