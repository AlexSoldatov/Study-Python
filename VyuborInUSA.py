d = {}
with open('input.txt') as fileIn:
    for line in fileIn:
        k, v = line.strip().split()
        d.setdefault(k, 0)
        d[k] += int(v)
    for i in sorted(d.items()):
        print(*i)
