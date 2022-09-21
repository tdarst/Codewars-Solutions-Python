def unique_in_order(i):
    l = []
    for x in range(0, len(i)):
        if i[x] not in l or i[x-1] != i[x]:
            l.append(i[x])
    return l