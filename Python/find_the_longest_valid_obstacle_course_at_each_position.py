class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        """
        pick a subsequence of obstacles up to the current index 
        such that the height is always increasing or stays the same (can have duplicates out of order)

        longest increasing subsequence
            my solution to this common problem was to use dp and binary search
                at first you can try every subsequence
                however this needs to be repeated N times since we need the longest obstacle course for each index
                    makes my solution O(N^2)

                an improvement, use dp and binary search which gives O(NlogN)
                recall dp[i] stores the minimum value where a subsequence end with length i + 1

                key takeaway 
                >>>>>> dp[i] stores the minimum value of the end of the increasing subsequence of length i + 1
                
                ex
                nums = [10,9,2,5,3,7,101,18]
                dp = [10]               # since dp was empty, nothing to compare with
                dp = [9]                # length 1 whos minimum value is 9
                dp = [2]                # same reason as above
                dp = [2, 5]             # new element is greater than the last value of dp
                dp = [2, 3]             # 3 < 5 and 3 > 2, smallest value is 2 and so 3 replaces 5
                dp = [2, 3, 7]          # min is 3 and 7 > 3
                dp = [2, 3, 7, 101]     # same idea as above
                dp = [2, 3, 18, 101]    # subsequence ending with the value less than 18 is 3 and so 18 can extend that
                essentially we do binary search to find the smallest element >= x in sub, and replace with number x

            which binary search method to use, find where to place obstacle on the right since it may be greater than all of dp
                use bisect_right
        """

        dp = []
        result = []

        for obstacle in obstacles:

            idx = bisect_right(dp, obstacle)

            if idx == len(dp):
                dp.append(obstacle)
            else:
                dp[idx] = obstacle

            result.append(idx + 1)
        
        return result
