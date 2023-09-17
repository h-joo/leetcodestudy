# https://leetcode.com/problems/longest-subsequence-with-limited-sum/description/

import bisect
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        accumulated_sum = []
        accumulate = 0
        for num in sorted(nums):
            accumulate += num
            accumulated_sum.append(accumulate)
        
        return (bisect.bisect_right(accumulated_sum, query) for query in queries)
