"""
From the Wikipedia article: 
"Formally, if f is the function that corresponds to the number of citations for each publication, we compute the h-index as follows: First we order the values of f from the largest to the lowest value. Then, we look for the last position in which f is greater than or equal to the position (we call h this position)"
"""

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        return sum(index < value for index, value in enumerate(sorted(citations, reverse = True)))
