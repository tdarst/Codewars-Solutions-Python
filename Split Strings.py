"""                                                                      Problem:

Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing
second character of the final pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']

"""

"""                                                                      Solution:

If the length of s is divisible by 2, append the characters of s as elements of w in pairs of 2. If the length of s is odd then append all of the characters except
for the last one as elements of w in pairs of two and then append the last character with an added '_'.

Return w

"""

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
