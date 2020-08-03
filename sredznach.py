n = int(input())
i = 1
sum = float(0.0)
med = float(0.0)
while n != 0:
    sum += n
    n = int(input())
    med = sum / i
    i += 1
print(med)
