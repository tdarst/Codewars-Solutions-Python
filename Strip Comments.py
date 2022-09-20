"""                                                                                Problem:


Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
The code would be called like so:

var result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
// result should == "apples, pears\ngrapes\nbananas"

"""

#                                                                                  Solution:

"""
Create a list containing the excerpts of the passed-in string, split by line breaks. For each of those excerpts (as indexes of "split") check and see if they contain
any of the passed-in comment markers (if any were passed-in at all), if so find it's index and slice it out, then strip its whitespace with ".strip()". After this 
process is done with all excerpts, rejoin them with a line break between each and return it. 

If no markers are passed-in simply strip its whitespace with ".strip()" and rejoin the excerpts with a linebreak between each.
"""

def solution(string,markers):
    
    split = string.split('\n')
    
    if markers:
        for x in range(0,len(split)):
            for y in markers:
                if y in split[x]:
                    split[x] = split[x][:split[x].find(y)]
                split[x] = split[x].strip()
                
        return '\n'.join(split)
    
    else:
        for x in range(0,len(split)):
            split[x] = split[x].strip()
            
        return '\n'.join(split)
