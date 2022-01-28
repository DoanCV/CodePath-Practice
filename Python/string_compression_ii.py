"""
U
we are dealing with run length encoding which is
    "aabbbaa" => "a2b3a2"

given a string and an integer k, you need to delete at most k characters so that the run length encoded version has minimum length
    we do not have to use up all k

ex. "xyzaabbbaa" k = 3
greedy removes single characters
    if we remove a b from b3 that wont help since that just makes b2 which is the same length
    the only times we can get less length is
        b2
        b100
        b1000
        and so on since if i remove a b i get a shorter length
        
greedy gives us a2b3a2
    however greedy doesnt always work so we cant use it
    the best answer in this example is from removing the b
    xyza4 is shorter
    the greedy solution does not consider new groups that can be compressed after removing characters

we will need to try all possible deletion choices and memoize them


a unique state is defined as (position, current run encoding, run length of current set of identital characters, number of deletes remaining)
"""

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        
        memo = {}
        
        def dfs(position, curr_encoding_char, run_streak_length, deletes_remaining):
            
            if position == len(s):
                return 0
            
            key = (position, curr_encoding_char, run_streak_length, deletes_remaining) 
            if key in memo:
                return memo[key]
            
            # two choices, we try both
            # delete or keep
            # we get the minimum length between the two choices and save it to the key
            
            
            # try delete
            delete_cost = float("inf")
            if deletes_remaining > 0:
                delete_cost = dfs(position + 1, curr_encoding_char, run_streak_length, deletes_remaining - 1)
            
            # try keep
            # if the characters are the same so we can inlude it in the same encoding
                # however if we are going from "a" to "aa", ie a to a2 we are acutally increasing length
                # 99 to 100, 999 to 1000 etc also fall under the same umbrella
            # else we have to keep the current character and we cant condense it as of right now so that means our length has to increase by 1
            if s[position] == curr_encoding_char:
                
                extra_digit = 1 if run_streak_length == 1 or len(str(run_streak_length + 1)) > len(str(run_streak_length)) else 0
                
                keep_cost = extra_digit + dfs(position + 1, curr_encoding_char, run_streak_length + 1, deletes_remaining)
                
            else:
                keep_cost = 1 + dfs(position + 1, s[position], 1 , deletes_remaining)
            
            
            memo[key] = min(keep_cost, delete_cost)
            return memo[key]
        
        return dfs(0, "", 0, k)
