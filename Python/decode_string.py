"""
Given a string, decode it

input: "a2[ab]"
output: "aabab"

input: a2[a3[ba]]
output: "aabababaabababa"

input: 10[a]
output: "aaaaaaaaaa"
"""

def decodeString(s):
  # check if the given string is empty
  if s is None:
    return ""
  
  stack = []
  
  for curr in s:
    # append the current character if it is not a close square bracket
    if curr == "[" or curr.isalpha() or curr.isdigit():
      stack.append(curr)
    else:
      # get the pattern inside the square brackets
        # popped + current_pattern, in this order since we are reading backwards
      current_pattern = ""
      while stack[-1] != "[":
        current_pattern = stack.pop() + current_pattern
      
      # we do not need the open square bracket anymore
      stack.pop()
      
      # get the multiplier, we need a loop since it can be more than one digit
        # popped + current_multiplier, in this order since we are reading backwards
      multiplier = ""
      while stack and stack[-1].isdigit():
        multiplier = stack.pop() + multiplier
      
      # the blank is implicitly 1
      if multiplier == "":
        multipler = 1
      
      # add the repeated current pattern to the stack
      stack.append(int(multiplier) * current_pattern)
      
return "".join(stack)

# O(N) time complexity, where N is the length of the given string, since we are traversing the string once and not repeating calculations.
# O(N) space complexity since in the worst case our stack will hold about N/2 open square brackets.
       
        
