# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        track_alpha = {}
        longest = 0
        
        for i, ch in enumerate(s):
            if ch in track_alpha:
                ch_prev_loc = track_alpha[ch] 
                if ch_prev_loc >= start:
                    start = track_alpha[ch] + 1
                    track_alpha[ch] = i
                    continue
            track_alpha[ch] = i
            longest = max(i - start + 1, longest)

        return longest