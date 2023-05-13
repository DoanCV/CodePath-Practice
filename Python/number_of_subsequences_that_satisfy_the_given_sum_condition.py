class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        """
        sort with two pointers works since we dont care about the actual subsequence
            we just need to count the possible ones and the max and min can be out of order

        once we get to a point where the sum of both pointers are less than or equal to target, update answer
            both pointers can be on the same single element

        calculate how many subsequences between start and end pointers
            2^(end-start)

        """
        MOD = 10**9 + 7

        subsequenceCount = 0
        nums.sort()

        j = len(nums) - 1
        for i in range(len(nums)):
            while i <= j and nums[i] + nums[j] > target:
                # need to keep honing in
                j -= 1

            if i <= j and nums[i] + nums[j] <= target:
                subsequenceCount += 2**(j-i)

        return subsequenceCount % MOD
