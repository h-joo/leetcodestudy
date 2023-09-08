# https://leetcode.com/problems/reduce-array-size-to-the-half/description/
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count_number = {}
        for value in arr:
            if value not in count_number:
                count_number[value] = 0
            count_number[value] += 1
        
        accumulated_elems = 0
        for i, count in enumerate(sorted(count_number.values(), reverse=True)):
            accumulated_elems += count
            if accumulated_elems >= len(arr)/2:
                return i + 1