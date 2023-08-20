// https://leetcode.com/problems/third-maximum-number/
class Solution {
    // Time Complexity: O(n), n: length of nums/ Runtime: 3ms
    // Space Compexity: O(n), n: length of nums/ Memory: 42.47MB
    public int thirdMax(int[] nums) {
        // make the array in an ascending order
        Arrays.sort(nums);
        int first = nums[nums.length-1];
        int second = nums[nums.length-1];

        if (nums.length < 3) {    // there is no maximum number
            return first;
        }

        // find third maximum number
        for (int i = nums.length-1; i >= 0; --i) {
            if (first == second && nums[i] < first) {
                second = nums[i];
                continue;
            } else if (nums[i] < second) {
                return nums[i];
            }
        }

        // if there is no third maximum number, return the maximum number
        return nums[nums.length-1];
    }
}