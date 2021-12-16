"""
We see that people are split into pairs so there is an even amount of people
    we have list of lists where each index is a person and at each index we have the people they prefer in order
    if someone is paired with someone they do not prefer the most then they are unhappy
        very confusing, probably not most but mutual?
    
we can store the pairs in a hashmap
    hashmap = {person: set(everyone they prefer over their actual partner)}
    
loop through our map and then check the condition
  if not with the highest priority friend and if you can get a better match

O(N^2) time complexity where N is the number of people. For each person in the worst case we will check the other n - 1 people for the condition.
"""

class Solution:
    def unhappyFriends(self, n, preferences, pairs):
        
        pair_preference = {}
        for x, y in pairs:
            # everyone before your partner you prefer so we add them to a set
                # x's partner is y and y's partner is x
            pair_preference[x] = set( preferences[x][:preferences[x].index(y)] )
            pair_preference[y] = set( preferences[y][:preferences[y].index(x)] )
        
        unhappy = 0
        for x in pair_preference:
            for y in pair_preference[x]:
                
                if x in pair_preference[y]:
                    unhappy += 1
                    break
        
        return unhappy
