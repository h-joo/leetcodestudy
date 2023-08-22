// https://leetcode.com/problems/reverse-words-in-a-string-iii/
import java.util.Arrays;

class Solution {
    // Time Complexity: O(n), n: number of words in string..? / Runtime: 5ms
    // Space Complexity: O(n) / Memory: 44.13MB
    public String reverseWords(String s) {
        String[] wordArr = s.split(" ");
        StringBuffer result = new StringBuffer();

        // reverse the order
        for (String word : wordArr) {
            StringBuffer reversed = new StringBuffer(word);
            reversed.reverse();
            result.append(reversed);
            result.append(" ");
        }

        // delete last whitespace
        result.deleteCharAt(result.length()-1);

        return result.toString();
    }
}