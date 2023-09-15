// https://leetcode.com/problems/rotate-image/
// Time Complexity: O(n^2), n: matrix.length
// Space Complexity: O(1)
class Solution {
    public void rotate(int[][] matrix) {
        // outer -> inner
        for (int i = 0; i < matrix.length/2; ++i) {
            int next = matrix.length - i - 1;
            for (int j = 0; j < matrix.length - 2 * i - 1; ++j) { // 4 cells are rotated
                int temp = matrix[i][i+j];
                matrix[i][i+j] = matrix[next-j][i];
                matrix[next-j][i] = matrix[next][next-j];
                matrix[next][next-j] = matrix[i+j][next];
                matrix[i+j][next] = temp;
            }
        }
    }

    /*
        4*4
        (0,0) (0,1) (0,2) (0,3)     (3,0) (2,0) (1,0) (0,0)
        (1,0) (1,1) (1,2) (1,3) =>  (3,1) (2,1) (1,1) (0,1)
        (2,0) (2,1) (2,2) (2,3)     (3,2) (2,2) (1,2) (0,2)
        (3,0) (3,1) (3,2) (3,3)     (3,3) (2,3) (1,3) (0,3)

        (0,0) -> (0,3) -> (3,3) -> (3,0)
        (0,1) -> (1,3) -> (3,2) -> (2,0)
        (0,2) -> (2,3) -> (3,1) -> (1,0)
        (0,3) -> (3,3) -> (3,0) -> (0,0)

        (1,1) -> (1,2) -> (2,2) -> (2,2)
    */
}