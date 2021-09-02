"""
REALLY REALLY fun fact :wazowskiStare:

the even digits all have a unique letter while the odd digits all don't:

zero: Only digit with z
two: Only digit with w
four: Only digit with u
six: Only digit with x
eight: Only digit with g

each of the odd number's letters all also appear in other digit words:
one, three, five, seven, nine

one is the only digit with an o
three is the only digit with t, h, and r
five is the only digit with f
seven is the only digit with s

we know every word version of a number is spelled out completely since s is guaranteed to be valid
    so we check for the even first and then remove it from the frequency map of characters, then we look for the odd numbers
    
ex. s = "owoztneoer"
letter_freq = {"o": 3, "w": 1, "z": 1, "t": 1, "n": 1, "e": 2, "r": 1}

result = [1,0,0,0,0,0,0,0,0,0]
letter_freq = {"o": 2, "w": 1, "z": 0, "t": 1, "n": 1, "e": 1, "r": 0}

result = [1,0,1,0,0,0,0,0,0,0]
letter_freq = {"o": 1, "w": 0, "z": 0, "t": 0, "n": 1, "e": 1, "r": 0}

result = [1,1,1,0,0,0,0,0,0,0]
letter_freq = {"o": 0, "w": 0, "z": 0, "t": 0, "n": 0, "e": 0, "r": 0}

"012"

"""

# frequency counter, hashmap
from collections import Counter

class Solution:
    def originalDigits(self, s: str) -> str:
        # get frequencies of each character in the given string
        letter_freq = Counter(s)
        
        # we will use this to remove the entire number when we find it 
        word_form = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        
        # order to search and remove
        unique_letter_to_number = {"z": 0, "w": 2, "u": 4, "x": 6, "g": 8, "o": 1, "h": 3, "f": 5, "s": 7, "i": 9}
        
        # remove the word form from the frequency map
        # we have a result array to keep track of what number we found, it will only have 0s or 1s
        result = [0 for _ in range(10)]     # a result array which is worst case size 10 since we are representing 0-9
        for key, val in unique_letter_to_number.items():
            
            # We found the number
            result[val] = letter_freq[key]
            
            # remove the word form of the number we just found from the frequency map
                # Counter(full word * remaining frequency of the letter) gives us the letter frequency of the word form of a number
            letter_freq -= Counter(word_form[val] * letter_freq[key])
        
        # we will convert the 0-9
            # enumerate => index (default 0), value
            # we have all 1s or 0s, 1s means we found it and 0s means we have not found it
        result = [str(i)*x for i, x in enumerate(result)]
        
        # return result, join ignores empty string which we have when we havent found the number
        return "".join(result)
