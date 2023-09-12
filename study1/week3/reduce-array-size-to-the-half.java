// https://leetcode.com/problems/reduce-array-size-to-the-half/
// Time Complexity: O(n), n: arr.length
// Space Complexity: O(n), n: arr.length
// In order that at least half of the integers of the array are removed, the most numerous integer has to be removed first (The more integer are removed, the faster can the array be smaller)
class Solution {
    public int minSetSize(int[] arr) {
        HashMap<Integer, Integer> integerMap = new HashMap<>();

        // put value into map
        for (int a : arr) {
            integerMap.put(a, integerMap.getOrDefault(a, 0) + 1);
        }

        // in an ascending order
        List<Integer> counts = new ArrayList<>(integerMap.values());
        Collections.sort(counts);

        int cntInteger = 0; // for counting the number of integers which are removed
        int halfArray = arr.length / 2;
        int iterateIdx = counts.size() - 1;
        while (cntInteger < halfArray) {
            cntInteger += counts.get(iterateIdx);
            --iterateIdx;
        }
        return counts.size() - iterateIdx - 1;
    }
}