def has_subpattern(s):
    ns = ''
    pat = False
    for x in s:
        ns += x
        if s.count(ns) == 1:
            break
        elif len(s) / len(ns) == s.count(ns) and s.count(ns) > 1:
            pat = True
            break
    return pat