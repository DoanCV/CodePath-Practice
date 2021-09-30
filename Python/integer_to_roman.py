"""
U
We are given an integer, convert it to Roman numeral

no negatives

weird cases
    4, 9, 40, 90, 400, 900
    
special characters
    1, 5, 10, 50, 100, 500, 1000

we want to output a string

M
We can account for these cases in a hashmap

Then we can build the roman numeral by checking the hashmap to see if the integer can be made up of the current key

P
store cases in hashmap

loop through each key
    
    divide the current value 
    
    add the converted form to the result string
    
    update the value since we just accounted for the current key


I
See solution class below

R
if we have 3 we want III
    when we look in our hashmap, only 1 is available which means 3 // 1 gives us 3 "I"
we can do this for each key
    3 // 1000 is the same as 3 // 900 since 1000 and 900 are not in 3
    
    
E
O(N) time since we solve in one pass
O(M) space where M is the number of cases or keys in our hashmap

"""

class Solution:
    def intToRoman(self, num: int) -> str:
        result = ""
        
        hashmap = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}
        
        for key, val in hashmap.items():
            
            result += (num // key) * val
            num %= key
        
        return result
