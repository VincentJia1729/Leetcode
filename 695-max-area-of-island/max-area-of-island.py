
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: # to handle edge case of no input
            return 0
        
        ROWS, COLS = len(grid), len(grid[0]) # we can assume this because the grid is square
        visited = set()
        res = 0 # counting the size of the islands

        def dfs(r,c):
            # dfs needs to mark the nodes that we have visited
            # it also need to return the size of the island
            

            if (r < 0 or r == ROWS or 
            c < 0 or c == COLS or 
            grid[r][c] == 0 or (r,c) in visited):
                return 0    

            visited.add((r,c))

            size_island = 1
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            for dr, dc in directions:
                size_island += dfs(r + dr, c + dc)

            return size_island

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                    res = max(res, dfs(r,c))
        return res