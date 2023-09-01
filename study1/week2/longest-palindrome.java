// https://leetcode.com/problems/longest-palindrome/
class Solution {
    // Time Complexity: O(n) -> 2 loop
    // Space Complexity: O(n) becausde of hashmap and char array
    public int longestPalindrome(String s) {
        HashMap<Character, Integer> letterMap = new HashMap<>();

        // put key and value into letterMap
        for (int i = 0 ;i < s.length() ; ++i) {
            char ch = s.charAt(i);
            letterMap.put(ch, letterMap.getOrDefault(ch, 0) + 1);
        }

        boolean isOne = false;
        int palindrome = 0;
        for (Character ch : letterMap.keySet()) {
            int count = letterMap.get(ch);
            if ( count % 2 == 0) { // the num of letter is even number
                palindrome += count;
            } else {    // the num of letter is odd number
                if (!isOne) {   // only one character which counts as odd number is permitted
                    palindrome += 1;
                    isOne = true;
                }
                palindrome += count-1;
            }
        }

        return palindrome;
    }
}