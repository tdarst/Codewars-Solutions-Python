"""                                                                      Problem:

Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced.
The input will be a non-negative integer.

Examples
    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2

"""

"""                                                                      Solution:

Turn passed-in int into string so each number in it can be seperately worked with. For each element of the string version accumulate it's integer value to c
and then repeat recursively until only a single digit number remains, return that number.

"""

def digital_root(n):
    c = 0
    for x in str(n):
        c += int(x)
    if c >= 10:
        return digital_root(c)
    else:
        return c
