// https://leetcode.com/problems/n-th-tribonacci-number/
class Solution {
    // updated version considering feedback which uses the array with length 4
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    public int tribonacci(int n) {
        if (n == 0) {
            return 0;
        } else if (n == 1 || n == 2) {
            return 1;
        }

        int[] triboArr = new int[4];  // using dynamic programming
        triboArr[0] = 0;
        triboArr[1] = 1;
        triboArr[2] = 1;

        for (int i = 3; i <= n; ++i) {
            triboArr[3] = triboArr[0] + triboArr[1] + triboArr[2];
            triboArr[0] = triboArr[1];
            triboArr[1] = triboArr[2];
            triboArr[2] = triboArr[3];
        }

        return triboArr[3];
    }

//    // old version
//    public int tribonacci(int n) {
//        if (n == 0) {
//            return 0;
//        } else if (n == 1 || n == 2) {
//            return 1;
//        }
//
//        int[] triboArr = new int[n+1];  // using dynamic programming
//        triboArr[0] = 0;
//        triboArr[1] = 1;
//        triboArr[2] = 1;
//
//        for (int i = 3; i <= n; ++i) {
//            triboArr[i] = triboArr[i-3] + triboArr[i-2] + triboArr[i-1];
//        }
//
//        return triboArr[n];
//    }
}