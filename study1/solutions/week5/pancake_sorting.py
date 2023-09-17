# https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        length = len(arr)
        solution = []
        for i in range(length, 0, -1):
            idxOf = arr.index(i)
            if idxOf + 1 == i:
                arr = arr[:-1]
                continue
            arr[:idxOf+1] = arr[:idxOf+1][::-1]
            arr = arr[::-1][:-1]
            solution.append(idxOf + 1)
            solution.append(i)
        return solution

