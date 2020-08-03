inFile = open('input.txt', 'r', encoding='utf8')
for line in inFile:
    bus1Beg, bus1End, bus2Beg, bus2End = line.strip().split(' ')
    bus1Beg = int(bus1Beg)
    bus1End = int(bus1End)
    bus2Beg = int(bus2Beg)
    bus2End = int(bus2End)
inFile.close()


def BusRange(beg, end):
    rangeBus = list()
    if beg > end:
        beg, end = end, beg
    busTemp = beg
    while end >= busTemp:
        rangeBus.append(busTemp)
        busTemp += 1
    return rangeBus
print(len(set(BusRange(bus1Beg, bus1End)) & (set(BusRange(bus2Beg, bus2End)))))
