from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        """
        we know that nobody will blunder

        Simulate with two queues, one for R and one for D
            queue maintains order within the same group
            but within the whole game, we need to keep track of the index
        """

        STOP = len(senate)

        hardRs = deque(idx for idx, value in enumerate(senate) if value == "R")
        hardDs = deque(idx for idx, value in enumerate(senate) if value == "D")

        while hardRs and hardDs:
            softR = hardRs.popleft()
            softD = hardDs.popleft()

            # minimum gets to ban the other dude and then go back into its queue and wait its turn
            if softR < softD:
                hardRs.append(softR + STOP)
            else:
                hardDs.append(softD + STOP)
        
        if len(hardDs) > len(hardRs):
            return "Dire"
        else:
            return "Radiant"
