x1 = int(input())
y1 = int(input())
z21 = int(input())
x2 = int(input())
y2 = int(input())
z2 = int(input())
d1 = (x1 // x2) * (y1 // y2) * (z21 // z2)
d2 = (x1 // x2) * (z21 // y2) * (y1 // z2)
d3 = (y1 // x2) * (z21 // y2) * (x1 // z2)
d4 = (y1 // x2) * (x1 // y2) * (z21 // z2)
d5 = (z21 // x2) * (x1 // y2) * (y1 // z2)
d6 = (z21 // x2) * (y1 // y2) * (x1 // z2)
if d1 >= d2:
    d2 = d1
if d3 >= d4:
    d4 = d2
if d5 >= d6:
    d6 = d5
if d2 >= d4 and d2 >= d6:
    print(d2)
elif d4 >= d6:
    print(d4)
else:
    print(d6)
