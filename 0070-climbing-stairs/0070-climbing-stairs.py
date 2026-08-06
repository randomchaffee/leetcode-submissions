# Aug 06, 2026 19:02
# this feels more like a combinatorics than a programming problem
# used dynamic programming 

class Solution:
    def climbStairs(self, n: int) -> int:
        # these two will represent the number of ways to reach the
        # current step from the two previous steps
        one = 1
        two = 1

        # basically, we iteratively build up the number of ways
        # from the base steps up to the n-th step
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        
        return one
