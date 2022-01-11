"""
U
we are given an n x n chessboard
    place n queens such that no two queens attack each other

M
queens cant be in the same row, column, diagonals
    we can use backtracking

P
keep a set of the columns, positive slope diagonals, negative slope diagonals
    positive slope diagonals: row + column will uniquely identify
    negative slope diagonals: row - column will uniquely identify

try each of the n positions in the first row
    then move on to the next row and try
    
at each step we store in the set

"""
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        columns = set()
        posSlopeDiagonal = set()
        negSlopeDiagonal = set()
        
        results = []
        board = [["." for _ in range(n)] for _ in range(n)]
        
        
        def dfs(row):
            
            # we are done if we exhausted the row
            if row == n:
                # return a copy in the correct format
                copy = ["".join(r) for r in board]
                results.append(copy)
                return 
            
            for col in range(n):
                
                # skip column if already used
                if col in columns or (row + col) in posSlopeDiagonal or (row - col) in negSlopeDiagonal:
                    continue
                
                columns.add(col)
                posSlopeDiagonal.add(row + col)
                negSlopeDiagonal.add(row - col)
                board[row][col] = "Q"
                
                dfs(row + 1)
                
                # backtrack
                columns.remove(col)
                posSlopeDiagonal.remove(row + col)
                negSlopeDiagonal.remove(row - col)
                board[row][col] = "."
        
        dfs(0)
        return results
