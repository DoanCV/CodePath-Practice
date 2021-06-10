def make_squares(arr):
  """ two pointers since negative and postive intergers are allowed and array is sorted so squaring equal magnitude is useless if only one is saved
  questions: 
  duplicates? yeah they're ok otherwise size of output is not always going to be the same size as input
  
  keep track of:
  start = 0
  end = len(arr) - 1
  squares
    return value
    array
    since we start from the two ends of the array, which will have highest magnitides and we want ordered result 
      we can fill this in backwards
      we do not have to worry about leading 0s when initalizing the result array since the size is the same as we are taking duplicates
  curr_result = len(arr) - 1

  logic:
  create squares as list of size len(arr) with all 0s
  initalize other variables metioned above

  # dont want them to cross
  while start < end:
    # calculate the squares of the values at indicies end and start 

    # compare the squares (order of checking does not matter)
    # if start result is greater than end result 
      # set the value of result at position curr_result to start
      # increment start by 1
    
    # else (end result is greater than start result or equal to)
      # set the value of result at position curr_result to end
      # decrement end by 1
      
    # when filled, move back one
    curr_result -= 1

  return squares

  ex.
  [-2,-1,0,1,2]
  [0,1,4]

  """

  squares = [0] * (len(arr))
  start = 0
  end = len(arr) - 1
  curr_result = len(arr) - 1

  while start < end:
    left_square = arr[start] ** 2
    right_square = arr[end] ** 2

    if left_square > right_square:
      squares[curr_result] = left_square
      start += 1
    else:
      squares[curr_result] = right_square
      end -= 1
    curr_result -= 1
  
  return squares

# O(N) time complexity, where N is the length of the given array, since we check every index of the array once
# O(1) space complexity since we are not creating new data structures.

"""
  alternate logic:
  zero_point, not a variable but a concept
    both pointers will start here
    it does not have to be zero but just first non negative since we need a boundary to begin comparing magnitudes
    one will move positive direction (forwards)
    other will move negative (backwards)
    ok i dont know how to stop the indexing so maybe try catch but i can just start outside and compare
  curr_pos
  curr_neg
"""
