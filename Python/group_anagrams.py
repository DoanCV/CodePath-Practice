"""
anagrams can be compared on the frequency of each character, if the frequencies are the same then they are anagrams
    however we have an array of strings so we cant just have that many hashmaps and then go and compare them all
    
instead we can map the anagram to its group then go through the map to add the groups to the output
    we can use the fact that anagrams when sorted are the same thing
    we will use the sorted version as our key to know when to add the original into the list
    
ex. 
strs = ["eat","tea","tan","ate","nat","bat"]

groups = {}

i = 0
eat => aet
groups = {"aet": ["eat"]}

i = 1
tea => aet
groups = {"aet": ["eat", "tea"]}

i = 2
tan => ant
groups = {"aet": ["eat", "tea"], "ant": ["tan"]}

... same idea

once we finish our single pass, we add every group to the output array

return it
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = {}
        
        for curr in strs:
            
            sorted_string = "".join(sorted(curr))
            
            if sorted_string in groups:
                
                groups[sorted_string].append(curr)
            
            else:
                
                groups[sorted_string] = [curr]
                
            
        return groups.values()
      
# O(N * KlogK) time complexity, where N is the length of the given array and K is the length of the string in the array. We sort each string for each string in the array of strings.
# O(N) space complexity since in the worst case no words are anagrams of each other and our hashmap is the size of the given array.
