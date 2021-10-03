"""
U
we have an array of asteroids
    the magnitude is the size
    the sign is the direction
    there is no size 0 asteroid
    
they all go at the same speed

in a collision:
    the larger remains, smaller gets destroyed
    both get destroyed if they are the same size


any asteroid that is moving to the right can collide if there is something on the right that is moving left
    asteroids moving to the left but have nothing to the left can't collide
    asteroids moving to the right but have nothing to the right can't collide
    
return the result after collision

M
we can use a stack to keep track of asteroids we visited to potentiall collide them or just return them in the result since they finished colliding or never collided

P
loop through each asteroid and handle each one
    if we see a positive asteroid
        push to the stack

    if we see a negative asteroid

        if the top of our stack is positive
            # collide
            if they are equal pop and move onto the next asteroid in the outer loop
            
            if the current asteroid is greater in magnitude, pop the top of the stack and keep peeking our stack to see if it will collide more
            
            if the top of the stack is greater in magnitude than the current asteroid then move onto the next asteroid since the current one gets destroyed
        
        when we are done we still push our negative asteroid into the stack since it has nothing else to collide with

IRE

"""

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for asteroid in asteroids:
            
            while stack and stack[-1] > 0 and asteroid < 0:
                    
                    if -asteroid == stack[-1]:
                        stack.pop()
                        break
                    if -asteroid > stack[-1]:
                        stack.pop()
                        continue
                    if -asteroid < stack[-1]:
                        break
            
            else:
                stack.append(asteroid)
        # while-else for when we are done looking at the stack for now and we still have an asteroid to handle        
                
        return stack
