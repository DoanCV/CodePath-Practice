"""

Fetch 2 numbers from the 4 numbers.
Then try the operations on the two numbers. 
    Operations: num1 + num2, num1 - num2, num2 - num1, num1 * num2, num1 / num2, num2 / num1
        ignore num2 + num1 and num2 * num1 because they are same with num1 + num2, num1 * num2
Then you get a new number result from step 2 and now the problem becomes to can you get 24 with the 3 numbers(new number from step 2, and another 2 left in step 1), this is recursive.
The recursive base is there is only one number in the array and the number is 24.



when you try num1 / num2, you need check if the number is 0 or not.
Because there is division, then you may get a float number, so final result maybe not exactly same with 24. Take example 1/3 is 0.33333333, then you multiply 3, it is 0.999999, but here it's equal to 1. so you just need check the final result is nearly to 24 enough, take prevision 0.0001

O(6^N) time complexity since there are 6 operations we can do for each pair of numbers where N is the length of cards which is 4.
O(1) space complexity since base is size 2
"""

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        
        if len(cards) == 1 and abs(cards[0] - 24) <= 0.001:
            return True
        
        for i in range(len(cards) - 1):
            for j in range(i + 1, len(cards)):
                base = [cards[x] for x in range(len(cards)) if x != i and x != j]

                if self.judgePoint24(base + [cards[i] + cards[j]]):
                    return True
                if self.judgePoint24(base + [cards[i] * cards[j]]):
                    return True
                if self.judgePoint24(base + [cards[i] - cards[j]]):
                    return True
                if self.judgePoint24(base + [cards[j] - cards[i]]):
                    return True
                if cards[j] != 0 and self.judgePoint24(base + [cards[i] / cards[j]]):
                    return True
                if cards[i] != 0 and self.judgePoint24(base + [cards[j] / cards[i]]):
                    return True
                  
        return False
                
