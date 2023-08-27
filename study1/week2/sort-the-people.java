class Solution {
    // Time Complexity: O(nlogn)
    // Space Complexity: O(1)
    public String[] sortPeople(String[] names, int[] heights) {
        // height becomes key because height is distinctive
        HashMap<Integer, String> pplHashMap = new HashMap<>(names.length);

        // put names and height into pplHashMap
        for (int i = 0; i < names.length; ++i) {
            pplHashMap.put(heights[i], names[i]);
        }

        ArrayList<Integer> heightSet = new ArrayList<>(pplHashMap.keySet());
        String[] nameArr = new String[names.length];

        // sorted in descending order by the heights -> O(nlogn)
        Collections.sort(heightSet, Collections.reverseOrder());

        int index = 0;
        for (Integer height : heightSet) {
            nameArr[index++] = pplHashMap.get(height);
        }

        return nameArr;
    }
}