def f(x):
    if x<=-2:
        x =1-((x+2)**2)
        return x
    elif x>-2 and x<=2:
        x =-(x/2)
        return x
    elif x>2:
        x =((x-2)**2)+1
        return x