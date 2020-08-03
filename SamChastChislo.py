l = [int(i) for i in input().split()]
print(max(l, key=l.count))
