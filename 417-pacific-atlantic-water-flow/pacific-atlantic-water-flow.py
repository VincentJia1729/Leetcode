# the trick is to do DFS from the edges
# instead of water flowing downhill, we imagine ourselves climbing uphill from the ocean
# we will climb from the "Pacific side" and the "Atlantic side", and the cells which are part of both sets, can flow to both oceans

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set() # sets for "Pacific" and "Atlantic" which will contain cells which can visit each ocean respectively

        def dfs(r, c, visited, prev_height):
            if ((r,c) in visited or 
                r < 0 or r == ROWS or 
                c < 0 or c == COLS or 
                heights[r][c] < prev_height):
                return
            visited.add((r,c))
            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c]) # top row for Pacific
            dfs(ROWS - 1, c, atl, heights[ROWS-1][c]) # bottom row of Atlantic
        
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0]) # left column for Pacific
            dfs(r, COLS-1, atl, heights[r][COLS-1]) # right column for Atlantic

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl: 
                    res.append([r,c])
        return res
