s = input()
m = s.find('h') + 1
n = s.rfind('h')
p_m = s[:m]
p_n = s[n:]
p = s[m:n].replace('h', 'H')
print(p_m, p, p_n, sep='')
