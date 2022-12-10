import bisect
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:

        accumulated_sum = []
        accumulate = 0
        for num in sorted(nums):
            accumulate += num
            accumulated_sum.append(accumulate)
        
        answer = []
        for query in queries:
            insert_point = bisect.bisect_right(accumulated_sum, query)
            answer.append(insert_point)

        return answer

