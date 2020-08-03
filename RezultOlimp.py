class Man:
    ball = 0
    name = ''


def manKey(man):
    return (-man.ball, man.name)


n = int(input())
peopleList = []
for i in range(n):
    tempManData = input().split()
    man = Man()
    man.name = tempManData[0]
    man.ball = int(tempManData[1])
    peopleList.append(man)
peopleList.sort(key=manKey)
for man in peopleList:
    print(man.name)
