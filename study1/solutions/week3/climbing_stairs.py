# https://leetcode.com/problems/climbing-stairs/description/
class Solution:
    def climbStairs(self, n: int) -> int:
        distinct_ways = [1, 2]    
        for i in range(2, n + 1):
            distinct_ways[i % 2] = distinct_ways[-1] + distinct_ways[-2]
        return distinct_ways[(n - 1) % 2]