n = int(input())
nSec = n % 60
nHour = n // 3600
nMin = (n % 3600) // 60
nMinS = str(nMin)
nSecS = str(nSec)
print(nHour, ":", '0' + nMinS, ':', '0' + nSecS, sep='')
