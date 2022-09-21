def count_deaf_rats(t):
    print(t)
    t = t.split('P')
    ls = t[0].replace(' ','')
    rs = t[1].replace(' ','')
    while 'OO' in ls or 'OO' in rs:
        ls = ls.replace('~OO~', 'O~')
        rs = rs.replace('~OO~', '~O')
    while '~~' in ls or '~~' in rs:
        ls = ls.replace('O~~O', 'O~')
        rs = rs.replace('O~~O', '~O')
    if len(ls) == len(t[0].replace(' ','')) and ls != "O~":
        ls = ''
    if len(rs) == len(t[1].replace(' ','')) and rs != "~O":
        rs = ''
    return int(len(ls)/2 + len(rs)/2)