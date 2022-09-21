"""                                                                      Problem:

In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". Your function receives one side of the DNA (string, except for Haskell);
you need to return the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).

Example: (input --> output)

"ATTGC" --> "TAACG"
"GTAT" --> "CATA"

"""

"""                                                                      Solution:

Create a dictionary to access the complement of each symbol, add the value for the key of every character from dna to s and then return s.

"""

def DNA_strand(dna):
    dicti = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    s = ''
    
    for i in dna:
        s += dicti[i]
        
    return s
