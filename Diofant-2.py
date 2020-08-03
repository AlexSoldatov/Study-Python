a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
s = 0
for i in range(1001):
    if i != e:
        if a * i * i * i + b * i * i + c * i + d == 0:
            s += 1
print(s)
