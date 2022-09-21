"""                                                                      Problem:


"""

"""                                                                      Solution:                                                                              """

""" create one integer value that's the full sum of the array and one equal to 0 and then add to the 0 value and subtract fro mthe full sum until they're even with the
subtracting and adding values being the numbers in the array that the for loop is indexing through. If an equivalence cannot be reached return False """

def find_even_index(arr):
    rSide = sum(arr)
    lSide = 0
    for x in range(0, len(arr)):
        rSide -= arr[x]
        if rSide == lSide:
            return x
        lSide += arr[x]
    return -1
