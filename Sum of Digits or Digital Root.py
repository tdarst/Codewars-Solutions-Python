def digital_root(n):
    c = 0
    for x in str(n):
        c += int(x)
    if c >= 10:
        return digital_root(c)
    else:
        return c