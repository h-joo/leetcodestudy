class Solution:
    def climbStairs(self, n: int) -> int:
        distinct_ways = [0, 1, 2, 3]    
        for i in range(4, n + 1):
            distinct_ways.append(distinct_ways[i - 1] + distinct_ways[i - 2])
        
        return distinct_ways[n]

