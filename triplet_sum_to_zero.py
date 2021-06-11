  """ 
  two pointer after sort with equation x + y + z = 0 => -x = y + z 
  sort is good since we can check adjacent elements to avoid duplicates

  keep track of:
  left = current position
  right = len(arr) - 1
    left and right will be the y and z
    for each x we negate then see if a pair sum is
  triplets
    return value
    array of arrays with 3 elements

  logic:
  we can split task up into two functions
    1. search triplets
      sort, no need to save input
      loop through the length of the array with x
        if previous value is the same 
          continue
        call search pair 
    2. search pair (takes in sorted array, -x, left (position of x + 1 as just x means that y = x or z = x which is not always true we do not want to reuse x in its own calculation since that introduces repeats), triplets)
      intialize right
      while left < right:
        y = value at left
        z = value at right
        if y + z == -x:
          append [x,y,z] to triplets
          left += 1
          right -= 1
          # get rid of duplicates
          while left < right and left prev is the same:
            left += 1
          while left < right and right next is the same:
            right -= 1
        elif y + z < -x:
          left += 1   
        elif y + z > -x:
          right -= 1
  """

def search_triplets(arr):
  triplets = []
  arr.sort()
  for x in range(len(arr)):
    if arr[x] == arr[x-1] and x > 0:
      continue
    find_pair(arr, -arr[x], x + 1, triplets)
  return triplets

def find_pair(arr, neg_x, left, triplets):
  right = len(arr) - 1
  while left < right:
    y = arr[left]
    z = arr[right]
    if neg_x == y + z:
      triplets.append([-neg_x,y,z])
      left += 1
      right -= 1
      while left < right and arr[left - 1] == arr[left]:
        left += 1
      while left < right and arr[right + 1] == arr[right]:
        right -= 1
    elif y + z < neg_x:
      left += 1
    else:
      right -= 1

