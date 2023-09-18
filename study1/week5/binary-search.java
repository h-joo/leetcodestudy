// https://leetcode.com/problems/binary-search/
// Time Complexity: O(logn)
// Space Complexity: O(1)
class Solution {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length-1;

        while (left <= right) {
            int mid = (left + right)/2;
            System.out.println("mid: " + nums[mid] + ", left: " + nums[left] + ", right: " + nums[right]);
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                left = mid+1;
            } else {
                right = mid-1;
            }
        }

        return -1;
    }
}