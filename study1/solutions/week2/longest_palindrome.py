class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = [0] * 58
        for char in s:
            char_count[ord(char) - ord('A')] += 1

        total_length = 0
        odd_number_exists = False
        for count in char_count:
            if count % 2 != 0:
                to_add = count - 1
                odd_number_exists = True
            else:
                to_add = count

            total_length += to_add

        return total_length + (1 if odd_number_exists else 0)