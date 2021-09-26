"""
[3,1,2,4]

generate permutations (inefficient but for demonstration)

generate subarrays up until the ith element
[3]
[3,1], [1]
[3,1,2], [1,2], [2]
[3,1,2,5], [1,2,5], [2,5], [5]
[3,1,2,5,4], [1,2,5,4], [2,5,4], [5,4], [4]

3
1 + 1
1 + 1 + 2
1 + 1 + 2 + 5
1 + 1 + 2 + 4 + 4

we observe that
if arr[i - 1] <= arr[i]:
    then result[i] = result[i] + arr[i]

our subarrays ending with i-th value are basically same subarrays for (i-1)-th value with extra element arr[i] added to each one of them and plus one extra subarray consisting of singular value arr[i]
this is why we can reuse the previous sum and account for the extra singular element subarray

result[i] = result[j] + arr[i]*(i-j)

"""

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr = [0] + arr
        
        result = [0 for _ in range(len(arr))]
        
        stack = [0]
        
        for i in range(len(arr)):
            while arr[stack[-1]] > arr[i]:
                stack.pop()
            j = stack[-1]
            result[i] = result[j] + (i - j) * arr[i]
            stack.append(i)
        
        return sum(result) % (10**9 + 7)
