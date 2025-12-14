# The idea is similar to the previous problem
# we know that "O's" on the edges cannot be captured
# so we should do a dfs from the edge ofthe grid inward
# This way, any "O's" that form a chain will be marked
# All other "O's" that do not form a chain will not be marked, at the end, we will change the O's which are not marked to "X's" 
# Search for nearby "O's"

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        
        def dfs(r,c):
            # if we have already visited this cell
            if (r < 0 or r == ROWS or
            c < 0 or c == COLS or 
            board[r][c] == "#"):
                return 
            if (board[r][c] == "O"):
                board[r][c] = "#" # mark cells we visited with "#""
                dfs(r+1, c)
                dfs(r-1, c)
                dfs(r, c+1)
                dfs(r, c-1)

        # do DFS along edge rows and cols
        # top and bottom rows
        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)
        

        # left and right cols
        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS - 1)

        # Go through, change all "O's" to "X's"
        # Change all "#"'s to "O's"

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "#":
                    board[r][c] = "O"
                elif board[r][c] == 'O':
                    board[r][c] = "X"

        

        