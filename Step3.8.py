b = []
a = int(input(''))
i = 0
if a == 1:
    print (a)
    if a == 2:
        print ('1,2')
else:
    for i in range(a):    
        for k in range(i):
            b.append(i)
    for i in range(a):
        print (b[i], end=' ')