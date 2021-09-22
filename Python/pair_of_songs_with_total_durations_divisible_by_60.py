"""
U
We have an array of song durations and each song is in seconds
    a pair of songs is valid if their sum is a mulitple of 60

M
If we mod everything by 60 then the problem is just sum of two pairs where if the complement (60 - curr % 60) exists then we are fine
we want
    (t + x) % 60 = 0

which is
t % 60 + x % 60 = 60
x % 60 = 60 - t % 60
however if the song is 60 seconds then that mod 60 is 0 which is wrong
    x % 60 = 60 - t % 60
    x % 60 = (60 - t % 60) % 60

P
we can use a hashmap to quickly find the complement, the hashmap will store 0 - 59
    it is a frequency map of how many times a valid complement exists
    we will use this to add to our count

IRE
"""

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ans = 0
        
        c = {i : 0 for i in range(60)}
        
        for t in time:

            ans += c[(60 - t % 60) % 60]
            
            c[t % 60] += 1
            
        return ans
