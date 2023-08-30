// https://leetcode.com/problems/n-th-tribonacci-number/
class Solution {
    // Time Complexity: O(n)
    // Space Complexity: O(n)
    public int tribonacci(int n) {
        if (n == 0) {
            return 0;
        } else if (n == 1 || n == 2) {
            return 1;
        }

        int[] triboArr = new int[n+1];  // using dynamic programming
        triboArr[0] = 0;
        triboArr[1] = 1;
        triboArr[2] = 1;

        for (int i = 3; i <= n; ++i) {
            triboArr[i] = triboArr[i-3] + triboArr[i-2] + triboArr[i-1];
        }

        return triboArr[n];
    }
}