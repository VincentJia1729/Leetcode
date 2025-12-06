class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:        

        max_heap = []
        for x,y in points: 
            dist = -(x**2 + y**2)
            max_heap.append([dist, x,y]) # this must be written this way because heapq checks the front element first

        heapq.heapify(max_heap) # turn into max heap

        # start popping front elements

        while len(max_heap) > k:
            heapq.heappop(max_heap)

        
        # return the elements in the desried format

        res = []

        for i in range(len(max_heap)): # pop as many elements in max_heap
            dist, x , y = heapq.heappop(max_heap)
            res.append([x,y])

        return res