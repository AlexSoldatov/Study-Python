def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n % m)


def ReduceFraction(n, m):
    x = gcd(n, m)
    p = n // x
    q = m // x
    return p, q


n = int(input())
m = int(input())
print(*ReduceFraction(n, m))
