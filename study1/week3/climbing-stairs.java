// https://leetcode.com/problems/climbing-stairs/
// Time complexity: O(n), n: input value
// Space complexity: O(1) because using only 3-size-array
class Solution {
    public int climbStairs(int n) {
        if (n == 1) {   // edge cases
            return 1;
        } else if (n == 2) {
            return 2;
        }

        int[] temp = new int[3];    // using dp
        temp[0] = 1;
        temp[1] = 2;

        for (int i = 2; i < n; ++i) {
            temp[2] = temp[0] + temp[1];
            temp[0] = temp[1];
            temp[1] = temp[2];
        }

        return temp[2];
    }
}