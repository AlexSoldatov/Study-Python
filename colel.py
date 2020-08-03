p = int(input())
m = 0
i = 0
while p != 0:
    n = int(input())
    if n != 0 and p < n:
        i += 1
    p = n
print(i)
