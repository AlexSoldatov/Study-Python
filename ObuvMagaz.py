n = int(input())
a = list(map(int, input().split()))
new = 0
s = 0
a.sort()
for i in range(len(a)):
    if a[i] < n:
        continue
    elif a[i] == s:
        continue
    elif a[i] == n:
        new += 1
        s = a[i]
    elif a[i] - s >= 3:
        new += 1
        s = a[i]
print(new)
