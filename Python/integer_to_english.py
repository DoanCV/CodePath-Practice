"""
U
We are given an integer, write it out in plain english

The test cases are enough

standard english:

    billion (which is the greatest since the integer given wont exceed 2^31 - 1), million, thousand, hundred
    
    twenty, thrity, fourty, fifty, sixty, seventy, eighty, ninety
    
    less than 20 is really weird:
    
        eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen
    
        one, two, three, four, five, six, seven, eight, nine, ten
    
        zero

M
Use a hashmap to capture the mapping from integer to english

the structure of the english form for 1001234567 is as follows

one BILLION one MILLION two hundred thiry four THOUSAND five hundred sixty seven

if we ingore the last hundred we can see that everything is processed at the comma or roughly every three digits

    for example the answer for a number between a million and a billion is word(number divided by a million) + "million" + word(remainder part after dividing by a million)
        this is where we use recursion to build the answer
        
P
we have to map everything above 

then we have a helper function to recurse through

    if num is <= 20 then we can use our map and we are done
    
    loop through our keys
        
        mod num by key
        integer divide num by key
        
        
        build part before the BILLION, MILLION, or THOUSAND
            use the integer division quotient
        
        build part after the BILLION, MILLION, or THOUSAND
            use the mod

IRE


"""

class Solution:
    def numberToWords(self, num: int) -> str:
        integer_to_english = {1e9: "Billion", 1e6: "Million", 1e3: "Thousand", 1e2: "Hundred", 
                              90: "Ninety", 80: "Eighty", 70: "Seventy", 60: "Sixty", 50: "Fifty", 40: "Forty", 30: "Thirty", 20: "Twenty",
                              19: "Nineteen", 18:  "Eighteen", 17: "Seventeen", 16: "Sixteen", 15: "Fifteen", 14: "Fourteen", 13: "Thirteen", 12: "Twelve", 11: "Eleven",
                              10: "Ten", 9: "Nine", 8: "Eight", 7: "Seven", 6: "Six", 5: "Five", 4: "Four", 3: "Three", 2: "Two", 1: "One", 
                              0: "Zero"}
        
        
        def helper(num):
            if num <= 20:
                return integer_to_english[num]
            
            for key, value in integer_to_english.items():
                quotient = num // key
                remainder = num % key
                
                # if we already accounted for this key then continue
                if not quotient: 
                    continue
                
                # < 100 does not have anything before so it is emtpy string
                if key >= 100:
                    s1 = helper(quotient) + " "
                else:
                    s1 = ""
                
                # if there is a reaminder then we build what is after the key otherwise it is an empty string
                if remainder:
                    s2 = " " + helper(remainder) 
                else:
                    s2 = ""
                
                return s1 + integer_to_english[key] + s2
            
        
        return helper(num)
