"""
Convert a n x m 2D array into a (n * m) x 1 1D array
"""

def convert(arr):
  """
  rowIndex * numberOfColumns + columnIndex
  """
  
  row_count = len(arr)
  column_count = len(arr[0])
  
  result = [0] * (row_count * column_count)
  
  if not arr:
    return result
      
  for i in range(row_count):
    for j in range(column_count):
      index = i * column_count + j
      result[index] = arr[i][j]
  
  return result
