"""                                                                      Problem:


Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return true if the string is valid, and false if it's 
invalid.

This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], and curly braces {}. Thanks to @arnedag for the idea!

All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.

What is considered Valid?
A string of braces is considered valid if all braces are matched with the correct brace.

Examples
"(){}[]"   =>  True
"([{}])"   =>  True
"(}"       =>  False
"[(])"     =>  False
"[({})](]" =>  False

"""

"""                                                                      Solution:

If the braces are legal then each occurance should have at least one set of consecutively completing braces like () [] or {} so if that's the case then those can be
removed and reinspected recursively because a new set of consecutively completing braces should exist now that the old one is removed, if at any point it doesn't
exist then we know it isn't a legal usage of braces and False is returned. If the string is completely empty at any point we know that it was legal throughout
the whole process so we can return True.

"""

def validBraces(string):
  s = ['()','[]','{}']
  if s[0] in string:
      string = string.replace(s[0], '')
      if string:
          return validBraces(string)
      else:
          return True
  elif s[1] in string:
      string = string.replace(s[1], '')
      if string:
          return validBraces(string)
      else:
          return True
  elif s[2] in string:
      string = string.replace(s[2], '')
      if string:
          return validBraces(string)
      else:
          return True
  else:
      return False
