def is_palindrome(check_palindrome):
    start, end = 0, len(check_palindrome) - 1

    while start < end:
        if check_palindrome[start] != check_palindrome[end]:
            return False
        start += 1
        end -= 1
    return True


class Solution:
    def validPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1

        while start < end:
            if s[start] != s[end]:
                return is_palindrome(s[start+1:end+1]) or is_palindrome(s[start:end])
            start += 1
            end -= 1
        return True
