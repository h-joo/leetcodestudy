# https://leetcode.com/problems/set-mismatch/

# Note: There could be a better way to figure this out with bit manipulation.
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        summation = int((len(nums) + 1) * len(nums) / 2)
        actual_sum = 0
        exists = set()
        double = -1
        for num in nums:
            if num in exists:
                double = num
            else:
                exists.add(num)
            actual_sum += num
        return [double, summation - actual_sum + double]
