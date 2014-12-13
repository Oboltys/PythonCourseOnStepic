def modify_list(l):
    b = l
    i = 0
    while i <= len(l):
        if i < len(l):
            if l[i] % 2 == 0:
                b.insert(i, int(l[i]/2))
                b.remove(l[i+1])
                i += 1
            else:
                b.remove(l[i])
        else:
            break