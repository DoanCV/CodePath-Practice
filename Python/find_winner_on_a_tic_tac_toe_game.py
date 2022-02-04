"""
Use 1 and -1 as flags
    check diagonals, r - c and r + c
    check rows
    check columns
"""

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        
        is_X_A = True
        
        rows = [0 for _ in range(3)]
        columns = [0 for _ in range(3)]
        neg_diagonal = 0
        pos_diagonal = 0
        
        for row, column in moves:
            
            if is_X_A:
                move = 1
            else:
                move = -1
                
            rows[row] += move
            columns[column] += move
            
            if row == column:
                neg_diagonal += move
                
            if row + column == 2:
                pos_diagonal += move
            
            if 3 in [abs(rows[row]), abs(columns[column]), abs(neg_diagonal), abs(pos_diagonal)]:
                return "A" if is_X_A else "B"
            
            is_X_A = not is_X_A
            
        return "Draw" if len(moves) == 9 else "Pending"
            
