

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]: # if the end newInterval is before the beginning of the existing interval 
                res.append(newInterval)
                return res + intervals[i:] # immediatetly return
            elif newInterval[0] > intervals[i][1]: # if the beginning of new interval is larger than the end of the existing interval
                res.append(intervals[i]) # just add the existing interval normally
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        res.append(newInterval) # to catch if newInterval is at the very end
        return res