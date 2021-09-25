"""
Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know them but they do not know any of them.

Goal: You want to find out who the celebrity is or verify that there is not one.

Output: The number associated with the celebrity, or -1 if no celebrity present.

The only thing you are allowed to do is to ask questions like:

"Hi, A. Do you know B?" to get information of whether A knows B. 
You need to find the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given a helper function knows(a, b)-->bool which tells you whether A knows B.

Implement a function findCelebrity(n)-->int, your function should minimize the number of calls to knows(a, b).
"""

"""
we can start with the first potential celebrity
  we will check if that person knows anyone else
  if they do then they are not the celebrity and the person they know can be the celebrity

loop again to see if our candidate knows anyone earlier in the loop and if everyone else knows this candidate
  if our candidate knows someone or someone does not know them then there is no celebrity

this will look like a graph since the celebirty must have an indegree from all of the other nodes but no outdegrees
"""

def findCelebrity(N):
  candidate = 0
  
  for i in range(1, N):
    if knows(candidate, i):
      candidate = i
  
  for i in range(0, N):
    # we have to skip over checking if a candidate knows themself, that does nothing
    # we need to know if the candidate knows someone or if someone else does not know them because if either of those conditions are true we do not have a celebrity
    if i != candidate and (knows(candidate, i) or !knows(i, candidate)):
      return -1
  
  return candidate
