"""                                                                      Problem:

Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and 
preserving the original order of elements.

For example:

uniqueInOrder("AAAABBBCCDAABBB") == {'A', 'B', 'C', 'D', 'A', 'B'}
uniqueInOrder("ABBCcAD")         == {'A', 'B', 'C', 'c', 'A', 'D'}
uniqueInOrder([1,2,2,3,3])       == {1,2,3}

"""

"""                                                                      Solution:

Create an empty list and fill it with the elements of the passed-in list if that element has not already been appended or is not a repeating element. This allows for 
the order of the elements to be preserved without repeating elements to be added.

Return the new list "l".

"""

def unique_in_order(i):
    l = []
    for x in range(0, len(i)):
        if i[x] not in l or i[x-1] != i[x]:
            l.append(i[x])
    return l
