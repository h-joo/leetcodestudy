# https://leetcode.com/problems/third-maximum-number/submissions/837300538/

# Note : This is actually a bad solution, you can do better without using a sort which is O(nlogn)
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        new_nums = sorted(nums)
        unique_num = set()
        
        for i in reversed(range(len(nums))):
            unique_num.add(new_nums[i])
            if len(unique_num) >= 3:
                return new_nums[i]
        
        return new_nums[-1]
