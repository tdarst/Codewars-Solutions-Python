"""                                                                      Problem:

Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

The binary number returned should be a string.

Examples:(Input1, Input2 --> Output (explanation)))

1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)

"""

"""                                                                      Solution:

Since python's bin() returns the binary representation of the value with a '0b' in front you just add the two passed-in integers together and return the binary
value without the '0b'.

"""

def add_binary(a,b):
    c = a + b
    return bin(c).replace('0b', '')
