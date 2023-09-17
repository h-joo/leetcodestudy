# https://leetcode.com/problems/binary-search/description/


# import bisect
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         index = bisect.bisect_right(nums, target)
#         return index - 1 if index > 0 and nums[index - 1] == target else -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        current = int((start + end)/2)
        while nums[current] != target:
            if start == end:
                return -1

            if target < nums[current]:
                end = min(current, end - 1)
                current = int((start + end)/2)
                continue
            
            start = max(current, start + 1)
            current = int((start + end)/2)

        return current

