pSum = 0
pSumSqa = 0
x = int(input())
n = 0
while x != 0:
    n += 1
    pSum += x
    pSumSqa += x ** 2
    x = int(input())
print(((pSumSqa - pSum ** 2 / n) / (n - 1)) ** 0.5)
