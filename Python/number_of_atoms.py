"""
if there is one atom of a given element when we scan it will not have a 1
    this is good since we are scanning for uppercase then lowercase then number

we need to output how many atoms of each element are in the compound so we need a hashmap, mapping the element to its frequency
    the elements
    
use a stack
    we will go from right to left
        this is because the multipler comes first when we read from right to left
    
    
    
"""

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        
