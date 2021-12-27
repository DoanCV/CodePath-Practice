"""
Exactly the same problem as 1081. Smallest Subsequence of Distinct Characters


Remove duplicate letters from the given string so that every letter appears once and only once
    make sure the reuslt is in the smallest lexicographical order among all possible results


Store the unique letters in a stack
To keep track of lexicographical order we use a hashmap to know the last occurance of a letter
    that way we include the last instance if the letter comes before another unqiue letter but shouldnt lexicographically
    
O(N) time complexity where N is the length of the given string. We have to visit each character of the string. I solve in two passes. The stack is worst case size 26 so that is just a coefficient.
O(26) space complexity since we have a stack that is worst case 26 letters of the english alphabet and a hashmap that has 26 keys in the worst case. 
"""

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_index = {value : index for index, value in enumerate(s)}
        stack = []
        
        for index, character in enumerate(s):
            if character not in stack:
                while stack and character < stack[-1] and index < last_index[stack[-1]]:
                    stack.pop()
                stack.append(character)
        
        return "".join(stack)
