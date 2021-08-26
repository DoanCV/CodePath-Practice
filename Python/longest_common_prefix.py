"""
we can just check the letter at each position of each string
    we can do this in one loop
the shortest string is the longest that the prefix can be

# if there is no prefix then we return an empty string
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # get the length of the shortest string in our list of strings
        shortest_string = min(strs, key = len)
        
        # if there is no prefix match, then longest_prefix = ""
        longest_prefix = ""
        
        # loop through the indicies of each string up until the length of the shortest string 
            # if the characters do not match then we return everything before
        for i in range(len(shortest_string)):
            # check each string in strings
                # if the characters we see so far match then update our longest_prefix
                # we can use .startswith() or just get up to ith position susbtring and compare
                
            if all([ curr_string[:i+1] == shortest_string[:i+1] for curr_string in strs]):
                longest_prefix = shortest_string[: i + 1]
        
        return longest_prefix
