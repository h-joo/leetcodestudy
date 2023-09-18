# https://leetcode.com/problems/max-area-of-island/description/

def connected_land_space(grid, row, col, row_length, col_length):
    to_visit = [(row, col)]
    grid[row][col] = 2
    total_space = 0
    while to_visit:
        current_row, current_col = to_visit.pop()
        total_space += 1
        if current_row > 0 and grid[current_row - 1][current_col] == 1:
            grid[current_row - 1][current_col] = 2
            to_visit.append((current_row-1, current_col))
        if current_col > 0 and grid[current_row][current_col - 1] == 1:
            grid[current_row][current_col - 1] = 2
            to_visit.append((current_row, current_col - 1))
        if current_row < row_length - 1 and grid[current_row + 1][current_col] == 1:
            grid[current_row + 1][current_col] = 2
            to_visit.append((current_row + 1, current_col))
        if current_col < col_length - 1 and grid[current_row][current_col + 1] == 1:
            grid[current_row][current_col + 1] = 2
            to_visit.append((current_row, current_col + 1))

    return total_space

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row_length = len(grid)
        col_length = len(grid[0])
        max_area = 0
        for row in range(row_length):
            for column in range(col_length):
                if grid[row][column] != 1:
                    continue
                max_area = max(max_area, connected_land_space(grid, row, column, row_length, col_length))

        return max_area