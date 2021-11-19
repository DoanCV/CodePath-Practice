"""
We are given a string representing an initial state of dominoes

At the initial state
    L means fall left
    R means fall right
    . means untouched

Return a string representing the final state
When there is force from both left and right the domino will not move

We have four cases:
L...L, in this case, we need to fill everything with L
R...R, in this case, we need to fill everything with R
L...R, we need to keep it as it is
R...L, then we need to fill first half with R and second with L, handling odd and even cases.

I think we can solve in one pass, we just need to access adjacent dominoes
    going from left to right
    
O(N) time complexity where N is the length of the given string since we solve in one pass. 
O(N) space complexity since we are creating a new string to hold our final result state
"""
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        result = ""
        i = 0
        
        while i < len(dominoes):
            
            # initial or final state has already been decided
            if dominoes[i] == "L" or dominoes[i] == "R":
                result = result + dominoes[i]
                i += 1
            
            else: # we see a "."
                
                # if we have a R previously then we need to see how many dots there are and what is after to push
                if i > 0 and dominoes[i - 1] == "R":
                    
                    j = i
                    while j < len(dominoes) and dominoes[j] == ".":
                        j += 1
                    dot_count = j - i
                    
                    # two cases here
                    # if j is at the end or the character at j is right then every dot is pushed right
                    if j == len(dominoes) or dominoes[j] == "R":
                        result = result + "R" * dot_count
                        
                    # if the character at j is left then we either push half left/right and leave one alone in the odd dot count case or push half left/right in even case
                    else:
                        result = result + "R" * (dot_count // 2) + "." * (dot_count - 2 * (dot_count // 2)) + "L" * (dot_count // 2)
                    
                    i = j
                    
                # there is no R before or so far all we have is dot since anything left wouldve gone left
                else:
                    
                    j = i
                    while j < len(dominoes) and dominoes[j] == ".":
                        j += 1
                    dot_count = j - i
                    
                    # two cases here
                    # if j is at the end or the last character at j is right then we just have dots
                    if j == len(dominoes) or dominoes[j] == "R":
                        result = result + "." * dot_count
                    
                    # we have a left at j so we have to push left
                    else:
                        result = result + "L" * dot_count
                    
                    i = j
                
        return result
            
