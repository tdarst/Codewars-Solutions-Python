def solution(s):
    w = []
    if len(s) % 2 == 0:
        for c in range(0,len(s),2):
            w.append(s[c:c+2])
    else:
        for c in range(0, len(s)-1, 2):
            w.append(s[c:c+2])
        w.append(s[len(s)-1] + '_')
    return w