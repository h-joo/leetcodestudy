// https://leetcode.com/problems/reduce-array-size-to-the-half/
// Time Complexity: O(n), n: arr.length
// Space Complexity: O(n), n: arr.length
// In order that at least half of the integers of the array are removed, the most numerous integer has to be removed first (The more integer are removed, the faster can the array be smaller)
class Solution {
    public int minSetSize(int[] arr) {
        int setSize = 0;
        HashMap<Integer, Integer> integerMap = new HashMap<>();

        // put value into map
        for (int a : arr) {
            integerMap.put(a, integerMap.getOrDefault(a, 0) + 1);
        }

        // in a descending order
        List<Integer> keyList = new ArrayList<>(integerMap.keySet());
        Collections.sort(keyList, (value1, value2) -> (integerMap.get(value2).compareTo(integerMap.get(value1))));

        int cntInteger = 0; // for counting the number of integers which are removed
        for (int key : keyList) {
            cntInteger += integerMap.get(key);
            setSize++;
            if (cntInteger >= arr.length/2) {
                return setSize;
            }
        }

        return setSize;
    }
}