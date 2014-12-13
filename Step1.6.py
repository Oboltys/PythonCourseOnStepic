a = input('')
b = len(a)
c = int(a[b-1])
if c == 2 or c == 3 or c == 4:
    if int(a) == 12 or int(a) == 13 or int(a) == 14 or int(a) == 112 or int(a) == 113 or int(a) == 114 or int(a) == 212 or int(a) == 213 or int(a) == 214:
        print (a, ' программистов')
    else:
        print (a, ' программиста')
elif c == 5 or c == 0 or c == 6 or c == 7 or c == 8 or c == 9 or int(a) == 11 or int(a) == 12 or int(a) == 13 or int(a) == 14 or int(a)== 111:
    print (a,' программистов')
elif (c == 1 and (not int(a) =='11' or int(a) == '111' )):
    print (a + ' программист')
