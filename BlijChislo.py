N = input()
num = list(map(int, input().strip().split()))
x = int(input().strip())
res = num[0]
for i in num:
    if abs(i - x) < abs(res - x):
        res = i
print(res)
