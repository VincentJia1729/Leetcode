class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        res = 0 # to track the number of intervals that should be removed
        prev_end = intervals[0][1] # the current smallest end

        
        for start, end in intervals[1:]:
            if start >= prev_end: # if no overlap
                prev_end = end # increment prev_end
            else:
                res += 1
                prev_end = min(end, prev_end) # this is to simulate removing the interval with larger end value
        return res