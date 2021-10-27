"""
shifts = []
cumulative_shifts = [sum(shifts[i:])]

conversion
ord((cumulative_shift[curr] + (ord(curr) - ord("a"))) % 26)

in the example:
[3,5,9] -> [17,14,9]
then we can apply the conversion on a list version of our string since we want to edit values

"""
    
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:    

        temp_string = []
        for i in range(len(s)):
            temp_string.append(s[i])
        
        cumulative_shifts = 0
        for position in range(len(temp_string) - 1, -1, -1):
            
            # shifts[i] = shifts[i + 1]
            # instead of starting from the left we can go backwards and reuse what we already computed
            # the shifts are cumulative
            
            cumulative_shifts += shifts[position]
            
            curr_ascii = ord(temp_string[position]) - ord("a")
            shift = (cumulative_shifts + curr_ascii) % 26
            temp_string[position] = chr(shift + ord("a"))
            
            
        return "".join(temp_string)
    


    def shiftingLetters_TLE_version(self, s: str, shifts: List[int]) -> str:
        cumulative_shifts = [ sum(shifts[i:]) for i in range(len(shifts)) ]
        
        temp_string = []
        for i in range(len(s)):
            temp_string.append(s[i])
        
        for position in range(len(temp_string)):
            
            temp_string[position] = chr((cumulative_shifts[position] + (ord(temp_string[position]) - ord("a"))) % 26 + ord("a"))
            
        return "".join(temp_string)
