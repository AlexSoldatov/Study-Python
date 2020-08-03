def Intersection(a, b):
    c = list(sorted(set(a) & set(b), key=int))
    return c


a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*Intersection(a, b))
