"""
U
given a string find the minimum number of characters you need to delete to make the string good
    a string is good if no two different characters have the same frequencies
    
we can ignore 0 frequency characters otherwise we would not know when to stop if every frequency is already taken

M/P
greedy approach

{char: freq} get the frequency of each character

{freq: [char, char, ...]} not necessary but is useful in thinking of the greedy algorithm

starting with max_freq check for next available key else 0 since we ignore 0 occurance
    we then allocate the character here and increment delete count by the difference between the old key and new key
    
however, we do not need to start with max_freq since we have to check very unique character and find the next lowest freq for all but one character if there is a tie
    we can have a set to store what frequencies have already been taken
    
"""

class Solution:
    def minDeletions(self, s: str) -> int:
        
        freq_map = {}
        for char in s:
            if char not in freq_map:
                freq_map[char] = 0    
            freq_map[char] += 1
        
        deletions = 0
        
        used_frequencies = set()
        for key, value in freq_map.items():
            
            while value > 0 and value in used_frequencies:
                value -= 1
                deletions += 1
            
            used_frequencies.add(value)
            
        return deletions
