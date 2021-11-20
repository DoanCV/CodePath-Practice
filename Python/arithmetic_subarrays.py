"""
A sequence is arithmetic if it contains at least two elements and the difference between every two consecutive elements are the same
ex. 
1, 3, 5, 7, 9 is arithmetic
7, 7, 7, 7 is arithmetic
3, -1, -5, -9 is arithmetic

We are given two lists, one represents starting indicies and the other ending indicies
    return a list of booleans inidcating if the query has an arithmetic sequence or can be rearranged into one

First thought:
Try each query
    sort the subarray and then scan again to see if it is arithmetic
O(m * nlogn) time complexity where m is the number of queries and n is the length of the subarray. We try eveyr query and sort every subarray in question.
O(n) space complexity since we use a sorted copy of the given array.


Second thought:
We can do this without sorting
    Take advantage that it is an arithmetic sequence that we are looking for
    If we have the max and min of the subarray we can apply the following
    The nth term of an arithmetic sequence is given by the equation:
        an = am + (n - m)d where m is a previous term
        Since we are using min and max we are referring to first and last terms a1, an
            we do not need to sort to find the min and max values
        Solving the equation for d we get:
        d = (an - a1) / (n - 1)

O(m * n) time complexity where m is the number of queries and n is the length of the subarray in question. We try every query but for each of them we do not sort the subarray. Instead we have a linear scan for max value, min value and added all elements to hashset. We then go through each step of a potentially valid sequence and search our hashset for validation.
O(m + n) space complexity since we have an array of size m which stores the result of each query and a hashset of size n since in the worst case every subarray in question does not have duplicates.
"""

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        def isArithmetic(subarray):
            # get the max and min and find the difference between each term
            sequence = set(subarray)
            max_val = max(subarray)
            min_val = min(subarray)
            
            # step needs to be an integer otherwise it makes no sense
            if (max_val - min_val) % (len(subarray) - 1) != 0:
                return False
            
            step = (max_val - min_val) // (len(subarray) - 1) # this has to be an integer
            
            # step can be 0 if the max and min are the same which means a valid arithmetic sequence
            if step == 0:
                return True
            
            # start from the min and increment to the max, if we are missing a value from the sequence then it is not arithmetic
            for i in range(min_val, max_val, step):
                if i not in sequence:
                    return False
            return True
        
        
        results = []
        for query in range(len(l)):
            results.append(isArithmetic(nums[l[query]: r[query] + 1]))
            
        return results
