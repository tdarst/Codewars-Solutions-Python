"""                                                                      Problem:

Given an array of integers, remove the smallest value. Do not mutate the original array/list. If there are multiple elements with the same value, remove the one with a lower index. If you get an empty array/list, return an empty array/list.

Don't change the order of the elements that are left.

"""

"""                                                                      Solution:

Copy the list to avoid mutation and then return it after removing the lowest value.

"""

def remove_smallest(numbers):
    num = numbers[:]
    if num:
        num.remove(min(num))
    return num
