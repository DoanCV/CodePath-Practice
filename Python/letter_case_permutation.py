"""
BFS subsets grokking pattern
Iterative version

"a1b2c3"                                                                    <= initialization
"a1b2c3" {"A1b2c3"}                                                         <= i = 0, a toggled to A
"a1b2c3" "A1b2c3"                                                           <= i = 1, ignore '1', which is a digit,
"a1b2c3" "A1b2c3" {"a1B2c3" "A1B2c3"}                                       <= i = 2, b toggled to B
"a1b2c3" "A1b2c3" "a1B2c3" "A1B2c3"                                         <= i = 3, ignore '2', which is a digit,
"a1b2c3" "A1b2c3" "a1B2c3" "A1B2c3" {"a1b2C3" "A1b2C3" "a1B2C3" "A1B2C3"}   <= i = 4, c toggled to C
"a1b2c3" "A1b2c3" "a1B2c3" "A1B2c3" "a1b2C3" "A1b2C3" "a1B2C3" "A1B2C3"     <= i = 5, ignore 3, which is a digit.

O(n * 2^n) time complexity where n is the length of the string. There are 2^n combinations since there are only 2 cases, upper and lower, and in the worst case our entire string is all letters. When we generate permutations we go through all of our previous permutations which are length n.
O(n * 2^n) space complexity since there are 2^n permutations and the depth of the tree is n.

"""

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        answer = [s]
        
        for index, character in enumerate(s):
            
            if character.isalpha():
                # swap the case for all of our permutations
                for j in range(len(answer)):
                    curr_permutation = list(answer[j])
                    curr_permutation[index] = curr_permutation[index].swapcase()
                    answer.append("".join(curr_permutation))
                    
        return answer         
