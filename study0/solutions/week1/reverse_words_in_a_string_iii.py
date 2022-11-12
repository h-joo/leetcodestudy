# https://leetcode.com/problems/reverse-words-in-a-string-iii/
class Solution:
    def reverseWords(self, s: str) -> str:        
        new_arr = []
        for split in s.split():
            new_arr.append(split[::-1])

        return " ".join(new_arr)
