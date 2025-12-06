class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        sorted_stones = [-s for s in stones]
        heapq.heapify(sorted_stones) # so now stones is a max heap

        # continue "smashing" our heap contains at least 2 elements
        while len(sorted_stones) >= 2:
            big_stone = -heapq.heappop(sorted_stones) # pop largest element
            small_stone = -heapq.heappop(sorted_stones) # pop second largest element

            new_stone = big_stone - small_stone

            if new_stone > 0:
                heapq.heappush(sorted_stones, -new_stone) # these things are always done in place

        return -sorted_stones[0] if sorted_stones else 0
    