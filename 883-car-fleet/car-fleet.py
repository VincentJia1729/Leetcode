class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pair = [[p,s] for p,s in zip(position, speed)]

        stack = []

        for p,s in sorted(pair, reverse = True): # sorts by position in decreasing order (7,4,1,0) 
            # print(p,s) 
            stack.append((target - p)/ s) # [3.0, 3.0, 4.5, 10.0]
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                # stack[-1] is the new car
                # stack [-2] is the old car
                # is the new car takes less time than the older car (t new car < t old car)
                # this means we collide
                # so the cars merge into a single car fleet
                stack.pop() # we pop off the new car. 

        return len(stack)
        