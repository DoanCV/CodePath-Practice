"""
inputs are valid so we know the parentheses are paired and in order

Each number consumes a sign.
Each + and - creates a new number.

expressions start like 3... or (..., not like +3... or +(....
there will always be someting before the sign, a number or a group bounded by parentheses

keep a running result value
keep an intial sign to process + or - when we see it and use it

1. when we see a digit read the rest of it, we are given a string so we need to get the entire number. since it is most significant first we just muliply by 10 and add the ascii equivalent of the current value

2. if we see a + sign we add the previous number and the next number

when we are done adding or subtracting numbers, reset the running sum since we finished a group of calculations

3. if we see a ( then we add our running sum to the stack to use later when we see a ) we also reset

4. if we see a ) then we pop our previous group result and combine with our running sum, then we reset our running sum


FOLLOW UP:
Add * and /

just pass through twice, first with * and / then again evaluate like before
    with order of operations * and / come first no matter what which then leaves + and -
"""

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        number = 0
        sign = 1
        
        for i in range(len(s)):
            curr_char = s[i]
            
            if curr_char.isdigit():
                number = number * 10 + int(curr_char)
            
            elif curr_char == "+":
                result += sign * number
                number = 0
                sign = 1
                
            elif curr_char == "-":
                result += sign * number
                number = 0
                sign = -1
                
            elif curr_char == "(":
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            
            elif curr_char == ")":
                result += sign * number
                number = 0
                result *= stack.pop()
                result += stack.pop()
        
        # add the first group
        result += sign * number
        
        return result
