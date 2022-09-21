"""                                                                      Problem:

A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog"
is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

"""

"""                                                                      Solution:

Since we know that the alphabet is 26 letters, we know the set of a string containing all letters of the alphabet will have a length of 26. Normally you would just
create a set directly from the list bt this problem was giving numbers too to throw you off so I iterated through and checked if each character of the string was
a letter before adding it to the set. If the set has a length of 26 return True, else return False.

"""

import string

def is_pangram(s):
    s = s.lower()
    lSet = set()
    for x in range(0, len(s)):
        if s[x].isalpha():
            lSet.add(s[x])
    if len(lSet) == 26:
        return True
    else:
        return False
