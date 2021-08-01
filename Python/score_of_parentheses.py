class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for curr in s:
            if curr == "(":
                stack.append(0)
            else:
                
                curr_score = 0
                
                while stack[-1]:
                    curr_score += stack.pop()
                    
                stack.pop()
                
                if curr_score > 0:
                    stack.append(2 * curr_score)
                else:
                    stack.append(1)
        
        result = 0
        for i in range(len(stack)):
            result += stack[i]
        
        return result
      
# O(N) time complexity where N is the length of the given string since we traverse through the sting once.
# O(N) space complexity since in the worst case the string is jsut nested parentheses pairs so our stack will get to N/2 capacity.
