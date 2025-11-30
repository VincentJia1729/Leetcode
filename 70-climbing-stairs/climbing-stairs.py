class Solution:
    def climbStairs(self, n: int) -> int:
        # just notice the fact that you can implement the fibonacci sequence directly
        one, two = 1,1

        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one