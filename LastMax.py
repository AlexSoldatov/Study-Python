lst = list(map(int, input().split()))
mv = lst[0]
mi = 0
for i, v in enumerate(lst):
    if v >= mv:
        mi = i
        mv = v
print(mv, mi)
