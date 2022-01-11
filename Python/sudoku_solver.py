class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # make global in class    
        self.board = board
        self.solve()
        
    # find the next empty cell
    def findEmpty(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == ".":
                    return row, col
        return -1, -1
    
        
    def solve(self):
        row, col = self.findEmpty()
        
        # if no empty cells then we are done
        if row == -1 and col == -1:
            return True
        
        for num in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            
            if self.isSafe(row, col, num):
                
                self.board[row][col] = num
                
                if self.solve():
                    return True
                
                self.board[row][col] = "." # backtrack
                
        return False

    
    def isSafe(self, row, col, num):
        # find the start row and column of square to scan for validity
        box_row = row - row % 3
        box_col = col - col % 3
        
        if self.checkRow(row, num) and self.checkColumn(col, num) and self.checkSquare(box_row, box_col, num):
            return True
        
        return False
    
    
    def checkRow(self, row, num):
        
        for column in range(9):
            if self.board[row][column] == num:
                return False
            
        return True
    
    
    def checkColumn(self, col, num):
        
        for row in range(9):
            if self.board[row][col] == num:
                return False        
        
        return True
    
    
    def checkSquare(self, box_row, box_col, num):
        
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                
                if self.board[i][j] == num:
                    return False
        
        return True       
