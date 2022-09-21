def xo(s):
    s = s.lower()
    if s.count('x') - s.count('o') == 0:
        return True
    else:
        return False