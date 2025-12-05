class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        pos_diagonal = set() # (r+c) is unique
        neg_diagonal = set() # (r-c) is unique

        result = []
        board = [["."]*n for i in range(n)]

        def backtrack(r): # the idea is that we start from the top row and decide which column to put in the Queen
            if r == n: # if we've hit the bottom row
                copy = ["".join(row) for row in board]
                result.append(copy)
                return
            for c in range(n): # go over all possible columns
                if ((c in col) or
                (r+c in pos_diagonal) or 
                (r-c in neg_diagonal)):
                    continue

                col.add(c)
                pos_diagonal.add(r+c)
                neg_diagonal.add(r-c)
                board[r][c] = "Q"

                backtrack(r+1)

                col.remove(c)
                pos_diagonal.remove(r+c)
                neg_diagonal.remove(r-c)
                board[r][c] = "."
        
        backtrack(0)
        return result


