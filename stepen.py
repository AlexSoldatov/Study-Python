n = int(input())
i = 1
while i <= n:
    if n != i:
        i = i * 2
    else:
        print('YES')
        break
else:
    print('NO')
