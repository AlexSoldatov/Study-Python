from math import sqrt

a = float(input())
b = float(input())
c = float(input())
D = (b ** 2) - (4 * a * c)
if D > 0 and a != 0 and b != 0:
    x1 = ((-b) + sqrt(D)) / (2 * a)
    x2 = ((-b) - sqrt(D)) / (2 * a)
    if x1 > x2:
        print('{0:.6}'.format(x2), '{0:.6}'.format(x1))
    else:
        print('{0:.6}'.format(x1), '{0:.6}'.format(x2))
elif D == 0 and a != 0 and b != 0:
    x1 = -(b / (2 * a))
    print('{0:.6}'.format(x1))
elif b == 0 and (-(c / a)) > 0:
    x1 = sqrt(-(c / a))
    x2 = -x1
    if x1 > x2:
        print('{0:.6}'.format(x2), '{0:.6}'.format(x1))
    else:
        print('{0:.6}'.format(x1), '{0:.6}'.format(x2))
elif c == 0:
    x1 = 0
    x2 = -(b / a)
    if x1 > x2:
        print('{0:.6}'.format(x2), x1)
    else:
        print(x1, '{0:.6}'.format(x2))
elif b == 0 and c == 0:
    x1 = 0
    x2 = 0
    print('{0:.6}'.format(x1), '{0:.6}'.format(x2))
