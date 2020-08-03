a = [int(i) for i in input().split()]
N = 1
for i in range(0, len(a) - 1):
    if a[i] != a[i + 1]:
        N += 1
print(N)
