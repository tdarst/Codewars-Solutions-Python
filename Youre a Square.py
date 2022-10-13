import math
def is_square(n):    
    return False if (n < 0) or (int(math.sqrt(n))**2 != n) else True