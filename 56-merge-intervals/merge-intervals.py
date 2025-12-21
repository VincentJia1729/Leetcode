class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda pair :pair[0]) # sort by starting the "start_i"
        output = [intervals[0]] # this just a list of lists containing a single element

        for start, end in intervals[1:]: # we go over the rest of the intervals
            last_end = output[-1][1] # this the most recent "end_i"

            if start <= last_end: # if there is an overlap
                output[-1][1] = max(last_end, end) # check which end is greater, modify in place
            else:
                output.append([start, end])
        return output