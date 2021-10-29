"""
One pass solution

start with the first key
    if the duration of the next key is longer then update
    if there is a tie return the one that is lexicographically larger (i.e we can literally use > or <)
"""

class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        
        answer_key = keysPressed[0]
        answer_duration = releaseTimes[0]
        
        for i in range(1, len(keysPressed)):
            
            curr_key = keysPressed[i]
            curr_duration = releaseTimes[i] - releaseTimes[i - 1]
            
            if (curr_duration > answer_duration) or (curr_duration == answer_duration and curr_key > answer_key):
                answer_key = curr_key
                answer_duration = curr_duration
                    
        return answer_key
