"""
Initially we can try out every seqeuence but that is O(N^2) time. However we can optimize since elements may overlap between calculations

nums = [2, 6, 8, 3, 4, 5, 1]

subsequence = [2]
subsequence = [2, 6]
subsequence = [2, 6, 8]
3 is less than the previous number but we have to keep 3 in case it is part of the longest sequence if the current one isnt
    we would then have another list containing a potential answer
    however there can be so many of them

but we can just keep one sub array
    when a new number x is not greater than the last element of the subsequence, we do binary search to find the smallest element >= x in sub, and replace with number x

O(N * log(N)) time complexity where N is the length of the given array. We use binary search for each element over subsequence list.
O(N) space complexity since in the worst case the subsequence list is the entire given array.
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subsequence = []
        for curr_val in nums:
            if len(subsequence) == 0 or subsequence[-1] < curr_val:
                subsequence.append(curr_val)
            else:
                idx = bisect_left(subsequence, curr_val)  # Find the index of the smallest number >= curr_val
                subsequence[idx] = curr_val  # Replace that number with x
        return len(subsequence)

    
"""
# DP solution, try out every subsequence and store the max length increasing subsequence
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:    
        dp = [1 for _ in range(len(nums))]
        
        for i in range(len(nums)):
            for j in range(i):
                
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        
        return max(dp)
"""
