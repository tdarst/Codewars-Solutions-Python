def parts_sums(l):
    l = l[::-1]
    y = 0
    for x in range(0, len(l)):
        y+=l[x]
        l[x] = y
    l.insert(0,0)
    return l[::-1]