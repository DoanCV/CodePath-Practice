def fruits_into_baskets(fruits):
  """ sliding window bc sounds like longest substring with k distinct characters where k = 2, array this time though
  keep track of:
  window_start = 0
  window_end
  tree_count
    hash table
  max_fruit_count = 0
    return value
    size of window
    we want to maximize this

  logic:
  loop over the length of the array with window_end
    if the fruit tree at index window_end is not in tree_count then add count = 0 (index hashtable)
    count += 1 (index hashtable)

    while len(tree_count) > 2:
      # shrink until we get only 2 distinct fruit
      subtract 1 from the window_start fruit tree count
      if the fruit_tree count for window_start is 0
        delete from hashtable
      add 1 to window_start

    # check the window size, update max if greater

  return max_fruit_count

  ex.
  [a,a,b,b,b,c,d]
  [a] valid, max = 1
  [a,a] valid, max = 2
  [a,a,b] valid, max = 3
  [a,a,b,b] valid, max = 4
  [a,a,b,b,b] valid, max = 5
  [a,a,b,b,b,c] invalid, must shrink
    [a,b,b,b,c]
    [b,b,b,c] valid, max = 5
  [b,b,b,c,d] invalid, must shrink
    [b,b,c,d]
    [b,c,d]
    [c,d] valid, max = 5
  """
  window_start = 0
  max_fruit_count = 0
  tree_count = {}

  for window_end in range(len(fruits)):
    end_fruit = fruits[window_end]
    if end_fruit not in tree_count:
      tree_count[end_fruit] = 0
    tree_count[end_fruit] += 1

    while len(tree_count) > 2:
      start_fruit = fruits[window_start]
      tree_count[start_fruit] -= 1
      if tree_count[start_fruit] == 0:
        del tree_count[start_fruit]
      window_start += 1

    if window_end - window_start + 1 > max_fruit_count:
      max_fruit_count = window_end - window_start + 1
  
  return max_fruit_count

  return -1

# O(N+N) => O(N) time complexity, where N is the length of the array, since the sliding window traverses the array once and there are no repeating calculations as the window_start and window_end trail together.
# O(3) => O(1) space complexity, since the max size of the hash table we insert into is 3. We stop at 3 since that is more than the number of baskets we have, 2, which can only have one type of fruit (key)
