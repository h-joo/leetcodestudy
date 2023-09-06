// https://leetcode.com/problems/pascals-triangle/
// Time Complexity: O(n^2), n: numRows
// Space Comlexity: O(n^2), n: numRows (Because there is a list which contains n lists)
class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> pascal = new ArrayList<List<Integer>>(1);
        List<Integer> rowList = new ArrayList<Integer>();   // row

        rowList.add(1); // numRows >= 1 => so there is always 1 on the top of triangle
        pascal.add(rowList);

        for (int i = 1; i < numRows; ++i) {
            List<Integer> temp = new ArrayList<Integer>();
            temp.add(1);    // first value in a row
            for (int j = 1; j < i; ++j) {
                temp.add(rowList.get(j-1) + rowList.get(j));
            }
            temp.add(1);    // last value in a row
            pascal.add(temp);
            rowList = temp;
        }

        return pascal;
    }

    /*
            1 -------- 0
           1 1 ------- 1
          1 2 1 ------ 2
         1 3 3 1 ----- 3
        1 4 6 4 1 ---- 4
      1 5 10 10 5 1 ---5
    */
}