// https://leetcode.com/problems/sort-the-people/submissions/
class Solution {
    // Time Complexity: O(nlogn)
    // Space Complexity: O(n) -> n(HashMap pplHashMap) + n(ArrayList heightSet) + n(String[] nameArr)
    public String[] sortPeople(String[] names, int[] heights) {
        // height becomes key because height is distinctive
        HashMap<Integer, String> pplHashMap = new HashMap<>(names.length);

        // put names and height into pplHashMap
        for (int i = 0; i < names.length; ++i) {
            pplHashMap.put(heights[i], names[i]);
        }

        String[] nameArr = new String[names.length];

        // sorted in descending order by the heights -> O(nlogn)
        Arrays.sort(heights);

        // put heights into nameArr
        for (int idx = 0 ; idx < heights.length ; ++idx ) {
            nameArr[heights.length - idx - 1] = pplHashMap.get(heights[idx]);
        }

        return nameArr;
    }
}