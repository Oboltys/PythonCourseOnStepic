a = int(input (''))
b = int(input (''))
kol = 0
s = 0
for i in range(a,b+1):
    del1 = i % 3
    if del1 == 0:
        s = s + i
        kol = kol+1
ar = s / kol
print (ar)