def find_even_index(arr):
    rSide = sum(arr)
    lSide = 0
    for x in range(0, len(arr)):
        rSide -= arr[x]
        if rSide == lSide:
            return x
        lSide += arr[x]
    return -1