// https://leetcode.com/problems/invert-binary-tree/
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
    // Space Complexity: O(1)
    public TreeNode invertTree(TreeNode root) {
        swapNode(root);
        traverseTree(root);

        return root;
    }

    public void traverseTree(TreeNode node) {
        if (node != null) {
            if (node.left != null) {
                swapNode(node.left);
                traverseTree(node.left);
            }
            if (node.right != null) {
                swapNode(node.right);
                traverseTree(node.right);
            }
        }
    }

    public void swapNode(TreeNode node) {
        if (node == null) {
            return;
        }

        if (node.left != null && node.right != null) {
            TreeNode temp = node.left;
            node.left = node.right;
            node.right = temp;
        } else if (node.left != null) { // if node.right == null
            node.right = node.left;
            node.left = null;
        } else {    // if node.left == null
            node.left = node.right;
            node.right = null;
        }
    }
}