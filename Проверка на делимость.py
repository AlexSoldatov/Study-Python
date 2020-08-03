a = int(input())
b = int(input())
print(('NO' * (a % b)), ('YES' * (1 - (a % b))), sep='')