#Step 1.4
t = input('')
if t == 'треугольник':
    a = int(input(''))
    b = int(input(''))
    c = int(input(''))
    p = float((a+b+c)/2)
    s = float ((p*(p-a)*(p-b)*(p-c))**0.5)
    print (s)
elif t == 'прямоугольник':
    a = int(input(''))
    b = int(input(''))
    s = float(a*b)
    print (s)
elif t == 'круг':
    r = int(input(''))
    s = float(3.14 * (r**2))
    print (s)
