n = int(input())
i = 0
while n != 0:
    n = int(input())
    if n % 2 != 0:
        continue
    i += 1
    print(i)
print(i-1)
