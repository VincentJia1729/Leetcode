class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        left, right = 1, max(piles)
        current_best = right
    
        while left <= right: # standard binary search
            middle = (left + right) // 2
            temp_sum = 0
        
            # calculate amount of time required to eat bananas
            # remember that this is ceil(x / k) where x is the height of that particular pile
            for p in piles:
                temp_sum += math.ceil(p/middle)
        
            if temp_sum <= h: # you are eating too quick. Move pointer R down
                right = middle -1
                # store current best
                current_best = min(middle, current_best)
        
            else: # temp_sum > h: # you are eating too slow. Move pointer L up
                left = middle + 1

        return current_best

 

        