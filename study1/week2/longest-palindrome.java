// https://leetcode.com/problems/longest-palindrome/
class Solution {
    // Time Complexity: O(n) -> 2 loop
    // Space Complexity: O(n) becausde of hashmap and char array
    public int longestPalindrome(String s) {
        char[] charArr = s.toCharArray();
        HashMap<Character, Integer> letterMap = new HashMap<>();
        int palindrome = 0;
        boolean isOne = false;

        // put key and value into letterMap
        for (char ch : charArr) {
            if (letterMap.containsKey(ch)) {
                letterMap.put(ch, letterMap.get(ch)+1);
            } else {
                letterMap.put(ch, 1);
            }
        }

        if (letterMap.keySet().size() == 1) {   // if only one letter exists
            return letterMap.get(charArr[0]);
        }

        for (Character ch : letterMap.keySet()) {
            if (letterMap.get(ch) % 2 == 0) { // the num of letter is even number
                palindrome += letterMap.get(ch);
            } else {    // the num of letter is odd number
                if (!isOne) {   // only one character which counts as odd number is permitted
                    palindrome += 1;
                    isOne = true;
                }
                palindrome += (letterMap.get(ch)-1);
            }
        }

        return palindrome;
    }
}