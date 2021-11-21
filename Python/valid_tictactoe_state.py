"""
We are given a state of a tic-tac-toe board, guaranteed 3x3
    Find if that state can be obtained from a game


We know that "X" has to go first so if the count of "O" is greater than that of "X" then the state is automatically invalid
Players also have to take turns so the difference between the two counts cannot be greater than 1

We also cannot have two winners
    if "O" won then we need to check if "X" also won and if that is the case we return False
        else we check if the count of "O" is equal to the count of "X" since "O" goes after "X" so a winning move has to make the counts equal
    
    if "X" won then the count of "O" must be less than that of "X" since the winning move is by "X"
"""

class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        
        
        def check_win_con(player):
            
            # check 3 in a row
            for row in range(len(board)):
                if board[row][0] == board[row][1] == board[row][2] == player:
                    return True
            
            # check 3 in a column
            for column in range(len(board[0])):
                if board[0][column] == board[1][column] == board[2][column] == player:
                    return True
                
            # check 3 in a diagonal
            if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
                return True
            
            return False
        
        
        
        X_count = 0
        O_count = 0
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    O_count += 1
                elif board[i][j] == "X":
                    X_count += 1
        
        if O_count > X_count or X_count - O_count > 1:
            return False
        
        if check_win_con("O"):
            if check_win_con("X"):
                return False
            else:
                return X_count == O_count
        
        if check_win_con("X"):
            if X_count != O_count + 1:
                return False
            
        return True
