n = int(input())
print('+___ ' * n)
for m in range(1, n + 1):
    print(f'|{m} / ', end='')
print('\n' + '|__\\ ' * n + '\n' + '|    ' * n)
