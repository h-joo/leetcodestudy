// https://leetcode.com/problems/flood-fill/
// Time Complexity: O(n*m), n: image.length, m: image[0].length
// Space Complexity: O(1)
// using recursive methods
class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        if (image[sr][sc] == color) {
            return image;
        }

        int pixelColor = image[sr][sc]; // original color

        image[sr][sc] = color; // change the color of the pixel

        int[][] dir = new int[][]{{0, 1},{0, -1},{1, 0},{-1, 0}}; // up, down, right, left
        for (int i = 0; i < dir.length; ++i) {
            int nr = sr + dir[i][0];
            int nc = sc + dir[i][1];

            if (nr < 0 || nr >= image.length || nc < 0 || nc >= image[0].length) {
                continue;
            }
            if (image[nr][nc] == pixelColor) {
                floodFill(image, nr, nc, color);
            }
        }

        return image;
    }
}