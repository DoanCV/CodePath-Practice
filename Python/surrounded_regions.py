"""
What does it mean to be surrounded?
    if an "O" is on the edge of the board then its not surrounded
    if an "O" is bordering an edge "O" and is connected by that vertically or horizontally then it is also not surrounded
        a path from this also means not surrounded
    otherwise flip the rest to an "X"
    
We can use DFS from the border when we find a "O"
    that way the "O" connected to the border "O" are also marked 

then we search through the entire board and flip "O" that have not been marked to "X" since those are surrounded
    flip the marked "O" back to "O"


O(N * M) time complexity, where N is the length of the board and M is the width of the board, since we have to visit every element of the board. We do this with double nested for loop.
We solve in place if we do not consider the recursive call stack. In the worst case our call stack would have snaked through every element as there are no "X".
"""

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # call dfs on the border
        for row in range(len(board)):
            self.dfs(row, 0, board)
            self.dfs(row, len(board[0]) - 1, board)
        for column in range(len(board[0])):
            self.dfs(0, column, board)
            self.dfs(len(board) - 1, column, board)
        
        # loop through the resulting board and flip marked "O" back to "O" and unmarked "O" to "X"
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != "marked":
                    board[i][j] = "X"
                else:
                    board[i][j] = "O"
        
        # do not return anything as instructed
        
        
    def dfs(self, row, column, board):
        # check if out of bounds or if not "O"
        if row < 0 or row > len(board) - 1 or column < 0 or column > len(board[0]) - 1 or board[row][column] != "O":
            return
        
        # flip if "O" to marked
        board[row][column] = "marked"
        
        # recurse in all four directions: up, down, left, right
        self.dfs(row + 1, column, board)
        self.dfs(row, column + 1, board)
        self.dfs(row - 1, column, board)
        self.dfs(row, column - 1, board)
