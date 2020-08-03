inFile = open('input.txt', 'r', encoding='utf8')
lines = inFile.readlines()
line = list(map(int, lines[0].split()))
n = line[0]
m = line[1]
ann = set()
bor = set()
ab = set()
ba = set()
for i in range(1, m + n + 1):
    if i <= n:
        line = lines[i].rstrip()
        line = int(line)
        ann.add(line)
    else:
        line = lines[i].rstrip()
        line = int(line)
        bor.add(line)

inters = sorted(ann & bor)
ab = sorted(ann.difference(bor))
ba = sorted(bor.difference(ann))
print(len(inters))
print(*inters)
print(len(ab))
print(*ab)
print(len(ba))
print(*ba)
