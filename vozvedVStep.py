def power(a, n):
    if n != 0:
        n -= 1
        if n <= 0:
            print(a)
            return
        a *= c
        power(a, n)
    else:
        print(1)


a = float(input())
n = int(input())
c = a
power(a, n)
