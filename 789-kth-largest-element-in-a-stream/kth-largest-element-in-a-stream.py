class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = nums # at this point, min_heap is a list
        self.k = k
        heapq.heapify(self.min_heap) # convert min_heap to a min-heap

        while len(self.min_heap)>k:
            heapq.heappop(self.min_heap) # automatically pops the smallest element

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val) # add value to heap

        # then if we have extra elements, pop the smallest value
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap) # pop the smallest value
        return self.min_heap[0] # the 0 index is automatically the smallest value