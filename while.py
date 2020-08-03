inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
lines = inFile.readlines()
list1 = []

for line in lines:
    surname, name, grade, score = line.strip().split(' ', maxsplit=4)
    list1.append((surname, name, score))


def surname(elem):
    return elem[0]


sortedList = sorted(list1, key=surname)
#  print(list1, file=outFile)
for i in range(len(list1)):
    #  sortedList = sorted(list1, key=surname(i))
    print(*sortedList[i], file=outFile)

inFile.close()
outFile.close()

