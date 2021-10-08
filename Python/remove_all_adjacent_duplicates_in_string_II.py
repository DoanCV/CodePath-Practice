"""
U
we are given a string and k

when we have k adjacent duplicate letters remove them
    after removing we may still have k adjacent duplicates
    
    
if more than k duplicates are adjacent, we remove just k of them
    we do this in k groups
    
return the final result


M
we can use a stack
    inside the stack we will store the number of consecutive letters we have seen and the letter itself
    that way when we hit k we just remove the top k elements
    
ex:
"deeedbbcccbdaa", k = 3

i = 0
stack = [(d,1)]

i = 1
stack = [(d,1), (e,1)]

i = 2
stack = [(d,1), (e,1), (e,2)]
we get 2 since we look at the top and see 1 then we add 1 since we just found an e

i = 3
stack = [(d,1), (e,1), (e,2), (e,3)]
    since stack[-1][1] aka 3 == k
        we can just pop instead of adding
stack = [(d,1)]

i = 4
stack = [(d,1), (d,2)]

i = 5
stack = [(d,1), (d,2), (b,1)]

i = 6
stack = [(d,1), (d,2), (b,1), (b,2)]

i = 7
stack = [(d,1), (d,2), (b,1), (b,2), (c,1)]

i = 8
stack = [(d,1), (d,2), (b,1), (b,2), (c,1), (c,2)]

i = 9
stack = [(d,1), (d,2), (b,1), (b,2), (c,1), (c,2), (c,3)]
    since stack[-1][1] aka 3 == k
        we can just pop instead of adding
stack = [(d,1), (d,2), (b,1), (b,2)]

i = 10
stack = [(d,1), (d,2), (b,1), (b,2), (b,3)]
    since stack[-1][1] aka 3 == k
        we can just pop instead of adding
stack = [(d,1), (d,2)]

i = 11
stack = [(d,1), (d,2), (d,3)]
    since stack[-1][1] aka 3 == k
        we can just pop instead of adding
stack = []

i = 12
stack = [(a,1)]

i = 13
stack = [(a,1), (a,2)]

output = "aa"

P
instead of a pair in the stack we also can use a hashmap to make it easy to join the result string back from the stack

however for now I will use the tuple in stack

IRE
"""
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        # intialize stack
        stack = []

        # loop through each character 
        for i in range(len(s)):
        
            # if the stack isnt empty and the top element is the same as the current element
            if stack and stack[-1][0] == s[i]:
                
                # add to the stack and increment the count
                stack.append((s[i], stack[-1][1] + 1))
                
                # if the count is equal to k then pop k times
                if stack[-1][1] == k:
                    for _ in range(k):
                        stack.pop()
                        
            # else add the element to the stack and its count is 1
            else:
                stack.append((s[i], 1))

        # join the string from the contents of the stack
        result = ""
        for i in range(len(stack)):
            result = result + stack[i][0]
        return result
