class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        """
        happy_sum = use string operation to turn int to string
        while len(happy_sum) >= 1
            curr_sum = 0
            loop through each index of string
                turn back to int
                square and add to curr_sum
                
            if curr_sum is 1
                return true
            else
                happy_sum = str(curr_sum)
            
            edge case: the other single digits
                < 10 false except 7 which works
                add as elif in the end logic of the while loop

        """
        n_as_string = str(n)
        
        while len(n_as_string) >= 1:
            curr_sum = 0
            for i in range(len(n_as_string)):
                curr_sum += int(n_as_string[i])**2
            
            if curr_sum == 1:
                return True
            elif curr_sum < 10 and curr_sum != 7:
                return False
            else:
                n_as_string = str(curr_sum)
