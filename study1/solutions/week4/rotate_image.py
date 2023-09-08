# https://leetcode.com/problems/rotate-image/discussion/


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)

        for row in range(int(length/2)):
            for column in range(math.ceil(length/2)):
                tmp = matrix[row][column]
                matrix[row][column] = matrix[length - 1 - column][row]
                matrix[length - 1 - column][row] = matrix[length - 1 - row][length - 1 - column]
                matrix[length - 1 - row][length - 1 - column] = matrix[column][length - 1 - row]
                matrix[column][length - 1 - row] = tmp