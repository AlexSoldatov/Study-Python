from collections import defaultdict
inFile = open('input.txt', 'r', encoding='utf8')
clients = defaultdict(lambda: defaultdict(int))
for line in inFile.readlines():
    client, thing, value = line.split()
    clients[client][thing] += int(value)
for client in sorted(clients):
    print(client + ':')
    for thing in sorted(clients[client]):
        print(thing, clients[client][thing])
inFile.close()
