class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count_number = {}
        for value in arr:
            if value not in count_number:
                count_number[value] = 0
            count_number[value] += 1
        
        sorted_by_occurances = sorted([count for number, count in count_number.items()], reverse=True)
        
        accumulated_elems = 0        
        for i, count in enumerate(sorted_by_occurances):
            accumulated_elems += count
            if accumulated_elems >= len(arr)/2:
                return i + 1
        return len(sorted_by_sum)
