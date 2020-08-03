sn = list(map(int, input().split()))
s = sn[0]
n = sn[1]
t = []
numUser = 0
sumUser = 0
pukUser = 0
while numUser < n:
    vUser = int(input())
    numUser += 1
    t.append(vUser)
t.sort()
for i in t:
    if sumUser < s:
        sumUser += i
        if sumUser < s:
            pukUser += 1
print(pukUser)
