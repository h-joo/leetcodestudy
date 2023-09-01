// https://leetcode.com/problems/range-sum-of-bst/
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    // Time Complexity: O(n)
    // Space Complexity: O(n)
    int sum = 0; // sum of values in the range [low, high]

    public int rangeSumBST(TreeNode root, int low, int high) {
        if (root == null) {
            return sum;
        }

        if (root.val >= low && root.val <= high) {
            sum += root.val;
        }

        // traverse
        if (root.left != null) {
            rangeSumBST(root.left, low, high);
        }
        if (root.right != null) {
            rangeSumBST(root.right, low, high);
        }

        return sum;
    }
}