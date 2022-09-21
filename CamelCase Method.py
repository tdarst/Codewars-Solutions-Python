"""                                                                      Problem:

Write simple .camelCase method (camel_case function in PHP, CamelCase in C# or camelCase in Java) for strings. All words must have their first letter
capitalized without spaces.

For instance:

camelcase("hello case") => HelloCase
camelcase("camel case word") => CamelCaseWord

"""

"""                                                                      Solution:

Since the words are already spaced we can use the title() method to capitalize them all and then remove the spaces. Was proud of doing this one in one line.

"""

def camel_case(s):
    return s.title().replace(" ", "")
