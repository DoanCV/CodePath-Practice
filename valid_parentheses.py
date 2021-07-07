class Solution:
    def isValid(self, s: str) -> bool:
        """
        Use a stack
        store open brackets in the stack
        when we see a closing bracket we pop the stack and compare
        if they do not match we do not have a valid string
        when the stack is empty after looping through the string, it is valid
        """
        
        symbols = {
            "(": ")",
            "[": "]",
            "{": "}" 
        }
        
        stack = []
        
        for curr in s:
            if curr in symbols:
                stack.append(curr)
            else:
                if len(stack) == 0:
                    return False
                if symbols[stack.pop()] != curr:
                    return False
        return len(stack) == 0
      
# O(N) times complexity, where N is the length of the given string, since we traverse through the string once.
# O(N) space complexity since the stack stores all of the opening parentheses.
