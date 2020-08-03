n = int(input())
all = set(range(1, n + 1))
while True:
    quest = input()
    if quest == 'HELP':
        break
    quest = {int(x) for x in quest.split()}
    answer = input()
    if answer == 'YES':
        all &= quest
    if answer == 'NO':
        all -= quest
print(' '.join([str(x) for x in sorted(all)]))
