class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Use a stack
        Loop through the array
            if not an operator, push to stack
            if operator, pop twice, perform operation, push result back to stack
        """
        
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == "/":
                a = stack.pop()
                b = stack.pop()
                result = int(b / a)
                stack.append(result)
            elif tokens[i] == "-":
                a = stack.pop()
                b = stack.pop()
                result = int(b - a)
                stack.append(result)    
            elif tokens[i] == "+":
                a = stack.pop()
                b = stack.pop()
                result = a + b
                stack.append(result)
            elif tokens[i] == "*":
                a = stack.pop()
                b = stack.pop()
                result = a * b
                stack.append(result)
            else:
                stack.append(int(tokens[i]))
        return stack.pop()
        
# O(N) time complexity, where N is the length of the array, since we traverse through the array once.
# O(N) space complexity since we are using a stack to store the numbers. There is always one more number than operands so roughly N/2 is asymptotically linear.
