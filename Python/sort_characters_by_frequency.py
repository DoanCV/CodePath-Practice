"""
we need the frequency of each character

then we store each letter and frequency in a heap
    we use frequency as priority
    that way when we pop we can know the order and we can make a size frequency string of the character and add it to a result string
    we will use max_heap since we want decreasing order
    
"""
from collections import Counter
from heapq import *
class Solution:
    def frequencySort(self, s: str) -> str:
        freq_map = Counter(s)
        
        max_heap = []
        
        for key, value in freq_map.items():
            heappush(max_heap, (-value, key))
        
        result = ""
        while max_heap:
            freq, letter = heappop(max_heap)
            
            curr = letter * -freq
            
            result = result + curr
        
        return result

      
# O(N + M + MlogM) -> O(N) time complexity, where N is the length of the given string and M is the number of distict characters in the given string. N comes from Counter() which is how we are adding elements to our hashmap. M comes from us going through the max_heap to build the sorted string. Rebalancing takes O(logM) time and we do this M times since that is each unique character from our hahsmap. We can actually see this as constant time since we are guaranteed lowercase alphabetical characters only so 26 max.
# O(M) space complexity since that is the size of both our heap and hashmap. We are not counting the length of the output string since that is obviously just N since it is just a sorted version of the given string. M is at most 26 based on the constraints.
