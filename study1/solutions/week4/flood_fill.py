# https://leetcode.com/problems/flood-fill/discussion/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        to_traverse = [(sr, sc)]
        row_count = len(image)
        column_count = len(image[0])
        original_color = image[sr][sc]
        image[sr][sc] = color

        while to_traverse:
            row, column = to_traverse.pop()
            if row > 0 and image[row - 1][column] == original_color:
                to_traverse.append((row - 1, column))
                image[row-1][column] = color
            if column > 0 and image[row][column - 1] == original_color:
                to_traverse.append((row, column - 1))
                image[row][column-1] = color
            if row < row_count - 1 and image[row + 1][column] == original_color:
                to_traverse.append((row + 1, column))
                image[row+1][column] = color
            if column < column_count - 1 and image[row][column + 1] == original_color:
                to_traverse.append((row, column + 1))
                image[row][column+1] = color

        return image
