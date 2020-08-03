inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
canString = inFile.readlines()
canList = []
for cand in canString:
    canSp = cand.strip()
    canList.append(canSp)
allVot = len(canList)
canDict = {}
for can in canList:
    canDict[can] = canDict.get(can, 0) + 1
canDict = [(vot, cn) for cn, vot in canDict.items()]
canDict.sort(key=lambda x: x[0], reverse=True)
if canDict[0][0] > (allVot // 2):
    print(canDict[0][1], file=outFile)
else:
    print(canDict[0][1], canDict[1][1], sep="\n", file=outFile)
inFile.close()
outFile.close()
