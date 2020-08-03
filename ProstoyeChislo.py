from math import sqrt
n = int(input())


def MinDivisor(n):
    i = 2
    while n % i != 0:
        i += 1
        if i > sqrt(n):
            return n
    return i


def IsPrime(n):
    return n // MinDivisor(n) == 1


print("YES" if IsPrime(n) else "NO")
