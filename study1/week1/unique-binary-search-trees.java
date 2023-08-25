// https://leetcode.com/problems/unique-binary-search-trees/
// References: https://st-lab.tistory.com/300
class Solution {
    // Time Complexity: O(n^2)
    // Space Complexity: O(n^2)
    public int numTrees(int n) {
        int numOfTree = 0;

        if (n <= 1) {
            return 1;
        }

        // using recursion
        for (int i = 1; i <= n; ++i) {
            int leftSubTree = numTrees(i - 1);
            int rightSubTree = numTrees(n - i);
            numOfTree += leftSubTree * rightSubTree;
        }

        return numOfTree;
    }
}