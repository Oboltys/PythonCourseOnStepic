a = float(input(''))
b = float(input(''))
c = input('')
if c == '/':
    if b == 0:
        print ('Деление на 0!')
    else:
        a=a/b
        print (a)  
elif c == 'mod':
    if b == 0:
        print ('Деление на 0!')
    else:
        a = a%b
        print (a)    
elif c == '+':
    a = a+b
    print (a)
elif c == '-':
    a = a-b
    print (a)
elif c == '*':
    a=a*b
    print (a)
elif c == 'pow':
    a = a**b
    print (a)
elif c == 'div':
    if b == 0:
        print ('Деление на 0!')
    else:
        a = a // b    
        print (a)