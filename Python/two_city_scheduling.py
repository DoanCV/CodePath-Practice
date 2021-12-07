"""
we have an array of tuples
    the array is size 2n since there are 2n people
    each index of the array has a tuple
        the cost of going to city a and the cost of going to city b
            every person has the choice to choose city a or city b
        
we want to minimize the cost of the trips and return that value
    there has to be n people that choose city a and n people who choose city b so we cant just take the minimum choice for each person
    we need to find the worst minimum choices

instead of trying all combinations we can use a heuristic
we can get the cost of getting all the people to choose city a
if we get all the differences between the costs we will know how much we can save by picking choice b over a or how much we save by sticking with city a

we can then sort the differences add the first n differences to our sum of city a
    this is our minimum


Proof from LC discussion:
Our heuristic gives solution S. In S, person x goes to B (in first half) and y goes to A (in second half).
Suppose there is a better solution S'. In S', x goes to A and y goes to B.
So cost(S) - cost(S') = (cost[x][1] + cost[y][0]) - (cost[x][0] + cost[y][1]) = (cost[x][1] - cost[x][0]) - (cost[y][1] - cost[y][0]).
As per our heuristic, x is in the first half and y is in the second half. And costs is sorted by cost[1]-cost[0]. So (cost[x][1] - cost[x][0]) < (cost[y][1] - cost[y][0]) and cost(S) - cost(S') < 0. So S' has higher cost is not a better solution, which leads to a contradiction.
So any modification to solution S will increase the cost. And S is the optimal solution.


"""

class Solution:
    def twoCitySchedCost(self, costs) -> int:
        result = []
        total_only_a = 0
        for cost_a, cost_b in costs:
            difference = cost_b - cost_a
            result.append(difference)
            total_only_a += cost_a
        
        result.sort()
        gain = 0
        for i in range(len(costs) // 2):
            gain += result[i]
            
        return total_only_a + gain
