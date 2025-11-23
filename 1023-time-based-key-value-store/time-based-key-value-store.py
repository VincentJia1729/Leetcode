class TimeMap:


    def __init__(self):
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:

        res = ""
        
        values = self.store.get(key,[]) # get the value at key, otherwise return an empty list
        # this will be something like [["bar1", 1],["bar2", 2]]

        # binary search, but notice how our "pointer" drifts upwards
        # it does not return "-1" if we do not find out desired target
        # for example if we have [1,2] and search for 5, we actually will point to 2
        l,r = 0, len(values) -1

        while l <= r:
            m = (l + r) //2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m-1
        return res
        
