# https://leetcode.com/problems/pascals-triangle/
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        solution = [[1]]
        for row in range(1, numRows):
            new_arr = [1]
            solution.append(new_arr)
            for i in range(len(solution[row-1]) - 1):
                new_arr.append(solution[row-1][i] + solution[row-1][i + 1])
            new_arr.append(1)
        return solution
            