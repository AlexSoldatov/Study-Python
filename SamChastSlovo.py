text = dict()
fileIn = open('input.txt', 'r', encoding='utf-8')
a = fileIn.read().strip().split()
for n in a:
    text[n] = text.get(n, 0) + 1
print(max(sorted(text.keys()), key=lambda x: text[x]))
fileIn.close()
