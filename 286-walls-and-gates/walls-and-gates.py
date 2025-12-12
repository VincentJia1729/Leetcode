

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        
        ROWS, COLS = len(rooms), len(rooms[0])
        visited = set() # contains tuples (r,c)
        q = deque()
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        def visit_neighbor(r,c):
            for dr, dc in directions:
                nr, nc = r + dr, c +dc
                if (nr < 0 or nr == ROWS 
                    or nc < 0 or nc == COLS 
                    or (nr,nc) in visited 
                    or rooms[nr][nc] == -1):
                        continue # very important that this is not return
                visited.add((nr, nc))
                q.append((nr, nc))
                    



        # initialize the visited set with the coordinates of the gates
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append([r,c])
                    visited.add((r,c))
        dist = 0

        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                rooms[r][c] = dist
                visit_neighbor(r,c)
            dist += 1
        


