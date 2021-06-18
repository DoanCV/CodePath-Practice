"""
fast and slow pointers since we are trying to find a cycle and see if two two pointers meet at 1

find cycle
  calculate the square sum of the digits
  fast pointer do it twice in a loop
  slow pointer do it once a loop

"""

def find_happy_number(num):
  hare = num
  tortoise = num
  while hare is not None and tortoise is not None:
    hare = calculate_next(calculate_next(hare))
    tortoise = calculate_next(tortoise)
    if hare == tortoise:
      break
  return hare == 1

def calculate_next(num):
  sum = 0
  num = str(num)
  for i in range(len(num)):
    sum += int(num[i])**2
  return sum

# O(logN) time complexity, where N is the given number.
# O(1) space complexity since we are not creating new data structures.
