"""
U
given a string, rearrange the characters so that any two adjacent characters are not the same
    return any possible rearrangement of s or return "" if not possible

M
max heap

P
if we get the frequency of each character and add to the max heap we can build a string starting with the max frequency character
    however we cant just rely on the top element since we cant two consecutive letters
    this means we need the top two at all times
        we can effectively have the top two by not adding the one we just used into the heap and waiting until the next step
            the only time when we would add back into the heap

"""
from heapq import *
class Solution:
    def reorganizeString(self, s: str) -> str:
        freq_map = {}
        for char in s:
            if char not in freq_map:
                freq_map[char] = 0
            freq_map[char] += 1
        
        max_heap = []
        for key, value in freq_map.items():
            heappush(max_heap, (-value, key))
        
        arrangement = []
        prev_char = ""
        prev_freq = 0
        while max_heap:
            curr_freq, curr_char = heappop(max_heap)
            
            arrangement.append(curr_char)
            
            curr_freq += 1

            if prev_freq < 0:
                heappush(max_heap, (prev_freq, prev_char))
            
            prev_freq = curr_freq
            prev_char = curr_char
            
            
        result = "".join(arrangement)
        if len(result) != len(s):
            return ""
        else:
            return result
