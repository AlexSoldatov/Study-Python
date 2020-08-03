def sum(a, b):
    if 1 <= b:
        a += 1
        b -= 1
        sum(a, b)
    else:
        print(a)


a = int(input())
b = int(input())
sum(a, b)
