class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        dict = {}
        for i in arr:
            if(i in dict):
                dict[i] += 1
            else: 
                dict[i] = 1
        
        if(len(set(dict.values())) == len(dict)):
            return True
        else:
            return False
