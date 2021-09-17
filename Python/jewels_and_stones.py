"""
U
we have a string that contains all valid jewels
    jewels are case sensitive
we will have count how many stones are jewels
    
the given test cases seem like enough
    is we dont have any jewels then we will have 0 stones but that is not part of the constraints

M
use a hashmap to store the jewels
then look at each stone if it is in hashmap then we increment a count of stones

P
LOL

I
See below

RE
"""

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hashmap = {}
        for i in range(len(jewels)):
            if jewels[i] not in hashmap:
                hashmap[jewels[i]] = True
        
        count = 0
        
        for i in range(len(stones)):
            if stones[i] in hashmap:
                count += 1
        
        return count
