a = [int(s) for s in input().split()]
iMin = 0
iMax = 0
for i in range(1, len(a)):
    if a[i] > a[iMax]:
        iMax = i
    if a[i] < a[iMin]:
        iMin = i
a[iMin], a[iMax] = a[iMax], a[iMin]
print(' '.join([str(i) for i in a]))
