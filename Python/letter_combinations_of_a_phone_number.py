"""
we are given a string of digits from 2-9
    these are digits that can map to different letters exactly like in a phone dial pad
    return all possible letter combinations that the given string can represent
    


approach:
use a hashmap to map the digit to a set of characters
keep track of our combinations in an array 

DFS
when we have gotten to the end of digits, then we are done
loop through all characters for the current digit in digits
    build the phone number
    recurse with the current combination
    backtrack when we finished one combination
    
O(4^N * N) time complexity where N is the length of digits. The 4 comes from the worst case number of possible mappings that we have for a given digit. This means 4 times the possibilities. The second N comes from the splicing which is linear in nature

O(4^N + N + 8) space complexity. We store all combinations in an array and there are 4^N of them. We also have a recursive call stack which would be the length of the digits string deep. The 8 which should of course be dropped is the size of our mappings hashmap.
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        mappings = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9 :"wxyz"}
        output = []
        
        # handle 0 len digits string
        if len(digits) == 0:
            return output
        
        def dfs_helper(position, phone_number):
            if len(phone_number) == len(digits):
                output.append(phone_number)
                return 
            
            curr_digit = digits[position]
            for digit in mappings[int(curr_digit)]:
                phone_number = phone_number + digit
                dfs_helper(position + 1, phone_number)
                phone_number = phone_number[0:-1] # backtrack, since until we get to the end of the for loop there are other letters to try
        
        
        dfs_helper(0, "")
        return output
        
