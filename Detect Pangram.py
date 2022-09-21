import string

def is_pangram(s):
    s = s.lower()
    lSet = set()
    for x in range(0, len(s)):
        if s[x].isalpha():
            lSet.add(s[x])
    if len(lSet) == 26:
        return True
    elif len(lSet) != 26:
        return False