"""                                                                      Problem:

Story
The Pied Piper has been enlisted to play his magical tune and coax all the rats out of town.

But some of the rats are deaf and are going the wrong way!

Kata Task
How many deaf rats are there?

Legend
P = The Pied Piper
O~ = Rat going left
~O = Rat going right
Example
ex1 ~O~O~O~O P has 0 deaf rats

ex2 P O~ O~ ~O O~ has 1 deaf rat

ex3 ~O~O~O~OP~O~OO~ has 2 deaf rats

"""

"""                                                                      Solution:

Split the string into two by the location of the piper and then delete the whitespace in each seperated string. Loop through and search for all rats facing each other
and replace them with a rat going the correct direction and then loop through again to clean up the remaining tails. Check if the piper is at the beginning or the end
of the string before returning the total length divided by two giving the amount of rats that weren't facing the correct direction (the "deaf rats")

This was a rather unelegant solution which I found out after could be solved in one line.

def count_deaf_rats(town):
    return town.replace(' ', '')[::2].count('O')
    
Which is the beneficial part of viewing other solution submissions post-solve.

"""
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
