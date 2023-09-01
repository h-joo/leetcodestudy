// https://leetcode.com/problems/time-needed-to-inform-all-employees/
// This code results in Time Limit Exceeded
class Solution {
    // Time Complexity: O(n^2)
    // Space Complexity: O(n) -> becasue of stack
    public int numOfMinutes(int n, int headID, int[] manager, int[] informTime) {
        int maxMin = 0;
        Stack<Integer> relations = new Stack<>();

        relations.add(headID);

        // using DFS
        while (!relations.isEmpty()) {
            int index = relations.pop();
            int subordinatesTime = informTime[index];
            maxMin = maxMin > subordinatesTime ? maxMin : subordinatesTime;

            for (int i = 0; i < n; ++i) {
                if (manager[i] == index) {
                    informTime[i] += subordinatesTime;  // change value in informTime[i] to accumulated value
                    relations.push(i);
                }
            }
        }

        return maxMin;
    }
}