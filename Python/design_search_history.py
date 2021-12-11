class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = []
        self.forward_history = []
        self.history.append(homepage)

    def visit(self, url: str) -> None:
        # add visited url to history
        self.history.append(url)
        
        # reset future
        self.forward_history = []

    def back(self, steps: int) -> str:
        # we want to have an element in the stack always
        while steps > 0 and len(self.history) > 1:
            curr_url = self.history.pop()
            self.forward_history.append(curr_url)
            steps -= 1
            
        return self.history[-1]
        

    def forward(self, steps: int) -> str:
        # future can be empty and if it is then we cant forward more than 0 steps so we return the same site again
        while steps > 0 and len(self.forward_history) > 0:
            curr_url = self.forward_history.pop()
            self.history.append(curr_url)
            steps -= 1
            
        return self.history[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

"""
Use two stacks

one will be used for the back command
the other for the forward
    we need this second one since if we were to go back and not store the order of the websites that we moved backwards through, we have no way of getting forwards
    
    
history stack takes in sites that we visit
when we pop from this stack to go back we push the popped website into the future stack
when we pop from the future stack to go forward we push it to the back stack


when we visit we have to clear the forward history which means to reset it
"""
