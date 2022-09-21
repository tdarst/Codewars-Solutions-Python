def duplicate_count(t):
    z = 0
    t = t.lower()
    for x, y in enumerate(t):
        if t.count(y) > 1 and t.find(y) == x:
            z+=1
    return z