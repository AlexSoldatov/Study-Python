fin = open('input.txt', 'r', encoding='utf-8')
bal9, bal10, bal11 = [], [], []
for line in fin:
    if int(line.split()[2]) == 9:
        bal9.append(int(line.split()[3]))
    elif int(line.split()[2]) == 10:
        bal10.append(int(line.split()[3]))
    else:
        bal11.append(int(line.split()[3]))
print(sum(bal9) / len(bal9), sum(bal10) / len(bal10), sum(bal11) / len(bal11))
