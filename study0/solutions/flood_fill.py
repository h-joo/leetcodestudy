class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        to_traverse = [(sr, sc)]
        row_count = len(image)
        column_count = len(image[0])
        original_color = image[sr][sc]

        while to_traverse:
            row, column = to_traverse.pop()
            if image[row][column] == color:
                continue
            image[row][column] = color
            if row > 0 and image[row - 1][column] == original_color:
                to_traverse.append((row - 1, column))
            if column > 0 and image[row][column - 1] == original_color:
                to_traverse.append((row, column - 1))
            if row < row_count - 1 and image[row + 1][column] == original_color:
                to_traverse.append((row + 1, column))
            if column < column_count - 1 and image[row][column + 1] == original_color:
                to_traverse.append((row, column + 1))

        return image
