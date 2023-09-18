# https://leetcode.com/problems/valid-palindrome-ii/

class Solution:
    def validPalindrome(self, s: str, checkError=True) -> bool:
        start, end = 0, len(s) - 1

        while start < end:
            if s[start] != s[end]:
                if checkError:
                    return self.validPalindrome(s[start+1:end+1], False) or self.validPalindrome(s[start:end], False)
                else:
                    return False
            start += 1
            end -= 1
        return True