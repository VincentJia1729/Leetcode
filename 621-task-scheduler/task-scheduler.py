
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # assume sample tasks is like ["A","B","A","B","C"]
        count = Counter(tasks) # automatically creates a dictionary for us
        max_heap = [-cnt for cnt in count.values()] # you can createa  list using a counter
        heapq.heapify(max_heap) # so we have somethign like [-2,-2,-1]

        time = 0
        q = deque() # pairs of [-cnt, idle_time]

        while max_heap or q: # while max_heap or q non-empty
            time += 1
            if max_heap:
                cnt = 1 + heapq.heappop(max_heap)
                if cnt:
                    q.append([cnt, time + n]) 
            if q and q[0][1] == time: # immediately pop the values from q when we hit the appropriate time
                heapq.heappush(max_heap, q.popleft()[0]) #  q.popleft()[0] is "-cnt"
        return time