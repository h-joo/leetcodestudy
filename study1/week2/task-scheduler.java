// https://leetcode.com/problems/task-scheduler/
// This is incomplete codes.
class Solution {
    // Time Complexity:
    // Space Complexity:
    // considering greedy algorithm, choose the most numerouse task first in order to choose the shortest units of time
    // First idea: allocate from the largest one to the smallest.
    // for example, allocate the largest one with the distance n and then allocate next one in empty space
    // The problem: ["A", "A", "A", "B", "B", "B", "C", "C"], n = 1
    // -> my algorithm: A, B, A, B, A, B, C, i, C (9)
    // -> possible solution: A B A B A C B C (8)

    public int leastInterval(char[] tasks, int n) {
        if (n == 0) {   // case 1: n = 0
            return tasks.length;
        }

        int minOfUnit = 0;
        // int[] cntOfTask = new int[26]; // 'A'- 65 ... 'Z', there are only upper-case letter
        HashMap<Character, Integer> taskMap = new HashMap<>(); // key: task, value: count of tasks
        int maxTask = 0; // the count of most numerous task

        for (char task : tasks) {
            taskMap.put(task, taskMap.getOrDefault(task, 0) + 1);
            if (maxTask < taskMap.get(task)) {
                maxTask = taskMap.get(task);
            }
        }

        // the number of tasks is less than n
        // if (taskMap.size() > n) {
        //     return tasks.length;
        // } else {

        // }

        return 0;

    }
}