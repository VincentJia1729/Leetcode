from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS, COLS = len(board), len(board[0]) 
        # we use full upper case letters for constant variables
        # assumption of a "rectangular" board

        path = set() # we need to keep track of our current index

        # use a recursive backtracking solution
        def dfs(r,c,i): 
            # r stands for "row index". r ranges from 0 to ROWS - 1
            # c stands for "column index" c ranges from 0 to COLS - 1
            # i is the index of how far you are into the word you are
            if i == len(word):
                return True
            # there are 4 different "break conditions" where we stop iterating and return False
            if (r< 0 or c < 0 or 
                r >= ROWS or c >= COLS or 
                word[i] != board[r][c] or
                (r,c) in path ):
                return False
                # let's break down all 4 "break conditions"
                # 1. we have gone too far up or too far left (out of bounds)
                # 2. we have gone too far down or too far right (out of bounds)
                # 3. at our current "r" and "c", board[r][c] does not match the letter word[i] 
                # 4. we have double counted an element on our path. You cannot reuse elements in path
            
            path.add((r,c)) # add a tuple containing r and c
            res = (dfs(r+1,c, i+1) or
                   dfs(r-1,c, i+1) or
                   dfs(r,c+1, i+1) or
                   dfs(r,c-1, i+1)) # if any of these subsearch returns True, then result is True
            path.remove((r,c))
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0): # if this condition returns True
                    return True
                
        return False