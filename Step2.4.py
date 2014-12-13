#GC-sostav
a = input ('')
a.lower()
A = a.lower().count('a'.lower())
G = a.lower().count('g'.lower())
T = a.lower().count('t'.lower())
C = a.lower().count('c'.lower())
if (A+T+G+C)!= 0:
    gc = (G+C)/(A+T+G+C)*100
    print (gc)
