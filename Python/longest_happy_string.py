"""
U
given three integers (a,b,c) return the longest possible happy string
    a string is happy when it only contains "a", "b", "c"
    it cannot contain the same three letters in a row
    the string will have at most
        a occurances of "a", b occurances of "b", c occurances of "c"
    
    there can be multiple answers, return any one of them
    
M
we can use a max heap to build our solution
    we can approach this with a greedy algorithm since we want to use the max frequency character as many times as we can

P
two cases
    the top character can be added
        we simply add the top character to the string builder and decrease the frequency of the top character and add it back
        
    the top cant be added
        this is because the last two characters in our string builder is the same as the top character
        we need to get the next character in our max heap
            there may not be another character, in that case our string is complete we cant increase the length
        
        we will then add that character to the string builder and then decrease the frqeuncy and then add the former top and next top back
    
we can only add back to the heap if the frequency is non zero
        
"""

from heapq import *
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        max_heap = []
        
        if a > 0:
            heappush(max_heap, (-a, "a"))
        if b > 0:
            heappush(max_heap, (-b, "b"))
        if c > 0:
            heappush(max_heap, (-c, "c"))

        longest_string = []
        while max_heap:
            
            first_char_frequency, first_char = heappop(max_heap)
            
            if len(longest_string) >= 2 and first_char == longest_string[-1] == longest_string[-2]:
                
                if not max_heap:
                    return "".join(longest_string)
                
                second_char_frequency, second_char = heappop(max_heap)
                longest_string.append(second_char)
                
                second_char_frequency += 1 # negative bc of max heap so we "add"
                if second_char_frequency < 0:
                    heappush(max_heap, (second_char_frequency, second_char)) 
                    
                heappush(max_heap, (first_char_frequency, first_char))
                
            else:
                longest_string.append(first_char)
                
                first_char_frequency += 1 # negative bc of max heap so we "add"
                if first_char_frequency < 0:
                    heappush(max_heap, (first_char_frequency, first_char))                
        
        return "".join(longest_string)
