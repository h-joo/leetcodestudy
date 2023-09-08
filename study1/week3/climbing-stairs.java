// https://leetcode.com/problems/climbing-stairs/
// Time complexity: O(n), n: input value
// Space complexity: O(1) because using only 3-size-array
class Solution {
    public int climbStairs(int n) {
        int[] temp = new int[]{1, 2};
        for (int i = 2; i < n; ++i) {
            temp[i % 2] = temp[0] + temp[1];
        }
        return temp[(n - 1) % 2];
    }
}