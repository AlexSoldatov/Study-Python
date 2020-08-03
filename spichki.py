l1 = int(input())
r1 = int(input())
l2 = int(input())
r2 = int(input())
l3 = int(input())
r3 = int(input())
if (l1 >= 0) and (l1 < r1) and (r1 <= 100) and \
        (l2 >= 0) and (l2 < r2) and (r2 <= 100) and \
        (l3 >= 0) and (l3 < r3) and (r3 <= 100):
    if ((l2 - r1) <= 1) and ((l3 - r2) > 1) and (l1 < l2) and \
            (l2 < r3) and (l1 < r3):
        print(3)
    elif ((l2 - r1) > 1) and ((l3 - r2) > 1) and (l2 - r1) <= (r3 - l3):
        print(3)
    elif ((l2 - r1) > 1) and ((l3 - r2) <= 1):
        print(1)
    elif ((l2 - r1) <= 1) and (((l3 - r2) <= 1) or ((l3 - r1) <= 1)):
        print(0)
    else:
        print(-1)
else:
    print(-1)
