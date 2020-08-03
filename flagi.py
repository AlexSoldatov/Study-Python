n = int(input())
i = 0
for i in range(n):
    print('+___', sep='', end=' ')
print()

for i in range(n):
    print('|', i + 1, ' /', sep='', end=' ')
print()

for i in range(n):
    print('|', "__", '\\', sep='', end=' ')
print()

for i in range(n):
    print('|   ', sep='', end=' ')
print()
