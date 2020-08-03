dic = dict()
with open('input.txt', 'r') as fileIn:
    for line in fileIn:
        for line in line.strip().split():
            dic[line] = dic.get(line, -1) + 1
            print(dic[line], end=' ')
