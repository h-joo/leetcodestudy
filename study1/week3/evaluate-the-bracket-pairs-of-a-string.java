// https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string
// Time Complexity: O(n)
// Space Complexity: O(n), because of hashmap

class Solution {
    public String evaluate(String s, List<List<String>> knowledge) {
        StringBuilder result = new StringBuilder();
        HashMap<String, String> wordMap = new HashMap<>();  // key: word to be changed, value: changing word

        for (List<String> word : knowledge) {
            wordMap.put(word.get(0), word.get(1));
        }

        for (int i = 0; i < s.length(); ++i) {
            char ch = s.charAt(i);
            if (ch == '(') {    // bracket found
                int end = s.indexOf(")", i);
                result.append(wordMap.getOrDefault(s.substring(i+1, end), "?"));
                i = end;  // change index to the end
            } else {
                result.append(ch);
            }
        }

        return result.toString();
    }
}