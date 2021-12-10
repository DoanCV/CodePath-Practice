"""
We have a 2D matrix of a candy crush board
  when we have 3 or more in a row or column we crush them
  then we let the candy above them fall and then we need to continue crushing
  when we are done crushing return the result state of the board

no new candy will spawn from above
positive integers represent the candy
0 means no candy in position i,j

seems like i will have to check the board everytime we crush and let the above candy fall
  loop through the board and try to crush candy
  if we are done then that means a scan of the board did nothing since it didnt crush candy


for the check we will use a sliding window of three candies
  that way anything in this window that has the same candy will be marked to get crushed
  to mark the candy we set the value equal to its negative value 

for the candy drop, we know it is by column
  this is the move 0s problem but on columns
"""


def candy_crush(board):
  # edge case: check for empty board
  if not board:
    return board

  done = True

  # crush rows
  for row in range(len(board)):
    for column in range(len(board[0]) - 2):

      num1 = board[row][column]
      num2 = board[row][column + 1]
      num3 = board[row][column + 2]

      if num1 == num2 and num2 == num3 and num1 != 0:
        board[row][column] = -num1
        board[row][column + 1] = -num2
        board[row][column + 2] = -num3

        done = False

  # crush columns
  for column in range(len(board[0])):
    for row in range(len(board) - 2):
      num1 = board[row][column]
      num2 = board[row + 1][column]
      num3 = board[row + 2][column]

      if num1 == num2 and num2 == num3 and num1 != 0:
        board[row][column] = -num1
        board[row + 1][column] = -num2
        board[row + 2][column] = -num3

        done = False

  # let the candy above fall down with gravity
  # loop through each column
    # in each column we will move positive values down similar to moving zeros problem
      # start from the bottom, i.e. last row
      # have a pointer on the bottom most negative value to set that to the candy above if we find it
      # when we hit the end of the column, i.e. last row, then the values from the pointer an up are 0s
  for column in range(len([0])):
    ptr = len(board) - 1
    for row in range(len(board) - 1, -1, -1):
      if board[row][column] > 0:
        board[ptr][column] = board[row][column] 
        ptr -= 1
    
    for curr_pos in range(ptr, -1, -1):
      board[curr_pos][column] = 0

  # if we made no changes in the most recent call to candy_crush
  if done:
    return board
  else:
    candy_crush(board)
