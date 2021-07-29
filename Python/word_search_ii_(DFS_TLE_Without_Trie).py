class Solution:
        
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        DFS recursion
        for each word in the list of words we will dfs through the matrix
        when we find the first letter of the word in the matrix we recurse through adjacent characters until we find a match or are out of bounds
            adjacent characters mean horizontally and vertically
        if there is a match we add the whole word to the output
        
        def dfs(self, ):
            
            check if out of bounds or if the first character does not match the current character in the matrix
                if they do not match return False
            
            flip the current character to an empty space or something that is not another letter
            
            recurse and save a match bool
                when we recurse we go up or down or left or right and we pass in the the word without the first character so we dont have to keep track of the position
            
            backtrack the current character change
            
            return the match bool
        
        def findWords():
            keep track of the valid words    
            
            for each word in words
                loop through the rows and columns of the given board
                    if the first character of the word matches the current character in the matrix, recurse
                        if there is a match and the word is not in the result, append the word to the result
                        
            return the result
                    
        """
        
        def dfs(board, word, row, column):
            
            if len(word) == 0:
                return True
            
            if row < 0 or column < 0 or row >= len(board) or column >= len(board[0]) or word[0] != board[row][column]:
                return False
            
            curr = board[row][column]
            board[row][column] = " "
            
            match = dfs(board, word[1:], row + 1, column) or dfs(board, word[1:], row - 1, column) or dfs(board, word[1:], row, column + 1) or dfs(board, word[1:], row, column - 1)
            
            board[row][column] = curr
            
            return match
        
        result = []
        
        for word in words:
            
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if (dfs(board, word, i, j)):
                        if word not in result:
                            result.append(word)
                            
        return result

      
# Time Limit Exceeded (TLE) since April 2021. The point is to use a trie so that means I need my own node class. I will still use DFS but on a trie.
