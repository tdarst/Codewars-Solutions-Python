def wave(str):
    w = []
    for c in range(len(str)):
        if str[c] != ' ':
            w.append(str[0:c] + str[c:len(str)+1].capitalize())
    return w