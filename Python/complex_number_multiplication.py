"""
# observations
we are given two string

a + bi

the sign of the b term is explicit so we can literally have a + -bi

human evalutation is as follows

(a_1 + b_1i) * (a_2 + b_2i)
FOIL it out

(a_1 * a_2) + (a_1 * b_2i) + (a_2 * b_1i) + (b_1 * b_2 * i * i)

all the a and b terms are just coefficients and are integers

we can scan through the first string and multiply each term with that of the second string
    four multiplications in total
    
we can store each result in an array
    then we scan this array of size 4 and then simplify

"""

class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        # find where the plus signs are since they are always going to be there
        plus_a = num1.index("+")
        plus_b = num2.index("+")
        
        # get the coefficients of real term
        a_1 = int(num1[:plus_a])
        a_2 = int(num2[:plus_b])
        
        # get the coefficients of imaginary term
        b_1 = int(num1[plus_a + 1 : -1])
        b_2 = int(num2[plus_b + 1 : -1])
        
        # FOIL
        result = str((a_1 * a_2) + (b_1 * b_2 * -1)) + "+" + str((a_1 * b_2) + (a_2 * b_1)) + "i"
        
        # return result
        return result
