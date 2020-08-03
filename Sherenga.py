a = [int(i) for i in input().split()]
x = int(input())
p = 0
while p < len(a) and a[p] >= x:
    p += 1
print(p + 1)
