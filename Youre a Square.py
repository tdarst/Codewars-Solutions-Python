"""                                                                      Problem:

Given an integral number, determine if it's a square number:

"""

"""                                                                      Solution:

Yay for short-circuit evaluation! Simply check if n is less than 0 or if (n's rounded-down square)^2 == n to determine if it is a perfect square or not.

"""

import math
def is_square(n):    
    return False if (n < 0) or (int(math.sqrt(n))**2 != n) else True
