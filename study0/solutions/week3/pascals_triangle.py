class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        solution = [[1]]
        for row in range(1, numRows):
            new_arr = []
            for i in range(len(solution[row-1]) - 1):
                new_arr.append(solution[row-1][i] + solution[row-1][i + 1])
            solution.append([1] + new_arr + [1])
        return solution

