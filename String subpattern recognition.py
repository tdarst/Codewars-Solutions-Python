"""                                                                      Problem:

In this kata you need to build a function to return either true/True or false/False if a string can be seen as the repetition of a simpler/shorter subpattern or not.

For example:

hasSubpattern("a") == false; //no repeated pattern
hasSubpattern("aaaa") == true; //created repeating "a"
hasSubpattern("abcd") == false; //no repeated pattern
hasSubpattern("abababab") == true; //created repeating "ab"
hasSubpattern("ababababa") == false; //cannot be entirely reproduced repeating a pattern
Strings will never be empty and can be composed of any character (just consider upper- and lowercase letters as different entities) and can be pretty long (keep an eye 
on performances!).

"""

"""                                                                      Solution:

Accumulate the characters in passed-in string s on ns and each time this happens check and see if first, the accumulated characters can even possibly be a pattern,
and second if the subpattern length cleanly divides the length of the string while simultaneously being equivalent to the amount of times it appears in the passed-in
string (making sure that happens more than once). This sets up conditions for absolute certainty that the subpattern either exists or doesn't. If it is found to exist
or not for sure at any point the loop breaks and returns T or F accordingly.

"""

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
