from typing import List
import collections

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0]) 

        visited = set()
        res = 0 # counting the number of islands

        def bfs(r,c): 
            q = collections.deque()
            visited.add((r,c)) # add the coordinates you visited as a tuple
            q.append((r,c)) # add the coordinates you visited to the queue

            while q:
                row, col = q.popleft() # pop the most oldest element
                directions = [[1,0], [-1,0], [0,1], [0,-1]]

                for dr, dc in directions:
                    r_combined , c_combined = row + dr, col + dc
                    if ((r_combined) in range(ROWS) and # r_combined is in bounds 
                        (c_combined) in range(COLS) and # c_combined is in bouds
                        grid[r_combined][c_combined] == '1' and # we have found land
                        (r_combined, c_combined) not in visited): # that we have not visited before
                        q.append((r_combined,c_combined)) # add the value to the queue
                        # eventually we will reach a boundary of 0's so we will stop popping
                        visited.add((r_combined,c_combined))


        for r in range(ROWS):
            for c in range(COLS): 
                if grid[r][c] == "1" and (r,c) not in visited: # visited is the key way we keep track of our progress
                    bfs(r,c) # this will mark all cells in a particular island as "visited"
                    # this way, we ensure we do not double count an island
                    res += 1
        return res