
"""                                                                      Problem:

Give you a 2D array(n * n, n is an odd number more than 1), rotate it counter-clockwise, remove max and min elements of each row, return the last surviving number when there is only one left

"""

"""                                                                      Solution:

Pretty straight-forward, [[arr[j][i] for j in range(len(arr))] for i in range(len(arr[0])-1,-1,-1)] rotates the array counter-clockwise and then for each row I remove the max and min, rinse and repeat
until there is one number left.

"""

def rotate_and_remove(arr):
    while len(arr) != 1:
        arr = [[arr[j][i] for j in range(len(arr))] for i in range(len(arr[0])-1,-1,-1)]
        for x in arr:
            x.remove(max(x))
            x.remove(min(x))
    return arr[0][0]
