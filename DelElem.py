numList = list(map(int, input().split()))
k = int(input())
for i in range(k, len(numList) - 1):
    numList[i] = numList[i + 1]
numList.pop()
print(*numList)
