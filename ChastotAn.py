text = dict()
fileIn = open('input.txt', 'r', encoding='utf-8')
a = fileIn.read().strip().split()
for n in a:
    text[n] = text.get(n, 0) + 1
fileIn.close()
for txt in sorted(sorted(text), key=text.get, reverse=True):
        print(txt)
