"""
We have a string of both 
    english lowercase characters
    open and close parentheses, "(" and ")"
    and no invalid characters
    
    
the string need to be balanced where parentheses come in pairs
    think valid parentheses problem


we can use a stack to keep track of visited parentheses, "("
    we will store the position

Have an a hashmap of indicies mapping to bools indicating whether or not we should remove the character at that position
    we will use what we pop from the stack to mark off what to keep or delete
    hashmap = {index: if True keep, if False delete or do not include when building the output string}
    
O(N) time complexity, where N is the length of the given string since we solve with two passes.
O(N) space complexity since our stack will store the open parentheses and in the case that the string is already valid we have N/2 open parentheses.
"""

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        valid_map = {}
        stack = []
        
        for index, character in enumerate(s):
            # ignore letters
            # we now can see two things
            # if we see ) then we know that we need to look at the top of the stack, but if this is our first character in a pair then we have to delete it
                # this is because there are no ( to balance so we need to remove the )
            if character == "(":
                stack.append(index)
            elif character == ")" and len(stack) > 0:
                valid_map[stack[-1]] = True
                valid_map[index] = True
                stack.pop()
            
        # build result
        result = []
        for index, character in enumerate(s):
            
            # check if the current parentheses should be included
            if character == "(" or character == ")":
                if index in valid_map and valid_map[index]:
                    result.append(character)
            
            # add letters
            else:
                result.append(character)
                
        return "".join(result)
