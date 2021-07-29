class Solution:
    def dfs(self, row, column, position, board, word):
        
            # check this first since we may already be out of bounds but we have verified the match
            if position == len(word):
                return True
            
            if row >= len(board) or column >= len(board[0]) or row < 0 or column < 0:
                return False
            
            if board[row][column] == word[position]:
                char = board[row][column]
                board[row][column] = " "
                
                match = (self.dfs(row + 1, column, position + 1, board, word) or 
                         self.dfs(row, column + 1, position + 1, board, word) or 
                         self.dfs(row - 1, column, position + 1, board, word) or 
                         self.dfs(row, column - 1, position + 1, board, word)
                        )
                
                board[row][column] = char
                
                return match

    
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        DFS on the character when we first find it and keep going until we get the word
            recurse up down left and right since letters are allowed to connect horizontally or vertically
        
        we need to keep track of position of each character since the word must be built sequentially
        
        def exist():
            we will loop through the row and columns of the matrix
                if we see a letter in the given word we will call our helper function
                    
            
        def dfs(self, given matrix, given word, row, column, word_position):
        
            if we are past the end of the word we have already verified the word
            
            check if we are out of bounds in the array
            
            
            flip the current character in the matrix to an empty space
            
            if we have a match
                recurse up down left and right with the next word_position
                    store match bool
            
            back track the empty space to the original character so we can use it in another search
            
            return the result of the recursion so far (the match bool)
            
        """
        
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if (self.dfs(i, j, 0, board, word)):
                        return True
        return False

# O(N * M) time complexity where N and M are the dimensions of the given matrix. We have to check every character in the matrix.
# O(N * M) space complexity since in the worst case our recursive call stack is at capacity which is when the word spans across the entire matrix.
