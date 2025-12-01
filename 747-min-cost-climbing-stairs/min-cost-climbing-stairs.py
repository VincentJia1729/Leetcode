class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)

        # the solution is actually really easy if you are clever
        # remember Dynamic Programming principle of working backwards from the base case
        for i in range(len(cost) - 3, -1, -1):
            cost[i] = min(cost[i]+ cost[i+1], cost[i] + cost[i+2]) # rewrite the elements in the array
            # no need to create another array
        return min(cost[0], cost[1])