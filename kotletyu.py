k = int(input())  # Вместимость сковородки
n = int(input())  # Количество котлет
m = int(input())  # время обжарки одной стороны
if n <= k:
    print(2 * m)
elif n * 2 % k != 0:
    print(m * (n * 2 // k))
else:
    print(m * (n * 2 // k +1))
