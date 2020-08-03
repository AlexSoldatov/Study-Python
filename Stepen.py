def stepen(a, n):
    if n == 0:
        avn = 1
        return avn
    if n % 2 != 0 and n > 1:
        avn = a * stepen(a, n - 1)
        return avn
    if n % 2 == 0 and n > 1:
        avn = 1 * stepen(a * a, n / 2)
        return avn
    if n == 1:
        avn = a
        return avn


a = float(input())
n = int(input())
print(stepen(a, n))
