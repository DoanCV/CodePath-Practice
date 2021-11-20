"""
DFS with backtracking
    for each substring check if it is palindrome

O(2^N) time complexity where N is the length of the given string. There are 2^N ways to partition.
"""

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def helper(start, end, path):
            if start == end:
                answers.append(path[:]) 
            
            for i in range(start, end):
                curr = s[start : i + 1]
                if curr == curr[::-1]:
                    path.append(curr)
                    helper(i + 1, end, path)
                    path.pop()
        
        answers = []
        helper(0, len(s), [])
        return answers
