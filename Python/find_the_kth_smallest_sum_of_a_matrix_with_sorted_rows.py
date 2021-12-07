"""
You are given an m * n matrix, mat, and an integer k, which has its rows sorted in non-decreasing order.
You are allowed to choose exactly 1 element from each row to form an array.
Return the Kth smallest array sum among all possible arrays

we build the function to find kth smallest pair sum
    use this to get the answer across the first two rows then keep going into the remaining row
    then we just process on the current k smallest sums and current row
    in the end we have the k smallest sums from the top row to the bottom row so our answer is kth element

O(m * klogk) time complexity where m is the number of rows and k is given. For each pair of rows we are finding the k smallest sums. This means that we are pushing, popping and reblancing k times per row. Rebalancing takes O(logk) time since our heap is size k.

O(k) space complexity since we have k elements in our heap
"""
from heapq import *
class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m = len(mat)
        n = len(mat[0])
        
        # if there is just one row then return the kth element
        if m == 1:
            return mat[0][k-1]
        
        # reapply find k pairs with smallest sums for the first two rows then for the rest
        answer = self.smallestSumPairs(mat[0], mat[1], k)
        
        for i in range(2, m):
            answer = self.smallestSumPairs(answer, mat[i], k)
        
        return answer[k - 1] 
        
    def smallestSumPairs(self, nums1, nums2, k):
        min_heap = []
        
        for i in range(min(k, len(nums1))):
            heappush(min_heap, (nums1[i] + nums2[0], i, 0))
        
        answer = []
        while k > 0 and min_heap:
            curr_pair_sum, nums1_index, nums2_index = heappop(min_heap)
            
            answer.append(curr_pair_sum)
            
            if nums2_index + 1 < len(nums2):
                heappush(min_heap, (nums1[nums1_index] + nums2[nums2_index + 1], nums1_index, nums2_index + 1))
            
            k -= 1
        
        return answer
        
