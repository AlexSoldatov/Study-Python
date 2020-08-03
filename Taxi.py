tar = sorted([int(s) for s in input().split()])
dist = sorted([int(s) for s in input().split()], reverse=True)
print(sum(t*d for t, d in zip(tar, dist)))
