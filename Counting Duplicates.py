"""                                                                      Problem:

Count the number of Duplicates
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

Example
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice

"""

"""                                                                      Solution:

Since capitals are involved first turn the string to lower-case only. Iterate through the enumerated string and check for each part of the original string if a certain
character is both a duplicate and has not already been counted (t.find(y) returns the index number it is first found at so "aa" isn't counted as two different duplicate
characters and instead one instance of a duplicate character). return the count.

"""

def duplicate_count(t):
    z = 0
    t = t.lower()
    for x, y in enumerate(t):
        if t.count(y) > 1 and t.find(y) == x:
            z+=1
    return z
