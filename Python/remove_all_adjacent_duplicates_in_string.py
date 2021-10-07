"""
U
we have a string
remove adjacent duplicates

the characters of the string are all lowercase english alphabet characters

after we remove a pair the resulting string may create a new pair
    keep in mind that they are pairs

strings are immutable
    so we can convert string to a list with list()


M
we can loop through each character but when we remove a duplicate from the list we may create another group
    so we use a stack to check the current character against the top of the stack

we do not need to convert to list since we can just use our stack

P
"abbaca"

add the first element since it has nothing to compare with
[a,b,b,a,c,a]
i = 0
stack = [a]

[a,b,b,a,c,a]
i = 1
stack = [a,b]

[a,b,b,a,c,a]
i = 2
stack = [a]

[a,b,b,a,c,a]
i = 2
stack = [a]

[a,b,b,a,c,a]
i = 3
stack = []

[a,b,b,a,c,a]
i = 4
stack = [c]

[a,b,b,a,c,a]
i = 5
stack = [c,a]


IRE
"""

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        
        # we can start our loop at 1 but we will still have to check if the stack is empty at any point
        # prev = s[0]
        # stack.append(prev)
        
        for i in range(0, len(s)):
            
            # check the top of the stack if the stack isnt empty, otherwise add the current character
            if stack and stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
                
        return "".join(stack)
