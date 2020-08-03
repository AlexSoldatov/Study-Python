land = {}
for i in range(int(input())):
    country, *cities = input().split()
    for city in cities:
        land[city] = country
for i in range((int(input()))):
    print(land[input()])
