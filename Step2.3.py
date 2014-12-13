a = int (input(''))
b = int (input(''))
c = int (input(''))
d = int (input(''))
for i in range(c, d+1):
    print('\t',i,end='')
for k in range (a, b+1):
    print('')
    print (k,end='\t')
    for m in range (c, d+1):
        h = k * m
        print (h, end='\t')
