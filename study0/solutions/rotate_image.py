def rotate_coordinates(row, column, length):
    return ((row, column), (column, length - 1 - row), (length - 1 - row, length - 1 - column), (length - 1 - column, row) )

def sub_rotate(matrix, row, column, length):
    original, first_rotate, second_rotate, third_rotate = rotate_coordinates(row, column, length)
    matrix[first_rotate[0]][first_rotate[1]], matrix[second_rotate[0]][second_rotate[1]], matrix[third_rotate[0]][third_rotate[1]], matrix[original[0]][original[1]] = matrix[original[0]][original[1]], matrix[first_rotate[0]][first_rotate[1]], matrix[second_rotate[0]][second_rotate[1]], matrix[third_rotate[0]][third_rotate[1]]

        
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        for row in range(int(length/2)):
            for column in range(math.ceil(length/2)):
                sub_rotate(matrix, row, column, length)
