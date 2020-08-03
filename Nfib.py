a = int(input())
if a == 0:
    print(0)
else:
    prev, next = 0, 1
    n = 1
    while next <= a:
        if next == a:
            print(n)
            break
        prev, next = next, prev + next
        n += 1
    else:
        print(-1)
