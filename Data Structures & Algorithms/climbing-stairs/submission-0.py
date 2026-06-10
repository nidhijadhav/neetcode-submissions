class Solution:
    def climbStairs(self, n: int) -> int:

        if n < 3:
            return n

        prevTwo = 1
        prevOne = 2

        for i in range(3, n + 1):
            curr = prevOne + prevTwo
            prevTwo = prevOne
            prevOne = curr

        return prevOne
        