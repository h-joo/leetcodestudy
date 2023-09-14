// https://leetcode.com/problems/valid-palindrome-ii/
// Time Complexity: O(n), n: s.length()/2
// Space Complexity: O(1)
class Solution {
    public boolean validPalindrome(String s) {
        for (int begin = 0, end = s.length()-1; begin < end; ++begin, --end) {
            if (s.charAt(begin) != s.charAt(end)) {
                return compareCharacter(s, begin+1, end) || compareCharacter(s, begin, end-1);
            }
        }
        return true;
    }

    // check the other characters
    public boolean compareCharacter(final String s, int left, int right) {
        while (left < right) {
            if (s.charAt(left++) != s.charAt(right--))
                return false;
        }
        return true;
    }
}