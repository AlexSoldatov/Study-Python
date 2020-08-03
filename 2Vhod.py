s = input()
pos = s.find('f')
if pos == -1:
    print('-2')
else:
    print(s.find('f', pos + 1))
