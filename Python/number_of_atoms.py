"""
if there is one atom of a given element when we scan it will not have a 1
    this is good since we are scanning for uppercase then lowercase then number

we need to output how many atoms of each element are in the compound so we need a hashmap, mapping the element to its frequency
    the elements
    
use a stack to store the multipliers that we scan when we find a )

we will go from right to left # this is because the multiplier comes first when we read from right to left

    if see a digit
        scan the digits of the multiplier
        save the multiplier
    
    if we see a )
        add the current multiplier to the stack
        update the multidepth weight
    
    if we see a (
        we have already processed elements in the parentheses, this means our depth decreases by 1 
        update our multidepth multiplier, divide by the multiplier at the top of the stack
    
    if we see a lowercase # check this before upper since it will come first and there can be multiple
        keep building the element as long as there are lowercase characters
        
    if we see an uppercase
        create the full element since we know that uppercase denotes the start of the element
        add the frequency of the element ie. current multiplier * multilevel depth
    
    decrement position


O(NlogN + N) => O(NlogN) time complexity, where N is the length of the given formula, since we sort the keys, ie. elements, of our hashmap to make sure that the output is in alphabetical order. Although N is not exactly equal to the number of elements since there can be other characters that are not capital letters this analysis suffices. I left O(N) to denote the main algorithm which is just scanning the formula from right to left

O(N) space complexity since we use a hashmap with the size equal to the number of unique elements in our formula. We also use a stack to store the multipliers at each depth.
"""

from collections import Counter
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        
        element_count = Counter()
        stack = []
        
        
        multiplier = 1 # keep track of the most recent integer
        cumulative_multiplier = 1 # this is the multidepth multiplier, when we find a ( we know that the multiplier at the top of the stack is unecessary
        
        i = len(formula) - 1
        while i >= 0:
            element_lowercase_string = "" # we reset as "" since we may just have a capital letter element
            multiplier = 1 # reset when we are done processing
            
            # we can find a digit, that is part of the multiplier
            if formula[i].isdigit():
                curr_multiplier = "" # build multiplier
                    
                while formula[i].isdigit():
                    curr_multiplier = formula[i] + curr_multiplier
                    i -= 1
                
                multiplier = int(curr_multiplier)
                
            # closed parentheses
            if formula[i] == ")":
                cumulative_multiplier *= multiplier
                stack.append(multiplier)
                
            # open parentheses
            if formula[i] == "(":
                cumulative_multiplier = cumulative_multiplier // stack.pop()
                
            # process the element, no element has 2 capital letters, it will start with a captial and have a lowercase (can be multiple)
            if formula[i].islower():
                    while formula[i].islower():
                        element_lowercase_string = formula[i] + element_lowercase_string
                        i -= 1
                        
            # we finished builing the element, now add its frequency that we just scanned to the map    
            if formula[i].isupper():
                element = formula[i] + element_lowercase_string
                element_count[element] += multiplier * cumulative_multiplier
             
            i -= 1
            
        result = []
        for element in sorted(element_count.keys()):
            result.append(element)
            
            if element_count[element] > 1:
                result.append(str(element_count[element]))
                
        return "".join(result)
