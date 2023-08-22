// https://leetcode.com/problems/set-mismatch/
class Solution {
    // Time Complexity: O(n)
    // Space Complexity: O(n)
    public int[] findErrorNums(int[] nums) {
        int[] result = new int[2];
        int[] counting = new int[nums.length+1];

        // increment value at the corresponding number
        for (int n : nums) {
            counting[n]++;
        }

        for (int i = 1; i < counting.length; ++i) {
            if (counting[i] == 2) { // duplicated number
                result[0] = i;
            }
            if (counting[i] == 0) { // lost number
                result[1] = i;
            }
        }

        return result;
    }
}