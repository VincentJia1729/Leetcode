

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS , COLS = len(grid), len(grid[0])
       
        q = deque()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        time, fresh = 0,0 # time is how much time has elapsed, fresh is the number of fresh oranges 

        # go through the grid and count the number of fresh oranges
        # this way, when we finish "rotting", the oranges, we will know if we still have fresh oranges

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1: # 1 is a fresh orange
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c)) # add the coordinates of the place we need to start our BFS
        
        while q and fresh > 0: # if either one of these things is false, we stop the loop
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c # nc stands for new row / nc stands for new column
                    if (nr < 0 or nr == len(grid) or 
                        nc < 0 or nc == len(grid[0]) or
                        grid[nr][nc] != 1): # if you don't see a fresh orange
                        continue
                    grid[nr][nc] = 2 # set the fresh orange to a rotten orange
                    q.append((nr, nc))
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1



