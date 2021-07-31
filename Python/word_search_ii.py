class trie:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False
    
    def insert(self, word):
        
        for i in word:
            
            if self.children[ ord(i) - ord("a") ] == None:
                self.children[ ord(i) - ord("a") ] = trie()
            self = self.children[ ord(i) - ord("a") ]
            
        self.isEnd = True
    

class Solution:
        
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        def dfs(row, column, t, s):
            if board[row][column] == "#":
                return 
            
            curr = board[row][column]
            board[row][column] = "#"
            
            t = t.children[ ord(curr) - ord("a") ]
            
            if t != None:
                substring = s + curr
                if t.isEnd:
                    result.add(substring)
                
                if row > 0:
                    dfs(row - 1, column, t, substring)
                
                if column > 0:
                    dfs(row, column - 1, t, substring)
                    
                if row < len(board) - 1:
                    dfs(row + 1, column, t, substring)
                    
                if column < len(board[0]) - 1:
                    dfs(row, column + 1, t, substring)
                    
            board[row][column] = curr
        
        """
        DFS recursion
        with a trie
            each child node of the trie is a letter of the alphabet
        """
        
        if len(board) == 0:
            return []
        
        t = trie()
        
        for word in words:
            t.insert(word)
        
        result = set()
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if t.children[ ord(board[i][j]) - ord("a") ] != None:
                    dfs(i, j, t, "")
                
        return list(result)
        
# O(N * M) time complexity, where N and M are the dimensions of the given board. We have to check every index.
# O(26^K) where k is the length of a word. We have 26 options in out trie and k is the depth of our path.
        
