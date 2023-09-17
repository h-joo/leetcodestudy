# https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 1:
            return 0 if s[0] == "0" else 1

        decodings = [1, 0 if s[0] == "0" else 1]
        index = 0
        for i in range(2, len(s) + 1):
            add = 0
            if '1' == s[i-2] or '2' == s[i-2] and s[i-1] < '7' :
                add += decodings[index]
            if s[i-1] != "0":
                add += decodings[index ^ 1]
            decodings[index] = add
            index ^= 1
        return decodings[len(s) % 2]